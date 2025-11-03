'''
Created on 24 juil. 2014

@author: MRO
'''
from sqlalchemy import select, delete
import binascii
import logging
from .reflect import reflect_table
from collections import defaultdict


class Saver:
    """
    Saver using AMT saving.
    """
    def __init__(self, application, job_id, name, plugin_id, plugin_version):
        
        self.plugin_id = plugin_id
        self.plugin_version = plugin_version
        self.name = name
        
        self.user_project_id = application.id
        self.kb = application.kb
        self.kb._load_infsub_types()
        self.engine = self.kb.engine
        self.metadata = self.kb.metadata
        self.job_id = job_id
        
        # internal id 
        self.next_id = 1
        
        # sequence for object positions
        # apparently per file id 
        self.object_position_sequence = defaultdict(int)
        
        self.property_char_offset = 0
        self.property_int_offset = 0

        self.project_type = self.kb.plugin_project_type
        
        self.in_project_link = 1054
        self.parent_link = 1032
        
        self.IN_OBJECTS = reflect_table("IN_OBJECTS", self.metadata, self.engine) 

        self.IN_LINKS = reflect_table("IN_LINKS", self.metadata, self.engine)   
         
        self.IN_CHAR_PROPERTIES = reflect_table("IN_CHAR_PROPERTIES", self.metadata, self.engine)    
        
        self.IN_INT_PROPERTIES = reflect_table("IN_INT_PROPERTIES", self.metadata, self.engine)     
        
        self.IN_POSITIONS = reflect_table("IN_POSITIONS", self.metadata, self.engine) 

        self.cursor = self.kb.create_cursor()
        self.raw_connection = self.kb.raw_connection

        # saving cache : fill this and fill in tables latter
        self.in_objects = []
        self.in_links = []
        self.in_int_properties = []
        self.in_char_properties = []
        self.in_positions = []
        
        # guids to check for unicity
        self.guids = set()
        
        self._create_project(self.name)
        
        # projects on which this one depend (basically all projects so that we have dlm and others)
        # but do not take application level projects; see: AIPCORE-1685
        # 141887 : 'CAST_ApplicationPluginProject'
        self.dependent_projects = [project for project in application.get_projects() if project.get_metamodel_type().id != 141887]

        # for custom objects, we need to memorise a map :
        # ancestor --> custom objects
        self.projects_belonging = defaultdict(list)
        
        self.__saved_properties = set()
        self.__properties = []

    def add_link(self, link_type, caller, callee, bookmark=None):
        """
        Create a link between 2 objects.
        
        @param link_type: either an integer, a string or a Type
        @param caller: either an integer or an cast.application.Object
        @param callee: either an integer or an cast.application.Object
        """
        link_id = self.next_id
        self.next_id += 1

        AMT_id_type = 'E'
        KB_id_type = 'I'

        link_type_id = None
        if type(link_type) is int:
            link_type_id = link_type
        elif type(link_type) is str:
            link_type_id = self.kb.metamodel.get_category(name=link_type).id
        else:
            link_type_id = link_type.id
        
        self.in_links.append([self.job_id,
                              link_id,
                              caller if type(caller) is int else caller.id,
                              callee if type(callee) is int else callee.id,
                              
                              # special cases for isInProjectLink : no project
                              -1 if link_type_id in[self.in_project_link, 2671] else self.project_id, 
                              AMT_id_type if type(caller) is int else KB_id_type,
                              AMT_id_type if type(callee) is int else KB_id_type,
                              KB_id_type if link_type_id in[2671] else AMT_id_type,
                              link_type_id
                              ])
        
        if bookmark:
            self.add_link_bookmark(link_id, bookmark)
        
        return link_id

    def add_object(self, name, fullname, guid, object_type, parent, ancestor, external):
        """
        Create a new custom object
        
        :param parent: int or cast.application.Object
        :param ancestor: cast.application.Object, the ancestor of this object that is present in KB
        
        """
        # guid unicity...
        if guid in self.guids:
            logging.warning('Duplicate GUID %s (fullname %s), objects with that GUID will not be saved.' % (guid,fullname))
        self.guids.add(guid)
        
        # basic create
        _id = self._create_object(guid, object_type)

        # is in project of plugin
        project_link_id = self.add_link(1054, _id, self.project_id)
        self.add_property(project_link_id, self.kb.projectRelationKind, 1 if external else 0)
        
        # name fullname        
        self.add_property(_id, self.kb.identification_name, name)
        self.add_property(_id, self.kb.identification_fullname, fullname)
        
        # has a parent
        self.add_link('parentLink', _id, parent)
        
        # for project belongings to 'ancestor' project
        self.projects_belonging[ancestor.id].append(_id)

        return _id

    def add_link_bookmark(self, link, bookmark):
        """
        Save a bookmark on a link.
        """
        
        self.in_positions.append([self.job_id,
                                  link,
                                  bookmark.file.id,
                                  'I',
                                  0,  # sequence number are computed in base for links
                                  2,  # line/col position type
                                  bookmark.begin_line,
                                  bookmark.begin_column,
                                  bookmark.end_line,
                                  bookmark.end_column,
                                  -1
                                  ])

    def add_object_property(self, guid, _property, value):
        """
        Raw saving on existing objects
        
        :param guid: str
        :param _property: Property
        :param value: int or str or list of those
        """
        if _property.get_type() == 'string':
            if type(value) is str:
                pass
            elif type(value) is list:
                if len(value):
                    sample = value[0]
                    if not type(sample) is str:
                        raise RuntimeError('Incorrect value type for save_property : property is of string type')
            else:
                raise RuntimeError('Incorrect value type for save_property : property is of string type')
        elif _property.get_type() == 'integer':
            

            if type(value) is int:
                # because of storage in css
                if abs(value) > (2 ** 31 - 1):
                    raise RuntimeError('Value should be a 32 bit integer')
            elif type(value) is list:
                if len(value):
                    sample = value[0]
                    if not type(sample) is int:
                        raise RuntimeError('Incorrect value type for save_property : property is of integer type')
                for x in value:
                    if abs(x) > (2 ** 31 - 1):
                        raise RuntimeError('Value should be a 32 bit integer')
            else:
                raise RuntimeError('Incorrect value type for save_property : property is of integer type')

            
        else:
            raise RuntimeError('Property should be integer or string type')
        
        if (guid, _property) in self.__saved_properties:
            raise RuntimeError('Property already saved for object')
        
        self.__saved_properties.add((guid, _property))
        
        self.__properties.append((guid, _property, value))
        

        
    def add_property(self, object, property, value):
        
        if property.get_type() == 'string' and type(value) is str:

            
            values = [value]
    
            if len(value) > 255:
                values = [value[i:i+255] for i in range(0, len(value), 255)]
            
            char_block = 0
            
            for val in values:
                
                self.in_char_properties.append([self.job_id,
                                                object if type(object) is int else object.id,
                                                property.id,
                                                self.property_char_offset,
                                                char_block,
                                                val
                                                ])
                char_block += 1
            
            self.property_char_offset += 1

        elif property.get_type() == 'integer' and type(value) is int:
            
            self.in_int_properties.append([self.job_id,
                                           object if type(object) is int else object.id,
                                           property.id,
                                           self.property_int_offset,
                                           value
                                           ])

            self.property_int_offset += 1

    def save(self):
        """
        Really save.
        """
        # 1. 'cleanup' of created objects
        # find the result project for this saving phase
        project_kb_id = None
        query = select([self.kb.Keys.c.idkey]).where(self.kb.Keys.c.keynam == self.name).where(self.kb.Keys.c.objtyp == self.project_type.id)
         
        for line in self.engine.execute(query):
            project_kb_id = line[0]

        objinf = reflect_table("ObjInf", self.metadata, self.engine)
        objdsc = reflect_table("ObjDsc", self.metadata, self.engine)
        KeyPar = self.kb.KeyPar
        
        
        # then remove in project links to other projects  
        if project_kb_id:
            
            # we have added some internal project links to the objects on which we attached (for visibility in enlighten + belonging to AU/application)
            # but this is not what dictates lifetime
            # so first we remove those links... 
            clean = self.kb.ObjPro.delete().where(self.kb.ObjPro.c.idobj.in_(select([self.kb.ObjPro.c.idobj]).where(self.kb.ObjPro.c.idpro == project_kb_id))).where(self.kb.ObjPro.c.idpro != project_kb_id)
            self.engine.execute(clean)
        
            # AMT saving is a little confused with properties and do not update/remove properties of the created objects, so we handle properties ourselves
            clean = objinf.delete().where(objinf.c.idobj.in_(select([self.kb.ObjPro.c.idobj]).where(self.kb.ObjPro.c.idpro == project_kb_id)))
            self.engine.execute(clean)
             
            clean = objdsc.delete().where(objdsc.c.idobj.in_(select([self.kb.ObjPro.c.idobj]).where(self.kb.ObjPro.c.idpro == project_kb_id)))
            self.engine.execute(clean)

            # AMT saving apparently do not cleanup the parentship in our case
            clean = KeyPar.delete().where(KeyPar.c.idkey.in_(select([self.kb.ObjPro.c.idobj]).where(self.kb.ObjPro.c.idpro == project_kb_id)))
            self.engine.execute(clean)
            
        
        
        # calculate the new project belongings due to custom objects
        # we get the projects of the ancestors
        class FakeObject:
            def __init__(self, object_id):
                self.id = object_id
          
        # self.projects_belonging is empty when no custom object is saved
        # @todo : So need to skip this query
        query = select([self.kb.ObjPro.c.idobj, 
                        self.kb.ObjPro.c.idpro,
                        self.kb.ObjPro.c.prop]).where(self.kb.ObjPro.c.idobj.in_(self.projects_belonging.keys()))
          
        for line in self.engine.execute(query):
              
            ancestor = line[0]
            project = FakeObject(line[1])
            prop = line[2]
              
            for o in self.projects_belonging[ancestor]:
                # add the same for each descendant objects 
                link = self.add_link('isInProjectLink', o, project)
                self.add_property(link, self.kb.projectRelationKind, prop)
        
        self.guids.clear()
        
        # AMT saving
        self._empty_in_tables()
        
        logging.debug('executing cache_init %d ...', self.job_id)
        self.kb._execute_function(self.cursor, 'CACHE_INIT', '%s' % self.job_id)
        self.raw_connection.commit()
        logging.debug('executed')

        
        # add all the dependency to other projects
        for project in self.dependent_projects:
            link_id = self.add_link(1056, self.project_id, project)
            self.add_property(link_id, self.kb.dependencyKind, 0)
        
        # flush IN tables

        for val in self.in_links:
            val[0] = self.job_id
        ins = self.IN_LINKS.insert()
        self.cursor.executemany(str(ins.compile()), self.in_links)
        self.raw_connection.commit()
        self.in_links = []
        

        for val in self.in_objects:
            val[0] = self.job_id
        ins = self.IN_OBJECTS.insert()
        self.cursor.executemany(str(ins.compile()), self.in_objects)
        self.raw_connection.commit()
        self.in_objects = []

        for val in self.in_positions:
            val[0] = self.job_id
        ins = self.ins = self.IN_POSITIONS.insert()
        self.cursor.executemany(str(ins.compile()), self.in_positions)
        self.raw_connection.commit()
        self.in_positions = []

        for val in self.in_char_properties:
            val[0] = self.job_id
        ins = self.IN_CHAR_PROPERTIES.insert()
        self.cursor.executemany(str(ins.compile()), self.in_char_properties)
        self.raw_connection.commit()
        self.in_char_properties = []
        
        for val in self.in_int_properties:
            val[0] = self.job_id
        ins = self.IN_INT_PROPERTIES.insert()
        self.cursor.executemany(str(ins.compile()), self.in_int_properties)
        self.raw_connection.commit()
        self.in_int_properties = []
        
        # for debug
