import os.path
import re
import glob
import imp
import traceback
import inspect
import logging
import cast.application
import sys
import platform
import cast.analysers.internal.plugin
from . import set_current_plugin
from .reflect import reflect_table
from distutils.version import StrictVersion
from sqlalchemy import Table, MetaData, select


application_level_plugins = []
"""List of plugins containing application level extensions"""


def get_plugins():
    global application_level_plugins
    return application_level_plugins

def set_plugins(plugins):
    global application_level_plugins
    application_level_plugins = plugins

has_warnings = False

def analysis_has_warnings():
    global has_warnings
    return has_warnings


def new_analysis_has_warnings(param_get_plugins):
    """
    Hacky...
    We have stored the has warning on plugin objects
    """
    plugins = param_get_plugins()
    
    for plugin in plugins:
        if hasattr(plugin, '_has_warnings'):
            return True
    
    return False    


def _get_execution_context():
    "Return execution context"
    return (sys.modules.copy(), sys.path.copy())


def _restore_execution_context(context):
    "restore an execution context"
    sys.modules.clear()
    sys.modules.update(context[0])
    sys.path = context[1]


# magic here...
def new_call_application_level_extensions(param_get_plugins, method_name, parameter):
    
    
    plugins = param_get_plugins()
    
    def call(plugin, method_name, parameter):
        
        context = _get_execution_context()
        
        setattr(parameter, 'current_plugin', plugin)
        
        logging.info("Running plugin %s...", plugin.get_name())
        
        set_current_plugin(plugin)
        
        try:
            _restore_execution_context(plugin.__execution_context)
            plugin._call_extension2('cast.application.ApplicationLevelExtension',
                                    method_name,
                                    parameter)
            
            if hasattr(parameter, 'kb'):
                parameter._run_amt_saver()
            
        except:
            logging.warning("plugin has encountered the following error : %s",
                            traceback.format_exc())
            setattr(plugin, '_has_warnings', True)
            
        _restore_execution_context(context)
        
        set_current_plugin(None)
            
        logging.info("Done running plugin %s.", plugin.get_name())

    
    setattr(parameter, '_current_phase', method_name)
    
    if method_name == 'end_application':
        # insert a new step for object creation just before the classical end_application
        
        setattr(parameter, '_current_phase', 'end_application_create_objects')
        
        # inserted here 
        logging.info('First pass for creating new objects : end_application_create_objects')
        for plugin in plugins:
            call(plugin, 'end_application_create_objects', parameter)
        
        # normal phase
        logging.info('Second pass end_application')
        setattr(parameter, '_current_phase', 'end_application')


    for plugin in plugins:
        call(plugin, method_name, parameter)

    setattr(parameter, '_current_phase', None)


def call_application_level_extensions(method_name, parameter):
    
    # recoded with previous one
    new_call_application_level_extensions(get_plugins, method_name, parameter)


def locate_plugins_folder(flat_path):
    """
    Determine the location of the folder containing plugins
    """
    # look into CastGlobalSettings.ini
    global_settings_path = os.path.join(flat_path, 'CastGlobalSettings.ini')
    
    try:
        global_settings = open(global_settings_path, 'r')
        strings = re.findall(r'^[ ]*CAST_PLUGINS_ROOT_PATH[ ]*=[ ]*([^\n]*)',
                             global_settings.read(),
                             re.MULTILINE)
        global_settings.close()

        if strings:
            return os.path.expandvars(strings[0])
    except:
        pass

    # default location depends on windows version
    path = os.environ['ALLUSERSPROFILE']
    
    win_version = StrictVersion(platform.version())
    
    if win_version >= StrictVersion('6.0.0'):
        path = os.path.join(path, 'CAST', 'CAST')
    else:
        path = os.path.join(path, 'Application Data', 'CAST', 'CAST')

    return os.path.join(path, 'Extensions')


def find_plugins(directory):
    """
    Find plugins from a folder containing plugins
    A plugin is a sub folder that contains python code + registrations of extensions
    """
    # reinitialise
    find_and_init_plugins(directory, glob.glob(directory + '/*'))


