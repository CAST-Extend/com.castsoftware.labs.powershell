"""
The part to be maintained

"""
from .. import Application, Bookmark, Database, DatabaseOwner, DatabaseSubset, File, ApplicationLevelExtension
from .. import KnowledgeBase, Object, Project, Reference, ReferenceFinder, CustomObject
from .. import LinkType, LinkQuery, ObjectQuery, EnlightenLink, create_link, open_source_file, publish_report
from .. import ModuleContent, Combined, read_enlighten_connection_profiles, read_servman_connection_profiles, ConnectionSharing
from .. import DMTApplication, DMTVersion, DMTPackage
from ..central import CentralBase, Snapshot as central_Snapshot, Application as central_Application
from ..managment import ManagmentBase, Application as managment_Application, AnalysisUnit, Package, Module, Snapshot as managment_Snapshot
from ..server import Server
from ..setup import CASTAIP
from ..test import run
from . import is_debug_log
from .find_plugins import new_call_application_level_extensions, new_analysis_has_warnings
import traceback
from ..test import TestKnowledgeBase
from functools import partial


# only public API here of __init__
patch_classes_names = {'Application':Application,
                       'ApplicationLevelExtension':ApplicationLevelExtension,
                       'Bookmark':Bookmark,
                       'CustomObject':CustomObject, 
                       'Database':Database, 
                       'DatabaseOwner':DatabaseOwner, 
                       'DatabaseSubset':DatabaseSubset, 
                       'File':File, 
                       'KnowledgeBase':KnowledgeBase, 
                       'Object':Object, 
                       'Project':Project, 
                       'Reference':Reference, 
                       'ReferenceFinder':ReferenceFinder,
                       'ObjectQuery':ObjectQuery,
                       'LinkQuery':LinkQuery,
                       'EnlightenLink':EnlightenLink,
                       'LinkType':LinkType,
                       'ConnectionSharing':ConnectionSharing, 
                       'CentralBase':CentralBase,
                       'Application':central_Application,
                       'CentralSnapshot':central_Snapshot,
                       
                       'ManagmentBase':ManagmentBase,
                       'ManagmentApplication':managment_Application,
                       'Module':Module,
                       'Package':Package,
                       'AnalysisUnit':AnalysisUnit,
                       'ModuleContent':ModuleContent,
                       'ManagmentSnapshot':managment_Snapshot,
                       
                       'DMTApplication':DMTApplication,
                       'DMTVersion':DMTVersion,
                       'DMTPackage':DMTPackage,
                       
                       'Combined':Combined,
                       'Server':Server,
                       
                       'CASTAIP':CASTAIP
                       }

# files other than __init__
patch_classes = {'central': {'CentralBase':CentralBase,
                             'Application':central_Application,
                             'Snapshot':central_Snapshot}, 
                 'managment' : {'ManagmentBase':ManagmentBase,
                                'Application':managment_Application,
                                'AnalysisUnit':AnalysisUnit,
                                'Package':Package,
                                'Module':Module,
                                'ModuleContent':ModuleContent,
                                'Snapshot':managment_Snapshot},
                 'server':{'Combined':Combined,
                           'Server':Server},
                 'setup':{'CASTAIP':CASTAIP},
                 'test':{'TestKnowledgeBase':TestKnowledgeBase}}


####################
## install part
####################
   

import sys
import cast.application
import inspect
from distutils.version import StrictVersion
import logging
import functools


cast_module = sys.modules["cast.application"]


def get_version(cast_module):
    
    if hasattr(cast_module, '__version__'):
        return getattr(cast_module, '__version__')
    else:
        return '1.0.0' # older version had no version variable so it is 1.0.0

def patch_module_classes(module, patch_classes_names):
    """
    :param module: the module object to be patched
    :param patch_classes_names: a map class name --> class containing the replacement classes
    """
    clsmembers = inspect.getmembers(module, inspect.isclass)
    patched_classes = []
    
    for cast_class in clsmembers:
        
        class_name = cast_class[0]
        class_object = cast_class[1]
        
        if class_name in patch_classes_names:
            # class is to be patched
            
            patched_classes.append(class_name)
