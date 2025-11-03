'''
Created on 5 janv. 2015

@author: MRO
'''
import logging
import tempfile
import os
import sys
import glob
import imp
import inspect
from sqlalchemy import create_engine
from cast import Plugin
from . import KnowledgeBase, ApplicationLevelExtension, Application, Object, MetaModelConcepts
from .internal.find_plugins import get_plugins, call_application_level_extensions
from .internal.test_api import create_schema, clean_data, load_metamodel_from_disk, create_application, \
                               create_project, create_object_with_parent, create_link, create_object, \
                               add_property as create_property, add_link_property, create_file_with_parent, \
                               add_position as create_position, add_object_to_project
from .internal.test_api import add_link_position


def run(kb_name, application_name, engine=None, event='end_application'):
    """
    Run current app level plugin on a kb/application.
    
    The code calling this function should be located in a *tests* subfolder of the plugin.  
    
    :param engine: sqlalchemy engine, see :func:`cast.application.create_postgres_engine`
    """
    FORMAT = '%(message)s'
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)
    
    # for auto-upgrade
    logging.root.setLevel(logging.DEBUG)
    
    kb = KnowledgeBase(kb_name, engine)
    application = kb.get_application(application_name)

    test_class_file_path = ''
    is_test_class = False
    import traceback
    stack = traceback.extract_stack()
    for element in stack:
        if is_test_class:
            test_class_file_path = element[0]
            break
        if element[2] == 'run' and element[3] == 'testMethod()':
            # next element is the unit test file
            is_test_class = True

    pathname = os.path.dirname(test_class_file_path)
    plugin_path = os.path.abspath(os.path.join(pathname, '..'))

    for filepath in glob.glob(plugin_path + '/*.py'):

        temp = os.path.split(filepath)
        module_name, _ = os.path.splitext(temp[-1])
        try:
            sys.path.append(plugin_path)
            if module_name in sys.modules:
                del sys.modules[module_name]
            module = imp.load_source(module_name, filepath)
            plugin = None
            for name in dir(module):
                member = getattr(module, name)

                if inspect.isclass(member) and member.__module__ != 'cast.application':
                    
                    app_level = False
                    
                    for parent in member.__bases__:
                        if parent.__module__ + '.' + parent.__name__ == 'cast.application.ApplicationLevelExtension':
                            app_level = True
                            break
                    
                    if app_level:
                        
                        if not plugin:
                            plugin_directory = temp[0]
                            plugin = Plugin(plugin_directory)
                            get_plugins().append(plugin)
                        extension = member()
                        plugin.register_extension(extension)
                
                        plugin.__execution_context = (sys.modules.copy(), sys.path.copy())
            
        except Exception:
            print(traceback.format_exc())
            # may be normal because we also have python/C++ bindings
            # other way of avoiding it is to empty declare those bindings
            pass
    
    import cast.application.internal
    cast.application.internal.set_current_application(application)
    
    for plugin in get_plugins():
        
        plugin.set_temporary('')
        plugin.set_intermediate('')
        
    call_application_level_extensions(event, application)


engine = None
metamodel = None