def find_and_init_plugins(directory, candidate_directories):

    global application_level_plugins
    application_level_plugins = []

    for d in candidate_directories:
        
        context = _get_execution_context()
        plugin = None
    
        for filepath in glob.glob(d + '/*.py'):
    
            temp = os.path.split(filepath)
            plugin_name = os.path.split(temp[0])[-1]
    
            module_name, _ = os.path.splitext(temp[-1])
            
            try:
                # current dir should be before other pathes
                sys.path.insert(0, os.path.join(directory, plugin_name))
                module = imp.load_source(module_name, filepath)
                
                for name in dir(module):
                    member = getattr(module, name)
                    if inspect.isclass(member) and member.__module__ != 'cast.application' and issubclass(member, cast.application.ApplicationLevelExtension):
                        if not plugin:
                            plugin_directory = temp[0]
                            plugin = cast.Plugin(plugin_directory)
                            application_level_plugins.append(plugin)
                        extension = member()
                        plugin.register_extension(extension)

                
            except Exception:
                print(traceback.format_exc())
                # may be normal because we also have python/C++ bindings
                # other way of avoiding it is to empty declare those bindings
                pass
            
        if plugin:
            plugin.__execution_context = _get_execution_context()
    
        _restore_execution_context(context)

def get_active_plugins(plugins_folder, ids_versions):
    """
    Return the plugin folders from a folder containing plugins and list of couple (id, version)
    """
    
    result = []
    
    if not ids_versions:
        return result
    
    to_be_found_plugins = list(ids_versions)
    
    for plugin_folder in glob.glob(plugins_folder + '/*'):

        plugin_id, plugin_version = cast.analysers.internal.plugin.get_plugin_id_and_version(plugin_folder)
        
        if not plugin_version:
            plugin_version = '(unversionned)'
        
        if (plugin_id, plugin_version) in ids_versions:
            result.append(plugin_folder)
            to_be_found_plugins.remove((plugin_id, plugin_version))
            logging.info("Registering Extension %s %s", plugin_id, plugin_version)

    # missing plugins : warn
    for (plugin_id, plugin_version) in to_be_found_plugins:
        logging.warning("Extension %s at version %s cannot be found on disk so it is desactivated. Please download it.", plugin_id, plugin_version)
            
    return result


def load_activated_plugins(kb):
    
    result = []
    metadata = kb.metadata
    sys_package_version = reflect_table("SYS_PACKAGE_VERSION", metadata, kb.engine)
    
    sel = select([sys_package_version.c.package_name, sys_package_version.c.version]).select_from(sys_package_version).where(sys_package_version.c.package_name.like('/%'))
    sel = sel.order_by(sys_package_version.c.package_name)
    
    for line in kb.engine.execute(sel):
        result.append((line[0][1:], line[1] if line[1] else None))
    
    return result
 

def find_cast_plugins(flat_path, kb):
    """
    Find the plugins given a flat path and a kb.
    """
    plugins_folder = locate_plugins_folder(flat_path)
    # select only those that are registered in sys_package_version
    ids_versions = load_activated_plugins(kb)
    folders = get_active_plugins(plugins_folder, ids_versions)

    find_and_init_plugins(plugins_folder, folders)


def _broadcast(extension, plugins, event, parameters):
    """
    broadcast
    """
    broadcast_name = ''
    current_plugin = None
    try:
        current_plugin =  extension.get_plugin()
        broadcast_name = current_plugin.get_name()
    except:
        pass

    _broadcast2(plugins, broadcast_name, event, parameters)
    cast.analysers.internal.set_current_plugin(current_plugin)


def _broadcast2(plugins, broadcasterName, eventName, parameter):
    '''Broadcast an event'''
    
    for plugin in plugins:
        
        context = _get_execution_context()
        
        try:
            _restore_execution_context(plugin.__execution_context)
#             logging.info("Running plugin %s...", plugin.get_name())
            plugin._call_broadcast(broadcasterName, eventName, parameter)
        except Exception:
            logging.warning("plugin %s has encountered the following error : %s",
                            plugin.get_name(),
                            traceback.format_exc())
            setattr(plugin, '_has_warnings', True)
                    
        _restore_execution_context(context)
#         logging.info("Done running plugin %s.", plugin.get_name())
    