#         self._display_in_tables()
        
        logging.debug('executing cache_processid %d, %d ...', self.job_id, self.user_project_id)
        self.kb._execute_function(self.cursor, 'CACHE_PROCESSID', '%s,%s' % (self.job_id, self.user_project_id))
        self.raw_connection.commit()
        logging.debug('executed')
        logging.debug('executing cache_flushdata %d', self.job_id)
        self.kb._execute_function(self.cursor, 'CACHE_FLUSHDATA', '%s' % self.job_id)
        self.raw_connection.commit()
        logging.debug('executed')

        # raw saving
        if self.__properties:

            # custom insert of properties
            # get the guids/ids
            project_kb_id = None
            query = select([self.kb.Keys.c.idkey]).where(self.kb.Keys.c.keynam == self.name).where(self.kb.Keys.c.objtyp == self.project_type.id)
             
            for line in self.engine.execute(query):
                project_kb_id = line[0]
    
            # load the objects of the project
            objects_id_by_guid = {}
            # not really exact with guid > 1024 chars
            objects = reflect_table("OBJECTS", self.metadata, self.engine)
            query = select([objects.c.idkey, objects.c.idnam]).where(objects.c.idkey.in_(select([self.kb.ObjPro.c.idobj]).where(self.kb.ObjPro.c.idpro == project_kb_id)))
            for line in self.engine.execute(query):
                
                objects_id_by_guid[line[1]] = line[0] 
            
            integer_values = []
            string_values = []
            
            for guid, prop, value in self.__properties:
                
                object_id = objects_id_by_guid[guid]
                
                # handle list/non list 
                local_values = value
                if not type(value) is list:
                    local_values = [value]
                
                if prop.get_type() == 'integer':
                    
                    block_number = 0 
                    for elementary_value in local_values:
                        integer_values.append((object_id,
                                               prop.inftyp,
                                               prop.infsubtyp,
                                               block_number,
                                               elementary_value))
                        block_number += 1
                    
                elif prop.get_type() == 'string':
                    
                    block_number = 0 
                    for elementary_value in local_values:
                        for storable_value in split_utf8(elementary_value, 255):
                        
                            string_values.append((object_id,
                                                  prop.inftyp,
                                                  prop.infsubtyp,
                                                  block_number, 
                                                  0, # 
                                                  0,
                                                  storable_value))
                            block_number += 1
                        block_number += 1
                
            if string_values:
                # bulk insert
                ins = objdsc.insert()
                cursor = self.kb.create_cursor()
                cursor.executemany(str(ins.compile()), string_values)
                self.kb.raw_connection.commit()
    
            if integer_values:
                # bulk insert
                ins = objinf.insert()
                cursor = self.kb.create_cursor()
                cursor.executemany(str(ins.compile()), integer_values)
                self.kb.raw_connection.commit()
            

    def _create_project(self, name):
        """
        Creates the result project for that saving session.
        """
        self.project_id = self._create_object(name, self.project_type)
        
        link_id = self.add_link(1054, self.project_id, self.project_id)
        self.add_property(link_id, self.kb.projectRelationKind, 0)

        self.add_property(self.project_id, self.kb.identification_name, name)
        self.add_property(self.project_id, self.kb.identification_fullname, name)
        
        try:
            id_property = self.kb.metamodel.get_property(id=140567)
            version_property = self.kb.metamodel.get_property(id=140568)
            
            self.add_property(self.project_id, id_property, self.plugin_id)
            self.add_property(self.project_id, version_property, self.plugin_version)
            
        except KeyError:
            # before 7.3.6
            pass
        

    
        
    def _create_object(self, guid, object_type):
        
        short_guid = guid[0:600]
        
        long_guid = guid
        if len(long_guid) > 1000:
            crc = binascii.crc32(long_guid)
            long_guid = '%s <#%08X>' % (long_guid[0:1000], crc)
        
        object_id = self.next_id
        self.next_id += 1
        
        self.in_objects.append([self.job_id,
                                object_id,
                                long_guid, # so called guid
                                short_guid, # guid but with max 600
                                object_type if type(object_type) is int else object_type.id
                                ])
        
                    
        return object_id
    
    def _empty_in_tables(self):
        
        ins = self.IN_OBJECTS.delete().where(self.IN_OBJECTS.c.session_id == self.job_id)
        self.engine.execute(ins)
        
        ins = self.IN_LINKS.delete().where(self.IN_LINKS.c.session_id == self.job_id)
        self.engine.execute(ins)
        
        ins = self.IN_CHAR_PROPERTIES.delete().where(self.IN_CHAR_PROPERTIES.c.session_id == self.job_id)
        self.engine.execute(ins)

        ins = self.IN_INT_PROPERTIES.delete().where(self.IN_INT_PROPERTIES.c.session_id == self.job_id)
        self.engine.execute(ins)
        
        ins = self.IN_POSITIONS.delete().where(self.IN_POSITIONS.c.session_id == self.job_id)
        self.engine.execute(ins)
    
    def _display_in_tables(self):
        
        logging.info('IN_OBJECTS :')
        self.cursor.execute("select * from IN_OBJECTS")
        self._print_result()

        logging.info('IN_LINKS :')
        self.cursor.execute("select * from IN_LINKS")
        self._print_result()

        logging.info('IN_CHAR_PROPERTIES :')
        self.cursor.execute("select * from IN_CHAR_PROPERTIES")
        self._print_result()

        logging.info('IN_INT_PROPERTIES :')
        self.cursor.execute("select * from IN_INT_PROPERTIES")
        self._print_result()

        logging.info('IN_POSITIONS :')
        self.cursor.execute("select * from IN_POSITIONS")
        self._print_result()

    def _print_result(self):
        for line in self.cursor:
            logging.info('%s', str(line))
        
    def _add_dependency(self, o):
        """
        Add a dependency to the object's project
        """
        if type(o) is int:
            return
        
        for project in o.get_projects():
            self.dependent_projects.add(project)


def split_utf8(s, n):
    """Split UTF-8 s into chunks of maximum length n."""
    while len(s) > n:
        k = n
        while (ord(s[k]) & 0xc0) == 0x80:
            k -= 1
        yield s[:k]
        s = s[k:]
    yield s