class TestKnowledgeBase:
    """
    A fake knowledge base meant for testing.
    
    An application is already created inside.
    """
    
    def __init__(self):
        
        self._locked = False
        self.__get_schema()
        
        self.__application = create_application(self.engine, 'app')
        self.__kb = None
        
    def add_project(self, name, _type):
        """
        Add a result project to the application.
        This is the result of an analysis. 'Almost' an analysis unit result.
        
        :param _type: int or str the metamodel type of the project
        """
        self.check_lock()
        
        if type(_type) is str:
            _type = self.metamodel.get_category(_type).id
            
        return TestProject(create_project(self.engine, self.__application, name, _type),
                           name,
                           self.metamodel.get_category(id=_type),
                           self,
                           kb=self)
                           
    
    def run(self, method, log_level=None):
        """
        Run a function, or method having the application as parameter.
        """
        if log_level:
            
            FORMAT = '%(message)s'
            logging.basicConfig(format=FORMAT, level=log_level)
            
            # for auto-upgrade
            logging.root.setLevel(log_level)
            logging.info('') # new line
        else:
            logging.root.setLevel(logging.CRITICAL)
        
        # create a fake plugin using the parent folder as root
        #sume that we are in a subfolder tests of the plugin folder
        plugin = Plugin(self.__get_plugin_path())
        
        # we have our app
        application = self.get_application()
        
        # state the current context
        from cast.application.internal import set_current_application
        set_current_application(application)
        application.current_plugin = plugin
        try:
            method.__self__.plugin = plugin
        except:
            pass # allow also function unbounded
        
        # run...
        method(application)
        
        # finally run the saving ? maybe we should call the raw saver instead
        application._run_amt_saver()
        
        return application
    
    def get_application(self):
        """
        Returns the object representing the application
        
        After this call, no project can be added anymore, no link can be added through this API etc...
        
        :rtype :class:`cast.application.Application`
        """
        self._locked = True

        self.__kb = KnowledgeBase(None, engine=self.engine)
        return self.__kb.get_application("app")
    
    def check_lock(self):
    
        if self._locked:
            raise RuntimeError('You cannot modify the application anymore because you already called get_application.')

    def __get_schema(self):
        global engine, metamodel
        # create only once
        if not engine:
            engine = create_engine('sqlite://')
            self.engine = engine
            create_schema(self.engine)
            # load metamodel from files
            metamodel = load_metamodel_from_disk(self.engine)
            
        self.engine = engine       
        # clean the data tables
        clean_data(self.engine)

        self.metamodel = metamodel
    
    def __get_plugin_path(self):
        
        test_class_file_path = ''
        is_test_class = False
        import traceback
        stack = traceback.extract_stack()
        for element in stack:
            if is_test_class:
                test_class_file_path = element[0]
                break
            if element[2] == 'run' and element[3] == 'testMethod()':
                # next element is the unit test file
                is_test_class = True

        pathname = os.path.dirname(test_class_file_path)
        return os.path.abspath(os.path.join(pathname, '..'))
    
    metamodel = None
    engine = None

    def _get_metamodel_wrapper(self):
        if not hasattr(self, '_metamodel_wrapper'):
            self._metamodel_wrapper = MetaModelConcepts(self.metamodel)

        return self._metamodel_wrapper
    
    