#                 print(class_name)
            patch_class=patch_classes_names[class_name]
            
            # patch each member method of the class
            for m in inspect.getmembers(patch_class, inspect.isroutine):
                member_name = m[0]
#                     print('     ', member_name, m[1])
                setattr(class_object, member_name, m[1])
    
    # remaining classes : directly added to module
    for name, cls in patch_classes_names.items():
        
        if not name in patched_classes:
            
            setattr(cast_module, name, cls)

def patch_application(application):
    """
    Patch an application object itself by replacing the methods and adding new ones
    for > 8.0.0
    """
    if not application:
        return

    for m in inspect.getmembers(Application, inspect.isroutine):
        member_name = m[0]
        if member_name.startswith('__') and member_name.endswith('__'):
            pass # predefined...
        else:
            setattr(application, 
                    member_name,
                    # binding of self... see https://stackoverflow.com/questions/277922/python-argument-binders 
                    functools.partial(m[1], application))
    
    

def apply_patch(version):

    if StrictVersion(get_version(cast_module)) < StrictVersion(version):
        """
        lower version so we install ourselves
        """
        setattr(cast_module, '__version__', version)
        
        logging.info('Upgrading API version to  %s', version)

        logger = logging.getLogger()
        
        # get the log level...
        if is_debug_log():
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)
            
            
        patch_module_classes(cast_module, patch_classes_names)
        
        # functions 
        setattr(cast_module, 'create_link', create_link)
        setattr(cast_module, 'open_source_file', open_source_file)
        setattr(cast_module, 'read_enlighten_connection_profiles', read_enlighten_connection_profiles)
        setattr(cast_module, 'read_servman_connection_profiles', read_servman_connection_profiles)
        setattr(cast_module, 'publish_report', publish_report)
        
        # other packages
        
        # example : lib_cast_upgrade_1_5_4.server
        lib_module_name = 'lib_cast_upgrade_' + version.replace('.', '_')
        
        def patch_module(module_name):
            
            final_module_name = 'cast.application.' + module_name
            
            try:
                module = sys.modules[final_module_name]
                patch_module_classes(module, patch_classes[module_name])
            except:
                # given module does not exist in the AIP release 
                module = sys.modules[lib_module_name + '.' + module_name]
                sys.modules[final_module_name] = module
        
        patch_module('central')
        patch_module('managment')
        patch_module('server')
        patch_module('setup')
        patch_module('test')

        test_module = sys.modules['cast.application.test']
        setattr(test_module, 'run', run)

        # patch run helper for tests
                  
        # non generic
        # for > 8.0.0
        try:
            from cast.application.internal import get_current_application
            if get_current_application() and hasattr(get_current_application(), 'kb'):
                try:
                    patch_application(get_current_application())
                    # reload projects
                    get_current_application()._calculate_project_list()
                except:
                    # here : not really good...
                    logging.warning(traceback.format_exc())
        except:
            # here probably 7.3.x
            pass
        
        
        # hot hot upgrade : still in progress...
        try:
            # replace some internals already loaded...
            # functions are already loaded by the main script so we use frame...
             
            # find the frame_object for main
            frame_object = None
            
             
            for frame in inspect.stack():
                if frame[3] == 'main':
                    frame_object = frame[0]
                    break
             

            # this is the "original" function : the one that will return the plugin list
            original_get_plugins = frame_object.f_globals['get_plugins']
             
            # replace stuff from main function 
            # here we replace the referenced function from the run_plugin code
            # when calling call_application_level_extensions it will be our new function called
            # we need to pass the get_plugins to give visibility to the plugin list
            frame_object.f_globals['call_application_level_extensions'] = partial(new_call_application_level_extensions, original_get_plugins)
            frame_object.f_globals['analysis_has_warnings'] = partial(new_analysis_has_warnings, original_get_plugins)
        except:
            pass
        
        
        logging.info('Ugrading done')
        