class TestObject(Object):
    """
    An object created manually to set up a test
    """
    def __init__(self, identifier, name, typ, test_application, project_id, kb=None):
        Object.__init__(self, kb, identifier, name, typ)
        self.engine = test_application.engine
        self.project_id = project_id
        self.test_application = test_application

        self.has_position = False
        
    def add_object(self, name, fullname, _type, internal=True, keyprop=0):
        """
        Create a child object.

        :param _type: metamodel type int or str
        :rtype: :class:`TestObject`
        """
        self.test_application.check_lock()
        
        if type(_type) is str:
            _type = self.test_application.metamodel.get_category(_type).id

        _id = create_object_with_parent(engine=self.engine, 
                                        project_id=self.project_id, 
                                        name=name, 
                                        objtyp=_type, 
                                        parent_id=self.id, 
                                        internal=internal,
                                        fullname=fullname,
                                        keyprop=keyprop)
        return TestObject(_id, name, self.test_application.metamodel.get_category(id=_type), self.test_application, self.project_id, kb=self.kb)
    
    def add_file(self, name, fullname, _type, content='', internal=True, filename=None):
        """
        Create child file object with content. 
        
        :param content: str the content of the file 
        :param filename: str if given this will be the filename generated; or it can be an existing file.
        
        A temporary file is generated with given content.
        """
        self.test_application.check_lock()
        
        if type(_type) is str:
            _type = self.test_application.metamodel.get_category(_type).id

        
        if filename and os.path.exists(filename):
            file_path = filename
        else:
            temp_path = tempfile.mkdtemp()
            file_path = os.path.join(temp_path,filename if filename else 'file')
            file = open(file_path,'w', encoding='utf-8')
            file.write(content)
            file.close()

        _id = create_file_with_parent(engine=self.engine, 
                                      project_id=self.project_id, 
                                      name=name, 
                                      objtyp=_type, 
                                      path=file_path, 
                                      parent_id=self.id, 
                                      internal=internal)
        return TestObject(_id, name, self.test_application.metamodel.get_category(id=_type), self.test_application, self.id)
    
    
    def add_property(self, prop_name_or_id, value):
        """
        Add a property on an object.
        
        prop_name_or_id is the id of the metamodel property or its fullname, e.g., 'comment.commentBeforeObject'
        property must have INF_TYPE/INF_SUB_TYPE
        
        :param prop_name_or_id: int or string
        """
        self.test_application.check_lock()
        
        if type(prop_name_or_id) is str:
            _property = self.test_application.metamodel.get_property(name=prop_name_or_id)
        else:
            _property = self.test_application.metamodel.get_property(id=prop_name_or_id)
        
        inftyp = _property.get_attributes()['INF_TYPE']
        infsubtyp = _property.get_attributes()['INF_SUB_TYPE']
        
        create_property(self.engine, self.id, inftyp, infsubtyp, value)
    
    def add_position(self, _f, begin_line, begin_column, end_line, end_column):
        """
        Add a position on an object.

        :param _f: :class:`TestObject`
        """
        self.test_application.check_lock()

        create_position(self.engine, self.id, _f.id, begin_line, begin_column, end_line, end_column)
        
        self.has_position = True
        
    def add_to_project(self, project, internal=True):
        """
        Add the object to the project.
        
        @warning: only useful for objects belonging to multiple projects. Do not use it 
        unless you really know what youy are doing.
        TestObject.add_object already take care of adding the object to its main project.
        
        USed for some advanced tests.  
        """
        add_object_to_project(self.engine,self.id, project.id, internal)
    
    def __repr__(self):
        return 'TestObject(%s, %s)' % (self.name, self.get_type())


class TestProject(TestObject):
    """
    An object created manually to set up a test
    """
    def __init__(self, identifier, name, typ, test_application, kb=None):
        TestObject.__init__(self, 
                            identifier=identifier, 
                            name=name, 
                            typ=typ, 
                            test_application=test_application, 
                            project_id=identifier,
                            kb=kb)
            
    def add_link(self, _type, caller, callee):
        """
        Create a new link.
        
        :param _type: cast.application.LinkType
        :rtype: :class:`TestLink`
        """
        self.test_application.check_lock()
        
        _id = create_link(self.engine, self.id, caller.id, callee.id, _type)
        result = TestLink(_id, self.test_application)
        result.caller = caller
        result.callee = callee
        return result
        
        
        
    def __repr__(self):
        return 'TestProject(%s, %s)' % (self.name, self.get_type())

class TestLink:
    
    def __init__(self, identifier, test_application):
        
        self.id = identifier
        self.engine = test_application.engine
        self.test_application = test_application
        
        self.caller = None
        self.callee = None
        
    def add_property(self, prop_name_or_id, value):
        """
        Add a property on a link.
        
        prop_name_or_id is the id of the metamodel property or its fullname, e.g., 'comment.commentBeforeObject'
        property must have INF_TYPE/INF_SUB_TYPE
        
        :param prop_name_or_id: int or string
        """
        self.test_application.check_lock()
        
        if type(prop_name_or_id) is str:
            _property = self.test_application.metamodel.get_property(name=prop_name_or_id)
        else:
            _property = self.test_application.metamodel.get_property(id=prop_name_or_id)
        
        inftyp = _property.get_attributes()['INF_TYPE']
        infsubtyp = _property.get_attributes()['INF_SUB_TYPE']
        
        add_link_property(self.engine, self.id, inftyp, infsubtyp, value)

    def add_position(self, _f, begin_line, begin_column, end_line, end_column):
        """
        
        """
        self.test_application.check_lock()
        
        if not self.caller.has_position:
            raise RuntimeError('In order to add a position on a link, the caller must have a position')
        
        add_link_position(self.engine, self.id, _f.id, begin_line, begin_column, end_line, end_column)

    