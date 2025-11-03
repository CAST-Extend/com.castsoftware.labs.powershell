"""
Handle extensibility at application level.
 
"""
import cast
from sqlalchemy import create_engine, MetaData, Table, Column, Sequence, Integer, \
                       String, select, text, TIMESTAMP, outerjoin, literal_column, union, \
                       delete, or_, and_, alias, inspect, join
from sqlalchemy.sql import func
from sqlalchemy.exc import NoSuchTableError
from collections import defaultdict
from datetime import date, datetime
from .internal.metamodel import MetaModel, Category, Type, Property, MetaModelConcepts
from .internal.amt_saver import Saver
from .internal.reflect import reflect_table
from .internal.test_api import create_link as create_test_link, add_link_position, \
                               create_object_with_parent as create_test_object, \
                               add_property as add_test_property
import subprocess
import tempfile, shutil
from sqlalchemy.schema import CreateSchema, DropSchema
import uuid
import sys
import traceback
import ssl
import pg8000
from .internal.p1 import get_message, set_message, Logger
from .internal.find_plugins import _broadcast

# not 'patchable' so import from 'real one'
from cast.application.internal.find_plugins import get_plugins

import cast.application.internal
import sqlparse
import urllib
import logging
import os
import collections
import re
import glob
import fileinput
import copy
from distutils.version import StrictVersion, LooseVersion
import pyodbc
from sqlalchemy.sql.expression import distinct
import xml.etree.ElementTree as eTree
import configparser


__version__ = '1.6.23'


class ApplicationLevelExtension(cast.Extension):
    """
    Inherit from this class to be consider as an application level extension.

    Usage :

    class MyExtension(ApplicationLevelExtension):

        def end_application(self, application):
            ...
    """

    def start_application(self, application):
        """
        Called before analysis.
        
        .. versionadded:: CAIP 8.3
        
        :type application: :class:`cast.application.Application`
        """
        pass

    def end_application_create_objects(self, application):
        """
        Called at the end of application's analysis, the first pass to create new objects.
    
        .. versionadded:: 1.6.0

        :type application: :class:`cast.application.Application`
        """
        pass
    
    def end_application(self, application):
        """
        Called at the end of application's analysis, the second pass to create new links.

        :type application: :class:`cast.application.Application`
        """
        pass
    
    def after_module(self, application):
        """
        Called after module content creation.
        
        .. versionadded:: CAIP 8.3
        
        :type application: :class:`cast.application.Application`
        """
        pass

    def after_snapshot(self, application):
        """
        Called after module content creation.
        Gives you the central's application.
        
        .. versionadded:: CAIP 8.3
        
        :type application: :class:`cast.application.central.Application`
        """
        pass
        
    def get_intermediate_files(self, name):
        """
        Return all the intermediate files of given name.
        The files are open in read mode.
        
        :rtype: list of read opened files
        """
        return [open(file_path, 'r') for file_path in self._get_intermediate_file_pathes(name)]
        
    def get_intermediate_file(self, name):
        """
        Return an intermediate file by name.
        The file is open in read mode.
        
        :rtype: fileinput.FileInput

        Raises an exception when the file does not exist.
        """
        return fileinput.input(files=self._get_intermediate_file_pathes(name))

    def _get_intermediate_file_pathes(self, name):
        application_intermediate = self.get_plugin().intermediate
        plugin_name = self.get_plugin().get_name()
        return glob.glob(application_intermediate + '/*/' + plugin_name + '/' + name)

    def broadcast(self, event, *parameters):
        """
        Send an event to other plugins
        
        .. versionadded:: 1.6.15        
        """
        _broadcast(self, get_plugins(), event, parameters)
        


class ConnectionSharing:
    
    
    connections = {}
    
    @staticmethod
    def get_connections(engine):
        """
        Connection sharing.
        """
        identity = str(engine)  
        
        try:
            return ConnectionSharing.connections[identity]
        except:
            
            result = (engine.connect(), engine.raw_connection())
            ConnectionSharing.connections[identity] = result
            # to reset cache on pg8000
            setattr(result[1], 'current_cast_schema', None)
            return result 

    _engines = {}

    @staticmethod
    def get_postgres_engine(user='operator',
                           password='CastAIP',
                           host='localhost',
                           port=2280,
                           database='postgres'):
        
        
        string = "postgresql+pg8000://%s:%s@%s:%d/%s" % (user, password, host, port, database)
        
        try:
            result = ConnectionSharing._engines[string]
            return result
            
        except:
            # optional ssl
            connect_args = get_ssl_connection_arguments(host, port)
            
            if connect_args:
                try:
                    engine = create_engine(string, connect_args=connect_args)
                    engine.connect()
                except:
                    # second try without certificate
                    try:
                        connect_args['ssl'].pop('ca_cert')
                    except KeyError:
                        pass
                    try:
                        connect_args['ssl'].pop('certfile')
                    except KeyError:
                        pass
                    try:
                        connect_args['ssl'].pop('keyfile')
                    except KeyError:
                        pass
                    engine = create_engine(string, connect_args=connect_args)
            else:
                engine = create_engine(string)
            ConnectionSharing._engines[string]= engine
            return engine
    
    @staticmethod
    def get_oracle_engine(user, password, host, port, sid, service):
        
        string = None
        
        if sid:
            string = "oracle+cx_oracle://%s:%s@%s:%d/%s" % (user, password, host, port, sid)
        else:
            string = "oracle+cx_oracle://%s:%s@(DESCRIPTION = (LOAD_BALANCE=on) (FAILOVER=ON) (ADDRESS = (PROTOCOL = TCP)(HOST = %s)(PORT = %d)) (CONNECT_DATA = (SERVER = DEDICATED) (SERVICE_NAME = %s)))" % (user, password, host, port, service)

        try:
            result = ConnectionSharing._engines[string]
            return result
            
        except:
            
            engine = create_engine(string)
            ConnectionSharing._engines[string]= engine
            return engine

    @staticmethod
    def get_sqlserver_engine(user, password, server, schema, port, instance, trusted=False):
        
        # somethiong that is enought to identify
        string = 'SQL Server %s, %s, %s, %s, %s, %s, %s' % (user, password, server, schema, port, instance, trusted)
        
        try:
            result = ConnectionSharing._engines[string]
            return result
            
        except:
            
            def connect():
                def try_connection(driver, user, password, server, schema, port, instance, trusted):
            
                    if port:
                        server += ',' + str(port)
                    elif instance:
                        server += '\\' + instance
                    """
                    server can be of the form : 
                    host,port
                    host\instance
                    @see 
                    - https://code.google.com/p/pyodbc/wiki/ConnectionStrings
                    - http://docs.sqlalchemy.org/en/rel_0_9/dialects/mssql.html#module-sqlalchemy.dialects.mssql.pyodbc
                    - http://stackoverflow.com/questions/25505081/python-pyodbc-how-to-connect-to-a-specific-instance
                    """
                    url = None
                    
                    url_string = 'DRIVER={%s};' % driver
                    if trusted:
                        url_string += 'Trusted_Connection=yes;'
                    else:
                        url_string += 'UID=%s;PWD=%s;' % (user, password)
                    
                    url_string += 'SERVER=%s;' % server
                    
                    # now optional
                    if schema:
                        url_string += 'DATABASE=%s;' % schema
                    
                    url_string += 'Mars_Connection=Yes'
                    
                    url = urllib.parse.quote_plus(url_string)
                    
                    try:
                        engine = create_engine("mssql+pyodbc:///?odbc_connect=" + url, case_sensitive=False)
                        engine.connect()
                        return engine
                    except:
                        pass
                    
                engine = try_connection('SQL Native Client', user, password, server, schema, port, instance, trusted)
                if engine:
                    return engine
                
                engine = try_connection('SQL Server Native Client 10.0', user, password, server, schema, port, instance, trusted)
                if engine:
                    return engine
                
                engine = try_connection('SQL Server Native Client 11.0', user, password, server, schema, port, instance, trusted)
                if engine:
                    return engine
                
                raise RuntimeError("Cannot find a driver to connect to SQLServer")
            
            engine = connect()
            ConnectionSharing._engines[string]= engine
            return engine
        
        
        
def create_postgres_engine(user='operator',
                           password='CastAIP',
                           host='localhost',
                           port=2280,
                           database='postgres'):
    
    return ConnectionSharing.get_postgres_engine(user, password, host, port, database)


def create_oracle_engine(user, password, host, port, sid, service):
    """
    sid or service name
    """
    return ConnectionSharing.get_oracle_engine(user, password, host, port, sid, service)


def create_sqlserver_engine(user, password, server, schema, port, instance, trusted=False):

    return ConnectionSharing.get_sqlserver_engine(user, password, server, schema, port, instance, trusted)


### begin...


def experimental(f):
    """
    Annotation for experimental functions.
    Use with care...
    """
    return f


def bitand(exp1, exp2, engine):
    
    if engine.dialect.name == 'oracle':
        return func.BITAND(exp1, exp2)
    else:
        return exp1.op('&')(exp2)


def invalidate_pg8000_cache(connection):
    
    if pg8000.__version__ == "1.10.1":
        # old version used before 8.3.23 (or 24)
        connection._caches.clear()
    elif pg8000.__version__ == "1.13.2":
#         print('invalidating cache')
        # see pg8000.core.handle_COMMAND_COMPLETE
        # see https://github.com/mfenniak/pg8000/commit/0ddbef586e7a8602616ac1596403dfa5382e786d
        for scache in connection._caches.values():
            for pcache in scache.values():
                for ps in pcache['ps'].values():
                    connection.close_prepared_statement(ps['statement_name_bin'])
                pcache['ps'].clear()


class CastSchema:
    """
    Common code.
    """
    def __init__(self, name, engine=None):
    
        self.engine = engine or create_postgres_engine()
        self.name = name
        
        _schema_name = name 
        if self.engine.dialect.name == 'mssql' and name:
            _schema_name = name + '.dbo'
        
        self.metadata = MetaData(bind=self.engine, schema=_schema_name)
        
        self.connection, self.raw_connection = ConnectionSharing.get_connections(self.engine)
        
        self._package_name = ""
    
    def create_cursor(self):
        cursor = self.raw_connection.cursor()
        if self.name:
            
            dialect = self.engine.dialect.name

            if dialect == 'postgresql':
                
                # lazy : for upgrade from old version where the field is not existent
                if not hasattr(self.raw_connection, 'current_cast_schema'):
                    setattr(self.raw_connection, 'current_cast_schema', None)
                
                # changing schema : invalidate cache
                # see https://github.com/mfenniak/pg8000/issues/136
                if self.raw_connection.current_cast_schema != self.name:
                    
                    invalidate_pg8000_cache(self.raw_connection)
                    self.raw_connection.current_cast_schema = self.name
                
                    
                cursor.execute("SET search_path TO %s" % self.name)
                
                # see https://github.com/mfenniak/pg8000/issues/46
                # assuming that in postgresql we are always utf8
                cursor.execute("SET CLIENT_ENCODING TO 'UTF8';")
                
            elif dialect == 'oracle':
                cursor.execute("ALTER SESSION SET CURRENT_SCHEMA = %s" % self.name)
            else:
                # SQL server
                cursor.execute("USE %s" % self.name)
                
        return cursor
    
    def get_caip_version(self):
        """
        Access to CAIP version of the schema.
        
        :return: distutils.version.StrictVersion
        """
        
        if hasattr(self, 'version'):
            return self.version
        
        if not hasattr(self, 'sys_package_version'):
            
            self.sys_package_version = reflect_table('SYS_PACKAGE_VERSION', self.metadata, self.engine)
        
        query = select([self.sys_package_version.c.version]).where(self.sys_package_version.c.package_name.in_(["APPW", 
                                                                                                                "PMC_MAIN",
                                                                                                                "ADG_CENTRAL"]))
        cursor = self._execute_sqlalchemyquery2(query)
        
        for line in cursor:
            # gives 7.3.6.1
            # remove the last .1
            elements = line[0].split('.')
            version_text = '.'.join(elements[0:3])
            self.version = None
            try:
                self.version = StrictVersion(version_text)
            except ValueError:
                pass
            return self.version
        
    def get_extensions(self):
        """
        Access to extensions installed on the schema.
        
        .. versionadded:: 1.5.4
        """
        
        if hasattr(self, 'extensions'):
            return self.extensions
        
        if not hasattr(self, 'sys_package_version'):
            
            self.sys_package_version = reflect_table('SYS_PACKAGE_VERSION', self.metadata, self.engine)
        
        query = select([self.sys_package_version.c.package_name, self.sys_package_version.c.version])
        cursor = self._execute_sqlalchemyquery2(query)

        self.extensions = []     
        for line in cursor:
            name = line[0]
            
            if name.startswith('/'):
                self.extensions.append((name[1:],line[1]))
        
        return self.extensions
    
    def get_size(self):
        """
        Get the schema size in bytes.
        """
        cursor = self.raw_connection.cursor()
        if self.name:
            
            dialect = self.engine.dialect.name

            if dialect == 'postgresql':
                cursor.execute("SELECT (sum(pg_relation_size(quote_ident(schemaname) || '.' || quote_ident(tablename)))::bigint) FROM pg_tables WHERE schemaname = '%s'" % self.name)
                for line in cursor:
                    return line[0]
        
        return -1
    
    class Event:
        
        def __init__(self, kb):
            self.kb = kb
            self.start_time = None
            self.end_time = None
            self.interrupted = False
    
    
    def get_install_events(self):
        """
        Access to install events of the schema.
        
        .. versionadded:: 1.5.4
        """
        
        class InstallVersion(CastSchema.Event):
            """
            Installation event
            """
            event_type = 'Install'

            def __init__(self, kb):
                CastSchema.Event.__init__(self, kb)
                self.version = None

            def __repr__(self):
                return 'Install version %s at %s ' % (self.version, self.start_time.strftime('%x %X'))
            
        class UpgradeVersion(CastSchema.Event):
            """
            Migration
            """
            event_type = 'Upgrade'
            
            def __init__(self, kb):
                CastSchema.Event.__init__(self, kb)
                self.from_version = None
                self.version = None
            
            def __repr__(self):
                return 'Upgrade from version %s to version %s at %s ' % (self.from_version, self.version, self.start_time.strftime('%x %X'))
        
        class InstallExtension(CastSchema.Event):
            """
            Installation event
            """
            event_type = 'Install Extension'

            def __init__(self, kb):
                CastSchema.Event.__init__(self, kb)
                self.extension = None
                self.version = None

            def __repr__(self):
                return 'Install Extension %s at version %s at %s ' % (self.extension, self.version, self.start_time.strftime('%x %X'))
        
        
        class UpgradeExtension(CastSchema.Event):
            """
            Installation event
            """
            event_type = 'Upgrade Extension'

            def __init__(self, kb):
                CastSchema.Event.__init__(self, kb)
                self.extension = None
                self.from_version = None
                self.version = None

            def __repr__(self):
                return 'Upgrade Extension %s from %s to %s at %s ' % (self.extension, self.from_version, self.version, self.start_time.strftime('%x %X'))

        class DowngradeExtension(CastSchema.Event):
            """
            Installation event
            """
            event_type = 'Downgrade Extension'

            def __init__(self, kb):
                CastSchema.Event.__init__(self, kb)
                self.extension = None
                self.from_version = None
                self.version = None

            def __repr__(self):
                return 'Downgrade Extension %s from %s to %s at %s ' % (self.extension, self.from_version, self.version, self.start_time.strftime('%x %X'))

        class UninstallExtension(CastSchema.Event):
            """
            Installation event
            """
            event_type = 'Uninstal Extension'

            def __init__(self, kb):
                CastSchema.Event.__init__(self, kb)
                self.extension = None
                self.from_version = None
                self.version = None

            def __repr__(self):
                return 'Uninstal Extension %s at %s ' % (self.extension, self.start_time.strftime('%x %X'))
        
        self._ensure_sys()
        
        # install
        install_events = []
        
        
        query = select([self.sys_package_history.c.package_name, self.sys_package_history.c.revision, self.sys_package_history.c.revision_date]).order_by(self.sys_package_history.c.revision_date)
        
        # the last installed/upgraded version
        current_version = None 
        
        extensions_current_version = {}
        
        for line in self._execute_sqlalchemyquery2(query):
            
            package_name = line[0]
            package_version = line[1]
            
            if package_name == self._package_name and package_version != '-1.-1.-1.-1':
                
                if not current_version:
                    
                    # fresh install
                    event = InstallVersion(kb=self)
                    event.version = package_version
                    event.start_time = line[2]
                    
                    install_events.append(event)
                    
                    current_version = package_version

                else:
                    
                    if package_version != current_version: 
                        """
                        not a refresh
                        """
                        event = UpgradeVersion(kb=self)
                        event.start_time = line[2]
                        event.from_version = current_version
                        event.version = package_version
                        install_events.append(event)
                        
                        current_version = package_version
            
            # @todo handle failed extension installed (have '-1.-1.-1.-1' as final version ...)
            if package_name.startswith('/') and package_version != '-1.-1.-1.-1':
                # extensions
                name = package_name[1:]
                
                if name in extensions_current_version:
                    
                    from_version = extensions_current_version[name]
                    
                    
                    if from_version != package_version:
                        event = None
                        try:
                            if package_version == 'Uninstall':
                                event = UninstallExtension(self)
                            elif LooseVersion(from_version) < LooseVersion(package_version):
                                event = UpgradeExtension(self)
                            else:
                                event = DowngradeExtension(self)
                                
                            event.start_time = line[2]
                            event.extension = name
                            event.version = package_version
                            event.from_version = from_version
                            
                            install_events.append(event)
                            
                            extensions_current_version[name] = package_version
                        except:
                            # @todo understand what is happening...
#                             print(traceback.format_exc())
                            print(name, from_version, package_version)
                else:
                    event = InstallExtension(kb=self)
                    event.start_time = line[2]
                    event.extension = name
                    event.version = package_version
                    
                    install_events.append(event)
                    
                    extensions_current_version[name] = package_version
        
        install_events.sort(key=lambda r: r.start_time)
            
        return install_events

    
    def execute_query(self, query):
        """
        Execute a query on the schema and return a cursor.
        
        .. versionadded:: 1.5.4
        """
        
        dialect = self.engine.dialect.name
        
        
        if dialect == 'postgresql':
            # see http://stackoverflow.com/questions/35135173/using-wildcard-with-pg8000
            query = query.replace('%', '%%') 
        
        cursor = self.create_cursor()
        try:
            cursor.execute(query)
        except:
            # handle sql errors
            self.raw_connection.rollback()
            raise
        
        return cursor
    
    def update_license_key(self, license_key):
        """
        Change the license key
        
        .. versionadded:: 1.6.21
        """
        sys_licenses = reflect_table("SYS_LICENSES", self.metadata, self.engine)
        query = sys_licenses.update().values(license_code=license_key)
        self.engine.execute(query)
            
    def _ensure_sys(self):
        
        if not hasattr(self, 'sys_package_version'):
            
            self.sys_package_version = reflect_table("SYS_PACKAGE_VERSION", self.metadata, self.engine)

        if not hasattr(self, 'sys_package_history'):
            
            self.sys_package_history = reflect_table("SYS_PACKAGE_HISTORY", self.metadata, self.engine)
    
    def _execute_sqlalchemyquery(self, query):
        """
        Execute a sqlalchemy query and return cursor
        
        @deprecated
        """
        cursor = self.create_cursor()
        try:
            cursor.execute(str(query.compile(compile_kwargs={"literal_binds": True})))
        except:
            # handle sql errors
            self.raw_connection.rollback()
            raise

        return cursor
    
    def _execute_sqlalchemyquery2(self, query):
        """
        Execute a sqlalchemy query and return a ResultProxy
        """
        try:
            return self.engine.execute(query)
        except:
            # handle sql errors
            self.raw_connection.rollback()
            raise
    
    def _execute_raw_query(self, cursor, query):
        
        # multi type : string, file, FileInput
        if type(query) is fileinput.FileInput:
            temp = ''.join(line for line in query)
            query = temp
        elif not type(query) is str:
            query = query.read()

        
        query = replace_special_variables(query)
        # split into several statements because dbapi generally can only
        # execute one statement at a time
        statements = sqlparse.split(query)

        for statement in statements:
            # may split with empty line...
            if statement:
                logging.debug('executing statement : raw  %s', statement)
                t = text(_remove_last_comma(statement))
                
                statement_string = str(t.compile(bind=self.connection))
                logging.debug('executing statement %s', statement_string)
                
                try:
                    cursor.execute(statement_string)
                    self.raw_connection.commit()
                except:
                    # handle sql errors
                    self.raw_connection.rollback()
                    raise

    def _execute_function(self, cursor, function_call, parameters=''):
        """
        parameters comma separated parameter without parenthesis
        """
        dialect = self.engine.dialect.name
        
        def add_parenthesis(parameters):
            return '(' + parameters + ')'
        
        if dialect == 'oracle':
            query = 'DECLARE error int;  begin error :=' + function_call + add_parenthesis(parameters) + '; end;'
            cursor.execute(query)
        elif dialect == 'postgresql':
            cursor.execute("SET search_path TO %s" % self.name)
            cursor.execute('select ' + function_call + add_parenthesis(parameters))
        elif dialect == 'mssql':
            cursor.execute('exec ' + function_call + ' ' + parameters)
            self.raw_connection.commit()


class KnowledgeBase(CastSchema):
    """
    A connection to a knowledge base.
    """
    def __init__(self, name, engine=None):
        """
        :param name: name of the local base, for example 'cre_cdms_local'
        :param engine: a connection to a server. by default, the connection used is css localhost:2280
        
        Any connection can be created by using one of :
        
        * :func:`cast.application.create_postgres_engine`
        * :func:`cast.application.create_oracle_engine`
        * :func:`cast.application.create_sqlserver_engine`
        """
        CastSchema.__init__(self, name, engine)
        self._package_name = "APPW"
        
        schema_exists = True
        
        try:
            

            if self.engine.dialect.name == 'mssql':
                
                self.Keys = reflect_table("Keys", self.metadata, self.engine)
            else:
                # usefull tables
                self.Keys = Table("keys",
                                  self.metadata,
                                  Column('idkey',
                                         Integer,
                                         Sequence('idkey_generator',
                                                  schema=name),
                                         primary_key=True),
                                  Column('objtyp', Integer),
                                  Column('keynam', String(255)),
                                  Column('keytyp', String(6)),
                                  Column('keysubtyp', Integer),
                                  Column('keyclass', Integer),
                                  Column('keyprop', Integer),
                                  Column('idusrdevpro', String(3)),
                                  Column('keydevdat', TIMESTAMP),
                                  implicit_returning=False,
                                  autoload=True,
                                  autoload_with=self.engine)
        
        except NoSuchTableError:
            schema_exists = False 
            
        if not schema_exists:            
            raise RuntimeError("knowledge base '%s' does not exist" % name) 
            
        self.ObjPro = reflect_table("ObjPro", self.metadata, self.engine)
        
        self.ObjFulNam = reflect_table("ObjFulNam", self.metadata, self.engine)
                               
        
        self.RefPath = reflect_table("RefPath", self.metadata, self.engine)
        
        self.ObjFilRef = reflect_table("ObjFilRef", self.metadata, self.engine)
        
        # corrects here : works for 7.3
        # for 8.0 call _additional_init()
        self.ObjPos = reflect_table("ObjPos", self.metadata, self.engine)
        
        self.KeyPar = reflect_table("KeyPar", self.metadata, self.engine)

        self.metamodel = None
        # interesting pointers
        self.project_category = None
        self.database_subset_category = None

        # metamodel caching
        self._load_metamodel()
        # usefull constants
        self.project_category = self.metamodel.get_category(id=1013)
        self.database_subset_category = self.metamodel.get_category(id=140351)
        self.user_project_category = self.metamodel.get_category(id=669)
        self.shell_category = self.metamodel.get_category(id=1014)
        self.directory_category = self.metamodel.get_category(id=5039)
        
        self.__init_database_related_informations__()

        # only in version >= 7.3
        self.plugin_project_type = None
        try:
            self.plugin_project_type = self.metamodel.get_category(id=141887)
        except:
            pass

        self.identification_name = self.metamodel.get_property(id=3)
        self.identification_fullname = self.metamodel.get_property(id=125)
        self.projectRelationKind = self.metamodel.get_property(id=1055)
        self.dependencyKind = self.metamodel.get_property(id=1058)
        
        if self.engine.dialect.name == 'oracle':
            cursor = self.create_cursor()
            self._execute_function(cursor, 'USER_INFO.init_internal_values', "-1, '%s'" % self.engine.url.username)
            self.raw_connection.commit()

        # Do not modify that constructor by adding table bindings

    def __init_database_related_informations__(self):
        #
        # compatible with CAST versions >= 7.0
        #
        try:
            self.rootContainer_category = self.metamodel.get_category(id=141169)  # CAST_SQL_RootContainer
        except:
            try:
                self.rootContainer_category = self.metamodel.get_category(id=278)  # DATABASE
            except:
                pass

        try:
            self.instanceContainer_category = self.metamodel.get_category(id=138012)  # CAST_Oracle_Instance or CAST_SQL_Instance (legacy)
        except:
            pass
        try:
            self.ownerContainer_category = self.metamodel.get_category(id=141170)  # CAST_SQL_OwnerContainer
        except:
            try:
                self.ownerContainer_category = self.metamodel.get_category(id=17)  # SQL_SCHEMA
            except:
                pass
        try:
            self.ownerContainer2_category = self.metamodel.get_category(id=138014)  # CAST_Oracle_Schema or CAST_SQL_Schema (legacy)
        except:
            self.ownerContainer2_category = None

    def get_applications(self):
        """
        Returns the list of application of the knowledge base.
        
        :rtype: list of :class:`cast.application.Application`
        
        """
        usrpro = reflect_table('UsrPro', self.metadata, self.engine)
        cursor = self._execute_sqlalchemyquery2(select([usrpro.c.idusrpro]))
        applications = [self._load_object(x[0]) for x in cursor]

        # skipp KB Information Finalization because not an application
        return [app for app in applications if app and app.get_name() != 'KB Information Finalization']

    def get_application(self, name):
        """
        Access to an application by name.
        
        :param str name: the name of the application

        :rtype: :class:`cast.application.Application`
        """
        for app in self.get_applications():
            if app.get_name() == name:
                return app
            
        return None


    def get_jobs(self):
        """
        Access to jobs of the knowledge base.
        """
        if not hasattr(self, '_jobs'):
            
            cursor = self.create_cursor()
            cursor.execute("select IdJob from UsrProJob")
            setattr(self, '_jobs', [self._load_object(x[0]) for x in cursor])
            cursor.close()
                
        return self._jobs

    
    def get_events(self):
        """
        Get the events of this KnowledgeBase.
        
        - AMT Saving
        - Metrics Calculation (after the analysis)
        - Update Cast Knowledge Base
        - Installation, upgrade events 
        - ...
        
        .. versionadded:: 1.5.4
        
        """
#         @todo: 
#         
#         - RunLinker:
#           - ' start LINK_ResolvePrototypes'
#           - 'end LINK_ResolvePrototypes'
#         - 'Start D_SupKeys'/'End D_SupKeys'

# in 7.3, 8.2
# "start CACHE_PROCESSID 5983037452" // job id = 5983037 application = 452
# "end CACHE_PROCESSID 5983037452"
# "start CACHE_FLUSHDATA 5983037"
# "end CACHE_FLUSHDATA 5983037"
# "Start FINAL_JOBANA 5983037"
# "END FINAL_JOBANA 5983037"



# in 8.3 ??
# "START CACHE_INIT13741286","2019-10-01 16:26:18.999366",530946 // begin of analysis job id =13741286
# "END CACHE_INIT13741286","2019-10-01 16:26:19.001978",530947
# "START CACHE_PROCESSID 13741286452","2019-10-01 23:36:57.876335",530948 // begin of analysis job id = 13741286 application = 452
# ...
# "END FINAL_JOBANA 13741286","2019-10-01 23:44:56.341288",531224

# KB Update

# "Start CI_INIT_DATA ","2019-10-01 23:57:39.581703",531249
# ...
# "START CACHE_INIT16292801","2019-10-01 23:58:34.533789",531252
# ...
# "END CACHE_FLUSHDATA 16292801","2019-10-01 23:58:47.376156",531304
        
        # load once
        applications = self.get_applications()        
        
        class AMTSaving(CastSchema.Event):
            """
            Event of Saving a job.
            """
            event_type = 'AMT Saving'
                
            def __init__(self, kb):
                CastSchema.Event.__init__(self, kb)

                # those may not exist anymore...
                self.job_id = None
                self.application_id = None

            def get_application(self):
                """
                The application on which the saving was done.
                """
                for app in applications:
                    if app.id == self.application_id:
                        return app
                
                class DeletedApplication:
                    
                    def __init__(self, identifier):
                        self.identifier = identifier
                    
                    def __repr__(self):
                        return 'Deleted Application(id=%s)' % self.identifier
                
                return DeletedApplication(self.application_id)

            def get_job(self):
                """
                Get the job, if still exists
                """
                if not self.job_id:
                    return None
                
                jobs = self.kb.get_jobs()
                for job in jobs:
                    if job.id == self.job_id:
                        return job
                

                class DeletedJob:
                    
                    def __init__(self, identifier):
                        self.identifier = identifier
                    
                    def __repr__(self):
                        return 'Deleted Job(id=%s)' % self.identifier
                
                return DeletedJob(self.job_id)

            def __repr__(self):
                
                if self.interrupted:
                    
                    return 'Interrupted AMT Saving %s --> ? (application : %s; job : %s)' % (self.start_time.strftime('%x %X'), self.get_application(), self.get_job())
                
                return 'AMT Saving %s --> %s (application : %s; job : %s)' %(self.start_time.strftime('%x %X'), self.end_time.strftime('%x %X'), self.get_application(), self.get_job())

        class KBUpdate(CastSchema.Event):
            """
            Event of Saving a job.
            """
            event_type = 'KB Update'
                
            def __init__(self, kb):
                CastSchema.Event.__init__(self, kb)

                # those may not exist anymore...
                self.job_id = None

            def get_job(self):
                """
                Get the job, if still exists
                """
                if not self.job_id:
                    return None
                
                jobs = self.kb.get_jobs()
                for job in jobs:
                    if job.id == self.job_id:
                        return job
                

                class DeletedJob:
                    
                    def __init__(self, identifier):
                        self.identifier = identifier
                    
                    def __repr__(self):
                        return 'Deleted Job(id=%s)' % self.identifier
                
                return DeletedJob(self.job_id)

            def __repr__(self):
                
                if self.interrupted:
                    
                    return 'Interrupted KB Update %s --> ? (job : %s)' % (self.start_time.strftime('%x %X'), self.get_job())
                
                return 'KB Update %s --> %s (job : %s)' %(self.start_time.strftime('%x %X'), self.end_time.strftime('%x %X'), self.get_job())

        class Snapshot(CastSchema.Event):
            """
            Event of Metrics Calculation.
            """
            event_type = 'MetricsCalculation'

            def __init__(self, kb):
                CastSchema.Event.__init__(self, kb)

            def __repr__(self):
                
                return ('Interrupted ' if self.interrupted else '') + 'Metrics Calculation %s --> %s' %(self.start_time.strftime('%x %X') if self.start_time else '?', 
                                                                                                        self.end_time.strftime('%x %X') if self.end_time else '?')
        
        
        self._ensure_additional_tables()
        
        query = select([self.dss_history.c.description, 
                        self.dss_history.c.history_id, 
                        self.dss_history.c.action_date]).order_by(self.dss_history.c.history_id)
        
        events = []
        
        current_job = None
        
        current_snapshot = None
        
        temp = None
        
        for line in self._execute_sqlalchemyquery2(query):
            
            description = line[0].upper()
            if description.startswith('START CACHE_PROCESSID'):
                
                # handle interruption
                if current_job:
                    current_job.interrupted = True
                if current_snapshot:
                    current_snapshot.interrupted = True
                
                
                current_job = AMTSaving(kb=self)
                current_job.start_time = line[2]
                temp = description[22:]
                
                events.append(current_job)
                
#                 print(line) 
#                 print(description, temp)
#                 print(current_job.start_time.strftime('%x %X'))
            
            elif description.startswith('START CACHE_FLUSHDATA'):
                "start CACHE_FLUSHDATA 352"
                'END FINAL_JOBANA'
                if current_job:
                    
                    current_job.job_id = description[22:]
                    current_job.application_id = int(temp[len(current_job.job_id):])
                    current_job.job_id = int(current_job.job_id)
            elif description.startswith('START AMT_P_BUILD'):
                "START AMT_P_BUILD13741287"
                if current_job:
                    
                    current_job.job_id = description[17:]
#                     print(current_job.job_id)
                    current_job.application_id = int(temp[len(current_job.job_id):])
                    current_job.job_id = int(current_job.job_id)
                                   
            elif description.startswith('END CACHE_PROCESSID'):
                
                if current_job:
#                     current_job.job_id = description[17:]
                    current_job.end_time = line[2]
#                     current_job.application_id = int(temp[len(current_job.job_id):])
#                     current_job.job_id = int(current_job.job_id)
                
                
#                 print(line)
#                 print(current_job.job_id, current_job.application_id, current_job.end_time.strftime('%x %X'))
                
#                 print(current_job)
                current_job = None
            elif description.startswith('START CI_CHECK_DATA'):
                
                # handle interruption
                if current_job:
                    current_job.interrupted = True
                if current_snapshot:
                    current_snapshot.interrupted = True
                                
                current_job = KBUpdate(kb=self)
                current_job.start_time = line[2]
                
                events.append(current_job)
                
            elif description.startswith('START CACHE_INIT'):
            # START CACHE_INIT16292901
                if current_job:
                    
                    current_job.job_id = description[16:]
                    current_job.job_id = int(current_job.job_id)
                    
            elif description.startswith('END CI_CHECK_DATA'):
                # "end CI_CHECK_DATA"
                if current_job:
                    current_job.end_time = line[2]
                current_job = None
                
            if description.startswith('START LOCAL SNAPSHOT'):
                
                current_snapshot = Snapshot(kb=self)
                current_snapshot.start_time = line[2]
                
                events.append(current_snapshot)
#                 print(line)
            elif description.startswith('END   LOCAL SNAPSHOT'):

                current_snapshot.end_time = line[2]
#                 print(line)
                
#                 print(current_snapshot)
                current_snapshot = None
            

        # install
        install_events = self.get_install_events()

        # merge both events types
        result = events + install_events
        result.sort(key=lambda r: r.start_time)
            
        return result

    def update_cast_system_views(self):
        """
        Updates the Cast System Views.
        """
        
        if self.get_caip_version() >= StrictVersion("8.3.10"):
            # already done by the platform itself : nothing should be done (would crush results)
            return
        
        cursor = self.create_cursor()
        
        # execute init

        """        
        LPSTR szCreateTempTable2 = "create table #CSV_INFO (IdKey int null, Mangling varchar(1000) null , Info varchar(1000) null) %s";
        LPSTR szCreateIdxTempTable2 = "create index IdxTemp2 on #CSV_INFO (IdKey)";
        """        
        
        if self.engine.dialect.name == 'mssql':
            
            try:
                cursor.execute('create table #CSV_INFO (IdKey int null, Mangling varchar(1000) null , Info varchar(1000) null)')
                cursor.execute('create index IdxTemp2 on #CSV_INFO (IdKey)')
            except pyodbc.ProgrammingError:
                pass # table already exist, for example in case of several calls to update_cast_system_views
                
            
        self._execute_function(cursor, 'CSV_INIT')
        self._execute_function(cursor, 'CSV_GENERATE_INFO')


    def _build_object_wrapper(self, identifier, idtype, name, additional_values=None):
        """
        Correctly subclass Object according to object type
        """
        typ = self.metamodel.get_category(id=idtype)
        
        import cast.application # sic
        
        if typ == self.user_project_category:
            return Application(self, identifier, name, typ)
    
        
        # cached types lists
        if not hasattr(self, 'cache_database_subset_types'):
            setattr(self, 'cache_database_subset_types', set(self.database_subset_category.get_sub_types()))
            setattr(self, 'cache_project_types', set(self.project_category.get_sub_types()))
            
            setattr(self, 
                    'cache_shell_types', 
                    set(self.shell_category.get_sub_types() | self.metamodel.get_category('APM Inventory Files').get_sub_types()))
            
            setattr(self, 'cache_rootContainer_types', set(self.rootContainer_category.get_sub_types()))
            setattr(self, 'cache_instanceContainer_types', set(self.instanceContainer_category.get_sub_types()))
            setattr(self, 'cache_ownerContainer_types', set(self.ownerContainer_category.get_sub_types()))
            setattr(self, 'cache_ownerContainer2_types', set(self.ownerContainer2_category.get_sub_types()))
        
        if typ in self.cache_database_subset_types:
            return cast.application.DatabaseSubset(self, identifier, name, typ)

        if typ in self.cache_project_types or typ.name == 'VB_PROJECT_GROUP':
            return cast.application.Project(self, identifier, name, typ, additional_values)

        try:
                
            if typ in self.cache_rootContainer_types:
                return cast.application.Database(self, identifier, name, typ, additional_values)
        except:
            pass

        try:

            if typ in self.cache_instanceContainer_types:
                return cast.application.Database(self, identifier, name, typ, additional_values)
        except:
            pass

        try:
            if typ in self.cache_ownerContainer_types:
                return cast.application.DatabaseOwner(self, identifier, name, typ, additional_values)
            else:
                try:
                    if typ in self.cache_ownerContainer2_types:
                        return cast.application.DatabaseOwner(self, identifier, name, typ, additional_values)
                except:
                    pass
        except:

            if typ in self.cache_ownerContainer2_types:
                return cast.application.DatabaseOwner(self, identifier, name, typ, additional_values)
        
        # UDBDATABASE
        if idtype == 313:
            return cast.application.Database(self, identifier, name, typ, additional_values)
        
        # UDBSCHEMA
        if idtype == 301:
            return cast.application.DatabaseOwner(self, identifier, name, typ, additional_values)
        
        if typ in self.cache_shell_types or idtype == 512:
            return cast.application.File(self, identifier, name, typ, additional_values)
        
        return cast.application.Object(self, identifier, name, typ, additional_values)

    def _load_object(self, identifier):
        """
        Load one object.
        """
        cursor = self.create_cursor()
        cursor.execute("select KeyNam,ObjTyp from Keys where IdKey = %s" % identifier)
        
        line = cursor.fetchone()
        
        self.raw_connection.commit()
        cursor.close()
        
        if line:
            obj_name = line[0]
            obj_type = line[1]
            
            return self._build_object_wrapper(identifier, obj_type, obj_name)
        
    def _load_metamodel(self):
        """
        Load the metamodel.
        
        We should not modify this method as metamodel is loaded before 
        api upgrade.
        """
        mm = MetaModel()
        
        # types
        cursor = self.create_cursor()
        cursor.execute("select IdTyp,TypNam,TypDsc from Typ")
        
        for mm_type in cursor:
            result = Type()
            result.id = mm_type[0]
            result.name = mm_type[1]
            result.description = mm_type[2]
            mm._add_type(result)
        cursor.close()
        
        # categories inheritance
        cursor = self.create_cursor()
        cursor.execute("select IdCat,CatNam,CatDsc from Cat")

        for mm_category in cursor:
            result = Category()
            result.id = mm_category[0]
            result.name = mm_category[1]
            result.description = mm_category[2]
            mm._add_category(result)
        cursor.close()

        # type inheritance
        # transitive inheritance 
        cursor = self.create_cursor()
        cursor.execute("select IdTyp,IdCatParent from TypCat")

        for inheritance in cursor:

            idtyp = inheritance[0]
            idcat = inheritance[1]
             
            typ = mm.get_category(id=idtyp)
            if typ:
                cat = mm.get_category(id=idcat)
                typ.all_inherited_categories.add(cat)
                cat.sub_categories.add(typ)
                cat.sub_types.add(typ)
        cursor.close()

        # category inheritance
        # only direct inheritance here
        cursor = self.create_cursor()
        cursor.execute("select IdCat,IdCatParent from CatCat")

        for inheritance in cursor:

            idtyp = inheritance[0]
            idcat = inheritance[1]

            typ = mm.get_category(id=idtyp)
            if typ:
                cat = mm.get_category(id=idcat)
                typ.all_inherited_categories.add(cat)
                typ.inherited_categories.add(cat)
                cat.sub_categories.add(typ)
        cursor.close()

        # properties
        cursor = self.create_cursor()
        cursor.execute("select IdProp,PropNam,PropTyp,CardMin,CardMax from Prop")
        for prop in cursor:

            result = Property()
            result.id = prop[0]

            # the small name in fact
            result.name = prop[1]

            predefined_type_names = {137475: 'integer',
                                     137476: 'string',
                                     137477: 'bookmark',
                                     137478: 'dateTime',
                                     1028: 'reference'}

            proptyp = prop[2]
            if proptyp in predefined_type_names:
                result.type = predefined_type_names[proptyp]
            else:
                # id of a category
                result.type = mm.get_category(id=proptyp)

            result.minimal_cardinality = prop[3]
            result.maximal_cardinality = prop[4]

            mm._add_property(result)
        cursor.close()

        mm.properties_by_name = {}
        # properties of types and categories
        cursor = self.create_cursor()
        cursor.execute("select IdTyp,IdProp from TypProp union select IdCat,IdProp from PropCat")
        for prop in cursor:
            idtyp = prop[0]
            idprop = prop[1]
            typ = mm.get_category(id=idtyp)
            p = mm.get_property(id=idprop)

            # reindex
            p.name = typ.name + '.' + p.name
            mm.properties_by_name[p.name] = p

            typ.properties.add(p)
        
        self.raw_connection.commit()
        
        cursor.close()
        self.metamodel = mm

    # last parameter is to enable TSQL legacy where project is database
    def _get_object_query(self, project_ids, internal=True, external=False, exclude_project=True):
        """
        Build a query that returns the objects of projects
        """
        is_in_project = self._get_project_filter(project_ids, internal, external, exclude_project)        
        query = self._get_select_object()
        
        # objects of projects
        query = query.where(self.Keys.c.idkey.in_(is_in_project))
        # but not the project themselves
        if exclude_project:
            query = query.where(~self.Keys.c.idkey.in_(project_ids))
        
        return query

    def _get_project_filter(self, project_ids, internal=True, external=False, exclude_project=True):
        """
        Get a filter for the projects.
        
        :param project_ids: list of id or application
        """
        # will now stand TONS OF PROJECTS
        is_in_project = select([self.ObjPro.c.idobj]).where(self.ObjPro.c.idpro.in_(_get_in_project(project_ids)))

        if internal and not external:
            is_in_project = is_in_project.where(self.ObjPro.c.prop == 0)
        elif not internal and external:
            # external objects : all props != 0
            # not efficient
            is_in_project = is_in_project.where(~self.ObjPro.c.idobj.in_(is_in_project.where(self.ObjPro.c.prop == 0)))
        
        return is_in_project
        
    def _get_select_object(self):
        """
        Return a query that select the correct columns.
        """
        key_fullname = outerjoin(self.Keys, self.ObjFulNam, self.Keys.c.idkey == self.ObjFulNam.c.idobj) 
        query = select([self.Keys.c.idkey, self.Keys.c.objtyp, self.Keys.c.keynam, self.ObjFulNam.c.fullname]).select_from(key_fullname).order_by(self.Keys.c.idkey)
        
        return query

    def _execute_query(self, query, application=None):
        """
        Execute a query.
        """
        cursor = self._execute_sqlalchemyquery2(query)
        return (self._build_object_wrapper(o[0], o[1], o[2], {'application':application, 'fullname':o[3]}) for o in cursor)

    def _get_objects(self, project_ids, internal=True, external=False, application=None):
        """
        Get all the objects of a set of projects
        """

        objects_of_projects = self._get_object_query(project_ids, internal, external)
        return self._execute_query(objects_of_projects, application)

    def _get_objects_by_name(self, project_ids, name, internal=True, external=False, application=None):
        """
        Get all the objects of projects with given name
        """

        objects_of_projects = self._get_object_query(project_ids, internal, external)
        query = objects_of_projects.where(self.Keys.c.keynam == name)
        return self._execute_query(query, application)

    def _search_objects(self, project_ids, name=None, category=None, application=None, parent_object=None, exclude_project=True, load_properties=False):
        """
        Search all the objects of projects by name and or by type. 
        If load_properties is true, will load the object properties too.
        """
        self._load_infsub_types()
        
        query = None
        if not load_properties:
            query = self._get_object_query(project_ids, True, False, exclude_project)
        else:
            
            objdsc = reflect_table("ObjDsc", self.metadata, self.engine)
            
            objinf = reflect_table("ObjInf", self.metadata, self.engine)
    
            """
            @todo : 
            - ordnum for multivalues
            - blkno for multi lines strings...
            """
            
            select_dsc = select([objdsc.c.idobj, objdsc.c.inftyp, objdsc.c.infsubtyp, objdsc.c.infval.label('string_value'), literal_column('null').label('int_value'), objdsc.c.blkno])
            select_inf = select([objinf.c.idobj, objinf.c.inftyp, objinf.c.infsubtyp, literal_column('null'), objinf.c.infval, objinf.c.blkno])
            
            properties = union(select_dsc, select_inf).alias('properties')
            j = outerjoin(self.Keys, self.ObjFulNam, self.Keys.c.idkey == self.ObjFulNam.c.idobj) 
            myjoin = outerjoin(j, properties, self.Keys.c.idkey == properties.c.idobj) 
            
            # @todo : will not stand TONS OF PROJECTS
            is_in_project = select([self.ObjPro.c.idobj]).where(self.ObjPro.c.idpro.in_(project_ids))
            is_in_project = is_in_project.where(self.ObjPro.c.prop == 0)
    
            query = select([self.Keys.c.idkey, self.Keys.c.objtyp, self.Keys.c.keynam, self.ObjFulNam.c.fullname, properties]).select_from(myjoin)
            # objects of projects
            query = query.where(self.Keys.c.idkey.in_(is_in_project))
            # but not the project themselves
            query = query.where(~self.Keys.c.idkey.in_(project_ids))
    
            query = query.order_by(self.Keys.c.idkey, properties.c.inftyp, properties.c.infsubtyp)
    
        if name:
            query = query.where(self.Keys.c.keynam == name)
    
        if category:
            types = self.metamodel.get_category(name=category).get_sub_types()
            type_ids = [t.id for t in types]
            query = query.where(self.Keys.c.objtyp.in_(type_ids))
        
        if parent_object:
            is_child = select([self.KeyPar.c.idkey]).where(self.KeyPar.c.idparent == parent_object.id)
            query = query.where(self.Keys.c.idkey.in_(is_child))
        
        if not load_properties:
            
            for o in self._execute_query(query, application):
                yield o
            
        else:
            cursor = self._execute_sqlalchemyquery2(query)
            
            current_object = None
            for line in cursor:
                current_object_id = current_object.id if current_object else None
                object_id = line[0]
    
                # true when we have changed object
                is_new_object_line = object_id != current_object_id
                 
                if is_new_object_line:
                    # create object
                    old_object = current_object
                    current_object = self._build_object_wrapper(line[0], line[1], line[2], {'application':application, 'fullname':line[3]})
                     
                # add property to current object
                inftyp = line[5]
                infsubtyp = line[6]
                prop = self._search_property(inftyp, infsubtyp)
                if prop:
                    string_value = line[7]
                    int_value = line[8]
                    value = int_value if not int_value is None else string_value
                    current_object._add_property_value(prop, value)
                else:
                    # object has no property at all : still put it empty
                    if not hasattr(current_object, '_properties'):
                        setattr(current_object, '_properties', {})
                
                if is_new_object_line and old_object:
                    yield old_object
            
            if current_object:
                yield current_object

    def _get_files(self, project_ids, languages=[], application=None, external=False):
        """
        Get all the files of a project.

        @param languages: a list of categories that filter the file types
        """
        
        # basic query
        query = select([self.Keys.c.idkey,
                        self.Keys.c.objtyp,
                        self.Keys.c.keynam,
                        self.RefPath.c.path,
                        self.ObjFulNam.c.fullname]).select_from(

                        self.Keys.join(self.ObjFilRef,
                                       self.ObjFilRef.c.idobj == self.Keys.c.idkey, 
                                       isouter=True).join(self.RefPath,
                                                          self.RefPath.c.idfilref == self.ObjFilRef.c.idfilref, 
                                                          isouter=True).join(self.ObjFulNam, 
                                                                             self.ObjFulNam.c.idobj == self.Keys.c.idkey, 
                                                                             isouter=True))

        # filter on projects
        # @todo : will not stand TONS OF PROJECTS
        is_in_project = select([self.ObjPro.c.idobj]).where(self.ObjPro.c.idpro.in_(project_ids))
        
        # internal only
        if not external:
            is_in_project = is_in_project.where(self.ObjPro.c.prop == 0)

        query = query.where(self.Keys.c.idkey.in_(is_in_project))

        # filter on types
        # cache it ???
        persistents = self.metamodel.get_category(id=1023).get_sub_types()
        directories = self.directory_category.get_sub_types()
        apm_inventory_files = self.metamodel.get_category('APM Inventory Files').get_sub_types()
        projects = self.project_category.get_sub_types()
        
        # all persistent types not directories inheriting from either shell or APM Inventory Files
        types = (self.shell_category.get_sub_types() | apm_inventory_files) & persistents - directories - projects

        type_ids = [t.id for t in types if not t.inherit_from(self.directory_category) and t.inherit_from_one_of(languages)]

        query = query.where(self.Keys.c.objtyp.in_(type_ids))

#         print(query.compile(compile_kwargs={"literal_binds": True}))

        # execute and pass additional param
        cursor = self._execute_sqlalchemyquery2(query)

        return (self._build_object_wrapper(o[0], 
                                           o[1], 
                                           o[2], 
                                           {'path': o[3], 
                                            'application':application, 
                                            'fullname':o[4]}) for o in cursor)

    def _check_sub_object(self, f, line):
        """
        Perform checks to determine if the line from a query represent 
        an new object or not
        """
        if f.id == line[0]:
            # this position is for the file
            if not f.positions:
                f.positions = []
            f.positions.append(Bookmark(f,
                                        line[3],
                                        line[4],
                                        line[5],
                                        line[6]))

            return False
        else:
            
            o = f._get_sub_object_by_id(line[0])
            
            if o:
                if not o.positions:
                    o.positions = []
                o.positions.append(Bookmark(f,
                                            line[3],
                                            line[4],
                                            line[5],
                                            line[6]
                                            ))
    
                return False
                
            return True

    def _load_objects(self, f):
        """
        loads the sub objects of a file.

        First try with objpos

        Will not work for synthetised sub objects, but we do not care for now
        """
        query = select([self.Keys.c.idkey,
                        self.Keys.c.objtyp,
                        self.Keys.c.keynam,
                        self.ObjPos.c.info1,
                        self.ObjPos.c.info2,
                        self.ObjPos.c.info3,
                        self.ObjPos.c.info4,
                        self.ObjFulNam.c.fullname
                        ]).select_from(self.Keys.join(self.ObjPos,
                                                      self.ObjPos.c.idobj == self.Keys.c.idkey).join(self.ObjFulNam, 
                                                                                                     self.ObjFulNam.c.idobj == self.Keys.c.idkey,
                                                                                                     isouter=True))
        query = query.where(self.ObjPos.c.idobjref == f.id)

        cursor = self._execute_sqlalchemyquery2(query)
        
        return (self._build_object_wrapper(o[0], o[1], o[2], {'begin_line': o[3],
                                                              'begin_column': o[4],
                                                              'end_line': o[5],
                                                              'end_column': o[6],
                                                              'file': f,
                                                              'application': f.application,
                                                              'fullname':o[7]})
                for o in cursor if self._check_sub_object(f, o))


        
        
    def _search_property(self, inftyp, infsubtyp):
        """
        Get a property per inftyp/infsubtyp 
        """
        
        m = getattr(self.metamodel, 'prop_per_inftyp')
        
        try:
            return self.metamodel.get_property(id=m[inftyp][infsubtyp])
        except:
            return None
    
    # # patch for KnowledgeBase type
    def _load_infsub_types(self):
        """
        loads the inftyp/infsubtyp for properties
        """
        if not hasattr(self.metamodel, 'prop_per_inftyp'):
            
            result = {}
            
            cursor = self.create_cursor()
            cursor.execute("select IdProp, AttrNam, IntVal from PropAttr where AttrNam = 'INF_TYPE' or  AttrNam = 'INF_SUB_TYPE' order by IdProp, AttrNam")
    
            inf_typ = None
            inf_subtyp = None
    
            for line in cursor:
                
                if line[1] == 'INF_TYPE':
                    inf_typ = line[2]
                    
                    # second line so we can register mapping
                    if not inf_typ in result:
                        result[inf_typ] = {}
                    
                    result[inf_typ][inf_subtyp] = line[0]
                    
                    try:
                        p = self.metamodel.get_property(id=line[0])
                        setattr(p,'inftyp',inf_typ)
                        setattr(p,'infsubtyp',inf_subtyp)
                    except:
                        pass
                    
                else:
                    inf_subtyp = line[2]
            
            
            setattr(self.metamodel, 'prop_per_inftyp', result)
            
            self.raw_connection.commit()
            cursor.close()

    # # patch for KnowledgeBase type
    def _fully_load_properties(self):
        """
        Loads the descriptions for properties + attributes
        """
        if not hasattr(self.metamodel, 'fully_load_properties'):
            
            cursor = self.create_cursor()
            cursor.execute("select IdProp, AttrNam, IntVal, StrVal from PropAttr")

            for line in cursor:
            
                try:
                    p = self.metamodel.get_property(id=line[0])
                    value = None
                    if line[2]:
                        value = line[2]
                    else:
                        value = line[3]
                    p.attributes[line[1]] = value 
                except:
                    pass
            
            cursor.execute("select IdProp, PropDsc from Prop")

            for line in cursor:
            
                try:
                    p = self.metamodel.get_property(id=line[0])
                    p.description = line[1]
                except:
                    pass
            
            cursor.execute("select idcat, attrnam, attrtyp, intval, strval, status from CatAttr")
            for line in cursor:
                
                if line[5] == 'INACTIVE':
                    continue
            
                try:
                    p = self.metamodel.get_category(id=line[0])
                    attribute_name = line[1]
                    if line[2] == 137476:
                        attribute_value = line[4]
                    else:
                        attribute_value = line[3]
                    p.attributes[attribute_name] = attribute_value
                except:
                    pass

            
            cursor.execute("select idtyp, attrnam, attrtyp, intval, strval, status from TypAttr")
            for line in cursor:
            
                if line[5] == 'INACTIVE':
                    continue
            
                try:
                    p = self.metamodel.get_category(id=line[0])
                    attribute_name = line[1]
                    if line[2] == 137476:
                        attribute_value = line[4]
                    else:
                        attribute_value = line[3]
                    p.attributes[attribute_name] = attribute_value
                except:
                    pass

            # add link from property to category
            cursor.execute("select IdTyp,IdProp from TypProp union select IdCat,IdProp from PropCat")
            for prop in cursor:
                try:
                    idtyp = prop[0]
                    idprop = prop[1]
                    typ = self.metamodel.get_category(id=idtyp)
                    p = self.metamodel.get_property(id=idprop)
                    p.category = typ
                except:
                    pass
                
            self.raw_connection.commit()
            cursor.close()
            
            setattr(self.metamodel, 'fully_load_properties', True)
    
    def _unlock(self):
        
        cursor = self.create_cursor()
        cursor.execute("SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname='postgres' AND state = 'idle in transaction'")
        cursor.close()

    def _ensure_additional_tables(self):
        """
        For table not loaded in version 7.3.x
        
        """
        if not hasattr(self, 'pmc_subsets'):
            
            self.pmc_subsets = reflect_table('PMC_SUBSETS', self.metadata, self.engine)

        if not hasattr(self, 'pmc_subset_objects'):

            self.pmc_subset_objects = reflect_table('PMC_SUBSET_OBJECTS', self.metadata, self.engine)


        if not hasattr(self, 'appset'):
            
            self.appset = reflect_table('APPSET', self.metadata, self.engine)
            
        
        if not hasattr(self, 'setroot'):
            
            self.setroot = reflect_table('SETROOT', self.metadata, self.engine)
        
        if not hasattr(self, 'objset'):
            
            self.objset = reflect_table('OBJSET', self.metadata, self.engine)
            
        if not hasattr(self, 'ctt_object_applications'):
            
            self.ctt_object_applications = reflect_table('CTT_OBJECT_APPLICATIONS', self.metadata, self.engine)
        
        if not hasattr(self, 'keypar'):

            self.KeyPar = reflect_table('KeyPar', self.metadata, self.engine)

        if not hasattr(self, 'dss_history'):
            
            self.dss_history = reflect_table("dss_history", self.metadata, self.engine)

            
        self._ensure_sys()

    def _get_metamodel_wrapper(self):
        if not hasattr(self, '_metamodel_wrapper'):
            self._metamodel_wrapper = MetaModelConcepts(self.metamodel)
            
        return self._metamodel_wrapper
        
        

    def __repr__(self):
        return 'KnowledgeBase(%s)' % self.name


class Bookmark:
    """
    A bookmark, i.e., a source code area.
    
    """

    def __init__(self, file, begin_line, begin_column, end_line, end_column):

        self.begin_line = begin_line
        self.begin_column = begin_column
        self.end_line = end_line
        self.end_column = end_column
        self.file = file

    def contains_position(self, line, column):
        """
        True if bookmark contains a given text location.
        """
        return line >= self.begin_line and line <= self.end_line and (line > self.begin_line or column >= self.begin_column) and (line < self.end_line or column <= self.end_column)

    def contains(self, position):
        """
        True if bookmark contains another bookmark.
        """
        return self.contains_position(position.begin_line, position.begin_column) and self.contains_position(position.end_line, position.end_column)

    def get_code(self):
        """
        Returns the code corresponding to the bookmark.
        
        It requires having physical access to the source code. 
        """
        return self.__get_raw_code()
    
    def get_code_line(self, additional_lines=0):
        """
        Returns one total line of code containing the bookmark.
        Very useful for link's positions.
        
        :param additional_lines: additional lines (before and after) to be returned.
        
        Example :
        
        for a link to 'CodeDetail'
        
        >>> pos.get_code_line() 
        lstReadyForAdmin.DataValueField = "CodeDetail";
        >>> pos.get_code_line(2)
        lstReadyForAdmin.DataSource = dataSet.Tables[1];
        lstReadyForAdmin.DataTextField = "Description";
        lstReadyForAdmin.DataValueField = "CodeDetail";
        lstReadyForAdmin.DataBind();
        lstReadyForAdmin.Items.Insert(0, new ListItem("*All", string.Empty));        
        
        If the bookmark spans on several lines, this method returns an empty string.
        """
        if self.begin_line != self.end_line:
            return ""
        
        result = self.__get_raw_code(additional_lines)

        return result
    
    def _get_code_line_from_snapshot(self, additional_lines=0):
        """
        Returns one total line of code containing the bookmark. 
        The code is taken from the last snapshot. WARNING : can be quite slow
        Very useful for link's positions.
        
        :param additional_lines: additional lines (before and after) to be returned.

        .. versionadded:: 1.5.4
        """
        
        current_line = 0
        result = ""
        try:
            for line in self.file._get_code_from_last_snapshot().split('\n'):
                current_line += 1
                if current_line >= self.begin_line - additional_lines and current_line <= self.end_line + additional_lines:
                    result += line
                if current_line > self.end_line + additional_lines:
                    break
        except:
            pass
        return result
    
    
    def __get_raw_code(self, additional_lines=0):
        
        current_line = 0
        result = ""
        try:
            with open_source_file(self.file.get_path()) as fp:
                for line in fp:
                    current_line += 1
                    if current_line >= self.begin_line - additional_lines and current_line <= self.end_line + additional_lines:
                        result += line
                    if current_line > self.end_line + additional_lines:
                        break
        except:
            pass
        return result
        
    
    def __repr__(self):
        return 'Bookmark(%s, %s, %s, %s, %s)' % (str(self.file), self.begin_line, self.begin_column, self.end_line, self.end_column)


class KnowledgeBaseElement:
    
    def _convert_into_property(self, prop):
        """
        Convert a string, id, etc into a cast.application.internal.metamodel.Property
        """
        try:
            if type(prop) is str:
                return self.kb.metamodel.get_property(name=prop)
            elif type(prop) is int:  
                return self.kb.metamodel.get_property(id=prop)
            else:
                return prop
        except:
            raise RuntimeError("Invalid property " + str(prop))


    def _add_property_value(self, prop, value):
        
        if not hasattr(self, '_properties'):
            setattr(self, '_properties', {})
        
        properties = getattr(self, '_properties')
        if not prop in properties:
            
            if prop.get_maximal_cardinality() == 1:
                properties[prop] = value
            else:
                properties[prop] = [value]
        else:
            if prop.get_maximal_cardinality() == 1:
                properties[prop] = value
            else:
                properties[prop].append(value)
    
    def _concat_property_value(self, prop, value):
        """
        For multi line values
        """
        properties = getattr(self, '_properties')
        if prop in properties:
            
            if prop.get_maximal_cardinality() == 1:
                properties[prop] += value
            else:
                properties[prop][-1] += value
            
        else:
            # should not happen 
            pass
    
    
    def _declare_property_loaded(self, prop):
        """
        Says that prop is loaded into object
        """
        if not hasattr(self, '__loaded_props'):
            setattr(self, '__loaded_props', [])
        
        _loaded_properties = getattr(self, '__loaded_props')
        _loaded_properties.append(prop)



class WithProperties:

    def _get_property(self, prop):
        """
        Return an object property.
        
        :param str or int or Property prop: the property fullname, or property id or property to get
        """
        if not hasattr(self, '_properties'):
            raise RuntimeError("Cannot use Object.get_property() if property has not been loaded")
        
        properties = self._properties
        
        if type(prop) is str:
            prop = self.kb.metamodel.get_property(name=prop)
        elif type(prop) is int:
            prop = self.kb.metamodel.get_property(id=prop)

        if hasattr(self, '__loaded_props'):
            
            if prop not in getattr(self, '__loaded_props'):
                raise RuntimeError("Property %s has not been loaded" % str(prop))
        
        try:
            return properties[prop]
        except:
            
            if prop.get_maximal_cardinality() == 1:
                return None
            else:
                return []    

    def _get_violations(self, prop):
        """
        Return the violations of an object.
        
        :param str or int or Property prop: the property fullname, or property id or property to get
        """
        if not hasattr(self, '_violations'):
            raise RuntimeError("Cannot use Object.get_violations() if violation has not been loaded")
        
        violations = self._violations
        
        if type(prop) is str:
            prop = self.kb.metamodel.get_property(name=prop)
        elif type(prop) is int:
            prop = self.kb.metamodel.get_property(id=prop)
        
        if hasattr(self, '__loaded_violations'):
            
            if prop not in getattr(self, '__loaded_violations'):
                raise RuntimeError("Violation %s has not been loaded" % str(prop))
        
        try:
            return violations[prop]
        except:
            return []    

class Object(KnowledgeBaseElement, WithProperties):
    """
    A KB object of any kind
    """

    def __init__(self, kb, identifier, name, typ, additional_values=None):
        self.kb = kb
        # cached data
        self.id = identifier
        self.name = name
        # metamodel type see cast.application.internal.metamodel.Type
        self.type = typ
        
        # loadable informations
        self.sub_objects = None
        self.positions = None
        
        self.application = None
        self.projects = None
        self.parent = None
        self.children = None
        self.fullname = None
        self.path = None
        
        try:
            self.fullname = additional_values['fullname']
        except:
            pass

        try:
            self.path = additional_values['path']
        except:
            pass
        
        try:

            self.positions = []
            self.positions.append(Bookmark(additional_values['file'],
                                           additional_values['begin_line'],
                                           additional_values['begin_column'],
                                           additional_values['end_line'],
                                           additional_values['end_column']))
        except:
            pass
        
        try:
            
            self.application = additional_values['application']
        except:
            pass

    def get_name(self):
        """
        Returns object name.
        """
        return self.name

    def get_fullname(self):
        """
        Returns object fullname.
        """
        return self.fullname

    @experimental
    def get_qualified_name(self):
        """
        Give a qualified name usefull for linking. 

        Try to compensate fullnames differences
        
        @since 1.4.0
        """
        
        
        # C++ case        
        Cpp = self.kb.metamodel.get_category(id=140009)
        if self.type.inherit_from(Cpp):
            return '.'.join(re.findall('\[([^\][]+)\]', self.fullname)[1:])
        
        # @todo : handle other cases
        
        # Dotnet, sqls, java
        return self.fullname
        
        
    def get_prefixed_name(self):
        """
        Returns object type.name.
        """
        return self.type.name + '.' + self.name

    def get_type(self):
        """
        Returns object's type name.
        """
        return self.type.get_name()

    def get_metamodel_type(self):
        """
        Returns object metamodel type.
        
        :rtype: cast.application.internal.metamodel.Type
        """
        return self.type

    def get_positions(self):
        """
        Returns object's code positions.
        
        :rtype: :class:`cast.application.Bookmark`
        """
        if self.positions is None:
            """
            @todo: load the positions of the object
            """
            pass

        return self.positions

    def get_property(self, prop):
        """
        Return an object property.
        
        :param str or int prop: the property fullname, or property id to get
        """
        return self._get_property(prop)

    def get_violations(self, prop):
        """
        Return the violations for an object.
        
        The term violation correspond to the bookmarks of quality rule with bookmarks.
        
        :return: list of violations, i.e. triplet (property, Bookmark, list of Bookmark)
        
        :param str or int prop: the property fullname, or property id corresponding to the violations
        """
        return self._get_violations(prop)

    def save_property(self, prop, value):
        """
        Save a property on current object.
        
        :param prop: the property to save. Either a string for the fullname of the property or an integer for the property id. 
        :param value: 
            the value to set, either a integer, a string or a list of those
            integers should be 32 bits integer (i.e. ranging from [ -2^31+1, 2^31-1])

        The current plugin must have declared the property has his own.  
        :see :meth:`cast.application.Application.declare_property_ownership`
        
        Saving several times the same property on the same object will trigger an exception.
        Both saving a given property on an object and saving a violation for that property will trigger an exception. 
        """
        _property = self._convert_into_property(prop)
        
        # @todo : apply authorisation matrix
        
        self.application._get_raw_saver().add_property(self, _property, value)

    def save_violation(self, prop, bookmark, additional_bookmarks=[]):
        """
        Add a violation for the given rule.

        prop is the fullname of a Metamodel property

        :param str prop: a property full name that count the number of rule violations
        :param cast.application.Bookmark bookmark: a bookmark to indicate the position of the violation
        :param cast.application.Bookmark additional_bookmarks: additional bookmarks that help
                                                               understanding the violation
        
        The property 'prop' is automatically valorised with the number of violations for the object.
         
        .. warning:: The property 'prop' is automatically valorised with the number of violations for the object. So do not use save_property for this property as it will trigger and exception.
        
        The current plugin must have declared the prop has his own.
        :see :meth:`cast.application.Application.declare_property_ownership`
        
        """ 
        _property = self._convert_into_property(prop)
        
        # @todo : apply authorisation matrix
        
        self.application._get_raw_saver().add_violation(self, _property, bookmark, additional_bookmarks)

    def set_as_external(self):
        """
        Set the object as external to the application (and all its descendants)
        """
        self.application._get_raw_saver().set_as_external(self)

    def get_application(self):
        """
        Returns object's application
        """
        return self.application

    def is_dbms(self):
        """
        True when object is an object from a database.
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_dbms())

    def is_directory(self):
        """
        True when object is a directory.
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_directory())

    def is_file(self):
        """
        True when object is a file. 
        """
        _type = self.type
        return (_type.inherit_from('shell') or _type.inherit_from('File')) and not self.is_directory()

    def is_program(self):
        """
        True when object is a program.
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_program())
    
    def is_class(self):
        """
        True when object is class or interface.
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_class())
    
    def is_executable(self):
        """
        True when object is callable and contains executable code.
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_executable())

    def is_package(self):
        """
        True when object is a package, namespace, module, schema, etc...
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_package())

    def is_variable(self):
        """
        True when object is a variable, field, member variable, something that can receive an assignment.
        """
        # field is there for some technos but not for others
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_variable())

    def is_table(self):
        """
        True when object is a database table or view.
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_table())
    
    def is_nosql_collection(self):
        """
        True when object is a nosql collection. Similar to a table.
        
        .. versionadded:: 1.6.7
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_nosql_collection())
    
    def is_index(self):
        """
        True when object is a database index.
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_index())
    
    def is_foreignkey(self):
        """
        True when object is a database foreign key.
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_foreignkey())

    def is_web_service_operation(self):
        """
        True when object is a web service operations (get, post, ...).
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_web_service_operation())

    def is_web_service_call(self):
        """
        True when object is a web service call (client side).
        
        .. versionadded:: 1.5.13
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_web_service_call())

    def is_rest_web_service_call(self):
        """
        True when object is a REST call (client side).

        .. versionadded:: 1.6.23
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_rest_web_service_call())

    def is_rest_web_service_receive(self):
        """
        True when object is a web REST receive (server side).

        .. versionadded:: 1.6.23
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_rest_web_service_receive())

    def is_soap_web_service_call(self):
        """
        True when object is a SOAP call (client side).

        .. versionadded:: 1.6.23
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_soap_web_service_call())

    def is_soap_web_service_receive(self):
        """
        True when object is a SOAP receive (server side).

        .. versionadded:: 1.6.23
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_soap_web_service_receive())

    def is_form(self):
        """
        True for forms, controls and events.
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_form())

    def is_default_transaction_entry(self):
        """
        "APM Forms"
        "APM IFPUG Transaction"
        "CAST_Web_File"
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_default_transaction_entry())

    def is_program_call(self):
        """
        True when object is a program call (client side).
        
        .. versionadded:: 1.6.14
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_program_call())

    def is_bean(self):
        """
        True when object is a java bean.
        
        .. versionadded:: 1.6.14
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_bean())

    def is_cloud_function(self):
        """
        True when object is a cloud function (AWS Lambda, Azure function, ...).
        
        .. versionadded:: 1.6.14
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_cloud_function())

    def is_cloud_function_call(self):
        """
        True when object is a call to a cloud function.
        
        .. versionadded:: 1.6.14
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_cloud_function_call())

    def is_rpc_receive(self):
        """
        True when object is a RPC receive.
        
        .. versionadded:: 1.6.14
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_rpc_receive())

    def is_rpc_call(self):
        """
        True when object is a call to RPC.
        
        .. versionadded:: 1.6.14
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_rpc_call())

    def is_message_send(self):
        """
        True when object is a send of a message.
        
        .. versionadded:: 1.6.14
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_message_send())

    def is_message_receive(self):
        """
        True when object is a receiving of a message.
        
        .. versionadded:: 1.6.14
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_message_receive())

    def is_query(self):
        """
        True when object is a query
        
        .. versionadded:: 1.6.18
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_query())

    def is_entity(self):
        """
        True when object is an ORM entity.

        :rtype: :class:`cast.application.ObjectQuery`
        
        .. versionadded:: 1.6.18
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_entity())
    
    def is_entity_operation(self):
        """
        True when object is an ORM entity operation.

        :rtype: :class:`cast.application.ObjectQuery`
        
        .. versionadded:: 1.6.18
        """
        return self.__generic_is(self.kb._get_metamodel_wrapper().get_entity_operation())

    def __generic_is(self, categories):
        """
        Generic version of is_xxx
        """
        for category in categories:
            if self.type.inherit_from(category):
                return True
            
        return False

    def get_projects(self):
        """
        Returns object's projects
        """
        if not self.projects:
            
            self.projects = self.application._get_projects(self)
                        
        
        return self.projects

    def load_objects(self):
        """
        loads the sub objects of an object.
        """
        if not self.sub_objects:
            return []

        return self.sub_objects

    def find_most_specific_object(self, line, column):
        """
        Find the most specific sub object containing line, column.
        """
        result = self
        result_position = None
        for sub_object in self.load_objects():
            for position in sub_object.get_positions():
                if position.contains_position(line, column) and (not result_position or result_position.contains(position)):
                    result = sub_object
                    result_position = position
                    
        return result
        
    def _has_additional_values(self, additional_values, expected_values):
        
        for value in expected_values:
            if not value in additional_values:
                return False
            
        return True
    
    def _get_sub_object_by_id(self, _id):
        
        if not self.sub_objects:
            return None
        
        for o in self.sub_objects:
            if o.id == _id:
                return o
        
        return None
    
    def load_children(self, categories=None, is_sorted=None):
          
        if not self.children:
            self.children = []
            if categories:
                for cat in categories:
                    for o in self.kb._search_objects(self.application.projects_ids, name=None, category=cat, application=self.application, parent_object=self):
                        self.children.append(o)
                        o.parent = self
            else:
                for o in self.kb._search_objects(self.application.projects_ids, name=None, category=None, application=self.application, parent_object=self):
                    self.children.append(o)
                    o.parent = self
          
        if is_sorted:
            self.children.sort(key=Object.get_prefixed_name)
            
        return self.children

    def get_children(self, categories=None):
        
        if categories:
            return [ child for child in self.children if child.type.inherit_from_one_of(categories) ]
        else:
            return [ child for child in self.children ]
    
    def __repr__(self):
        
        display_name = self.get_qualified_name()
        if not display_name:
            display_name = self.get_name()
            
        return 'Object(%s, %s)' % (display_name, self.get_type())

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id    
    

    def _convert_into_types(self, type_names):
        """
        Convert a string, id, list of those into a list of cast.application.internal.metamodel.Type
        """
        def convert_single(_cat):
            
            try:
                cat = None
                if type(_cat) is str:
                    cat = self.kb.metamodel.get_category(name=_cat)
                elif type(_cat) is int:  
                    cat = self.kb.metamodel.get_category(id=_cat)
                if cat:
                    return cat.get_sub_types()
                else:
                    raise RuntimeError("Invalid type or category " + str(_cat))
            except:
                raise RuntimeError("Invalid type or category " + str(_cat))
        
        if type(type_names) is list:
            
            result = []
            for _typ in type_names:
                result += convert_single(_typ)
            return result
        else:
            return convert_single(type_names)
    
    def _add_position(self, file, begin_line, begin_column, end_line, end_column):
        
        if not self.positions:
            self.positions = []
        self.positions.append(Bookmark(file, begin_line, begin_column, end_line, end_column))
    

class Application(Object):
    """
    A kb object representing an application
    """
    def __init__(self, kb, identifier, name, typ):
        Object.__init__(self, kb, identifier, name, typ)

        self.projects_ids = []
        self.projects = []
        self.projects_by_id = {}
        self._calculate_project_list()
        
        # special job type for plugins. 
        # lifetime is not handled through castms.
        self.type_id = 141884
        # the job names created during the session
        self.job_names = set()
        self.current_plugin = None
        self.amt_saver = None
        
        # added in 1.5.4
        self.managment = None
        
    def sql_tool(self, query):
        """
        Execute a so called SQL Tool.
        
        :param str or file query: sql batch

        @type query: str or file
        
        Basically it executes a query after having replaced some special variables :
        §
        
        See documentation of CAST-MS for further detail.
        """
        cursor = self.kb.create_cursor()
        
        
        self.kb._execute_raw_query(cursor, query)
        
        # we return result...
        return cursor

    def update_cast_knowledge_base(self, name, query):
        """
        Execute a so called Update Cast knowledge base.

        :param str or file query: sql batch

        @type query: str or file
        
        Basically it executes a query after having replaced some special variables :
        §
        
        to fill in CI_xxx tables and launch the tools that perform the update.
        
        See documentation of CAST-MS for further detail.
        """
        cursor = self.kb.create_cursor()
        
        plugin_name = self.current_plugin.get_name() if self.current_plugin else ''
        logging.debug('plugin name is %s', plugin_name)
        
        
        """
        plugin_name is generally of the form : a.b.c
        plugin_name is a directory name
        
        name can be anything
        """
        job_name = "%s/%s/%s" % (self.name, plugin_name, name)
        if job_name in self.job_names:
            raise RuntimeError('You cannot create 2 update_cast_knowledge_base with the same name : %s' % name)

        """
        @todo : C++ code does something before...
        """
        self.job_names.add(job_name)
        
        # execute init
        job_id = self.create_job(job_name)
        
        is_mssql = False
        
        if self.kb.engine.dialect.name == 'mssql':
            is_mssql = True
            cursor.execute('exec CI_INIT_DATA %s' % job_id)
        else:
            self.kb._execute_function(cursor, 'ci_init_data', '%s' % job_id)
        
        self.kb.raw_connection.commit()
        
        # execute user query
        self.kb._execute_raw_query(cursor, query)

        # execute check and close 
        if is_mssql:
            cursor.execute('exec CI_CHECK_DATA %s,%s' % (job_id, self.id))
        else:
            self.kb._execute_function(cursor, 'ci_check_data', '%s,%s' % (job_id, self.id))
        self.kb.raw_connection.commit()
        if is_mssql:
            cursor.execute('exec CI_PROCESS_DATA %s' % job_id)
        else:
            self.kb._execute_function(cursor, 'ci_process_data', '%s' % job_id)
        
        self.kb.raw_connection.commit()

    def get_knowledge_base(self):
        """
        Access to the knowledge base
        
        :rtype: :class:`cast.application.KnowledgeBase`

        """
        return self.kb
    
    def get_managment_base(self):
        """
        Access to managment base.
        
        :return: :class:`cast.application.managment.ManagmentBase`
    
        WARNING : 
           this version only works for combined install on the same server.
           Future version of CAIP will leverage this limitation.
           
           Not working on sqlserver
        
        .. versionadded:: 1.5.4
        """
        if not hasattr(self, 'managment'):
            setattr(self, 'managment', None)
        
        if not self.managment:
            
            kb_name = self.kb.name

            if not kb_name:
                # ms with database encoded in the connectio nstring ...
                url = str(self.kb.engine.url)
                result = re.search('DATABASE=(.*);', url)
                kb_name = result.group(1)
                print(kb_name)
            
            if kb_name.lower().endswith('_local'):
                # case sensisitve ms
                if kb_name.endswith('_local'):
                    postfix = '_mngt'
                else:
                    postfix = '_MNGT'
                
                mngt_name = kb_name[:-6] + postfix
                self.managment = ManagmentBase(mngt_name, self.kb.engine) 
        
        if not self.managment:
            logging.warning('get_managment_base is only working for combined installs')
            
        return self.managment

    def get_application_configuration(self):
        """
        Access to managment base application.
        
        :return: :class:`cast.application.managment.Application`
    
        WARNING : 
           this version only works for combined install on the same server.
           Future version of CAIP will leverage this limitation.
        
        .. versionadded:: 1.5.4
        """
        try:
            mngt = self.get_managment_base()
            return mngt.get_application(self.name)
        except:
            logging.warning('get_application_configuration is unsupported')
            return None
        
    
    def get_projects(self):
        """
        The result projects of the application.
        
        :rtype: iterable of :class:`cast.application.Project`
        """
        return self.projects

    def objects(self):
        """
        All internal objects of the application as an iterable.
        
        .. versionadded:: 1.5.0
        
        :rtype: :class:`cast.application.ObjectQuery`
        """
        return ObjectQuery(application=self)
        
    def links(self):
        """
        All the links of the application as an iterable.
    
        .. versionadded:: 1.5.0
        
        :rtype: :class:`cast.application.LinkQuery`
        """
        return LinkQuery(application=self)
        
    def get_objects(self, internal=True, external=False):
        """
        Return a iterable collection of all the objects of the application.
        
        Projects are not considered as part of the of the application as they
        already are accessible as direct child through get_projects.

        :rtype: iterable of :class:`cast.application.Object`
        """
        return self.kb._get_objects(self.projects_ids, internal, external, self)

    def get_objects_by_name(self, name, internal=True, external=False):
        """
        Search objects of a given name 
        
        .. warning:: Use with caution, do not use it with a variable name parameter (unit queries cause performances issues)
        
        :param str name: name of the searched object.  
        
        :rtype: iterable of :class:`cast.application.Object`
        
        """
        return self.kb._get_objects_by_name(self.projects_ids, name, internal, external, self)

    def search_objects(self, name=None, category=None, load_properties=False):
        """
        Search objects by name or/and by type
        
        .. warning:: Deprecated
        
        .. deprecated:: 1.5.0
           Use :func:`cast.application.Object.objects` instead + :func:`cast.application.ObjectQuery.load_property`
        
        :param str name: the name of the searched object
        :param str category: the category name of the searched object
        :param bool load_properties: if True properties of objects will be available. Slower.
        
        :rtype: iterable of :class:`cast.application.Object`
        """
        return self.kb._search_objects(self.projects_ids, name, category, self, load_properties=load_properties)
    
    def get_files(self, languages=[], external=False):
        """
        Get all the files of the application.
        
        :param languages: list of str possible categories for the searched files.  
        :param external: when True takes also files marked as external
        :rtype: iterable of :class:`cast.application.File`
        
        """
        return self.kb._get_files(self.projects_ids, languages, self, external)
        
    def get_databases(self, is_sorted=None):
        """
        Get all the database objects of the application.
        
        :rtype: iterable of :class:`cast.application.Database`
        
        """
        databases = []
        for project in self.projects:
            if not project:
                continue
            project.load_children(None, is_sorted)
            try:
                # Oracle instances
                databases.extend(project.get_children(['CAST_Oracle_Instance']))
            except:
                pass
            try:
                # Legacy Oracle instances
                machines = list(project.get_children(['CAST_SQL_Machine']))
                for machine in machines:
                    machine.load_children(None, is_sorted)
                    databases.extend(machine.get_children(['CAST_SQL_Instance']))
            except:
                pass
            try:
                # Other instances
                instances = list(project.get_children(['CAST_SQL_InstanceContainer']))
                for instance in instances:
                    if instance.type.name != 'CAST_Oracle_Instance':
                        instance.load_children(None, is_sorted)
                        databases.extend(instance.get_children(['CAST_SQL_RootContainer']))
            except:
                pass
            try:
                # Legacy Other instances (DATABASE are projects)
                if project.type.name == 'DATABASE':
                    databases.append(project)
                if project.type.name == 'DB2ANALYZE':
                    databases.extend(project.get_children(['UDBDATABASE']))
                    
                
            except:
                pass

        return databases
        
    def get_analyzer_technologies(self):
        """
        Returns the technologies present in this application.
        
        :rtype: multimap language --> projects for each language found
        
        @todo : in case of UA we also need principal projects of ua
        
        language is of type ast.application.internal.metamodel.Category
        
        .. versionadded:: 1.5.9
        """
        result = defaultdict(list)
        for project in self.get_projects():
    
            language = project.get_metamodel_type().get_language()
            if language:
                # UAL : UA language technology
                # N/A:
                # REFIND_PROJECT
                # KB_API_PROJECT
                # Server : DatabaseSubset
                # PLSQL_DYNAMIC_PROJECT
                if language.name not in ['UAL', 'N/A', 'Server']:
                    result[language].append(project)
            else:
                if project.get_metamodel_type().name == 'CAST_SQL_MSTSQL_Project':
                    
                    result[self.kb.metamodel.get_category(id=141155)].append(project)
            
        return result
            
        
    def declare_property_ownership(self, prop, scope):
        """
        State that the current plugin handles the production of a property for some types.
        Also works for links by passing a LinkQuery.
        
        The current plugin will calculate all the values for that property for all the objects of those types.
        Object of that type that will not receive a value will have no value.
        
        scope is the cleanup scope.
        
        Necessary for saving properties.
        
        :param prop: the property to save. Either a string for the fullname of the property or an integer for the property id. 
        :param scope: list of strings the names of the types or categories, or a :class:`cast.application.LinkQuery`
        
        All given types must have the property.
        """
        _property = self._convert_into_property(prop)
        
        # @todo : apply authorisation matrix
        
        # @todo : not really good ?
        if type(scope).__name__ == 'LinkQuery':
            
            self._get_raw_saver().declare_link_property(scope, _property)
            
        else:
    
            types = self._convert_into_types(scope)
            
            def has_property(cat, prop):
                
                if prop in cat.get_properties():
                    return True
                
                for c in cat.all_inherited_categories:
                    if prop in c.get_properties():
                        return True
                    
                return False
    
            for t in types:
                if not has_property(t, _property):
                    raise RuntimeError("Property " + str(_property.get_name()) + " is not valid for type " + str(t.get_name()))
            
            self._get_raw_saver().declare_property(types, _property)
        
    def create_job(self, name, type_id=None):
        """
        Create or get an application level plugin job.
        Mark it as used. 
        See _mark_plugin_jobs_as_unused and _delete_unused_jobs.
        """
        if not type_id:
            type_id = self.type_id
        
        AnaJob = reflect_table("AnaJob", self.kb.metadata, self.kb.engine) 
        
        UsrProJob = reflect_table("UsrProJob", self.kb.metadata, self.kb.engine)  

        AnaAttr = reflect_table("ANAATTR", self.kb.metadata, self.kb.engine)  
        
        # search first if job of that name exist
        plugin_jobs = select([AnaJob.c.idjob]).where(AnaJob.c.jobtyp == type_id).where(AnaJob.c.jobnam == name)
        query = select([UsrProJob.c.idjob]).where(UsrProJob.c.idjob.in_(plugin_jobs)).where(UsrProJob.c.idusrpro == self.id)
        
        results = self.kb.engine.execute(query)
        job_id = None
        for result in results:
            job_id = result[0]
        
        
        # job exist : just marking its
        if job_id:
            
            # temp code
            delete = AnaAttr.delete().where(AnaAttr.c.session_id == job_id)
            self.kb.engine.execute(delete)
            
            ins = AnaAttr.insert().values(session_id=job_id,
                                          attrnam='SyncOnlyModified',
                                          intval=0)
            self.kb.engine.execute(ins)
            
            ins = AnaAttr.insert().values(session_id=job_id,
                                          attrnam='AnalysisInfoProperties_Common_EscalateLinks',
                                          intval=0)
            self.kb.engine.execute(ins)
            # temp code
            
            
            logging.debug('Recreating job name %s id %d ', name, job_id)
            self._mark_job_as_used(job_id)
            return job_id
        
        
        # job does not exist : creating
        dialect = self.kb.engine.dialect.name
        if dialect == 'mssql':
            
            """
            Next ID to allocate is in Parms table, so select then update.
            """
            
            Parms = reflect_table('Parms', self.kb.metadata, self.kb.engine)
            
            logging.debug('getting id...')
            
            next_id = select([Parms.c.intval]).where(Parms.c.lib == 'Id')
            results = self.kb.engine.execute(next_id)
            for result in results:
                job_id = result[0]
            
            logging.debug('got id %d', job_id)
            
            logging.debug('reserving id...')
            self.kb.engine.execute(Parms.update().where(Parms.c.lib == 'Id').values(intval=job_id+1))
            logging.debug('reserved')
            
            logging.debug('executing insert Keys...')
            ins = self.kb.Keys.insert().values(idkey=job_id,
                                               keynam=name,
                                               objtyp=type_id,
                                               keytyp='XXXXXX',
                                               keysubtyp=-1,
                                               keyclass=-1,  # no need to have a correct keyclass
                                               keyprop=0,
                                               idusrdevpro='???',
                                               keydevdat=date.today())
            result = self.kb.engine.execute(ins)
            logging.debug('executed')
            
        else:
            # Warning : DOP says that even in that case, Parms is filled ...
            # checked and answer is no : Parms contains 11 on a populated KB
            ins = self.kb.Keys.insert().values(keynam=name,
                                               objtyp=type_id,
                                               keytyp='XXXXXX',
                                               keysubtyp=-1,
                                               keyclass=-1,  # no need to have a correct keyclass
                                               keyprop=0,
                                               idusrdevpro='???',
                                               keydevdat=date.today())
         
            result = self.kb.engine.execute(ins)
            job_id = result.inserted_primary_key[0]

        logging.debug('Creating new job name %s id %d ', name, job_id)
        
        ins = AnaJob.insert().values(idjob=job_id,
                                     jobnam=name,
                                     jobtyp=type_id,
                                     jobver=730,  # do not care in fact
                                     idcnx=-1)
        
        self.kb.engine.execute(ins)
        
        ins = UsrProJob.insert().values(idusrpro=self.id,
                                        idjob=job_id,
                                        ordnum=1,
                                        prop=0)
        # this makes the job seen as used
        self.kb.engine.execute(ins)

        # oracle need it        
        ins = AnaAttr.insert().values(session_id=job_id,
                                      attrnam='SyncOnlyModified',
                                      intval=0)
        self.kb.engine.execute(ins)
 
        # oracle need it        
        ins = AnaAttr.insert().values(session_id=job_id,
                                      attrnam='AnalysisInfoProperties_Common_EscalateLinks',
                                      intval=0)
        self.kb.engine.execute(ins)
       
        return job_id

    def _mark_plugin_jobs_as_unused(self):
        
        cursor = self.kb.create_cursor()
        try:
            cursor.execute("update UsrProJob set Prop = -1 where IdUsrPro = %d and IdJob in (select IdKey from Keys where ObjTyp = %d)" % (self.id, self.type_id))
            self.kb.raw_connection.commit()
        except:
            self.kb.raw_connection.rollback()
            
    def _mark_job_as_used(self, job_id):
        
        cursor = self.kb.create_cursor()
        try:
            cursor.execute("update UsrProJob set Prop = 0 where IdUsrPro = %d and IdJob = %d" % (self.id, job_id))
            self.kb.raw_connection.commit()
        except:
            self.kb.raw_connection.rollback()

    def _delete_unused_jobs(self):

        cursor = self.kb.create_cursor()
        
        try:
            
            # detach created objects from other projects to allow cleanup
            # all 'create_objects' projects to be removed 
            query = """
            select IdPro from AnaPro where IdJob in (
                select IdJob from UsrProJob
                             where IdUsrPro = %d and
                             Prop = -1 and IdJob in (
                                select IdKey from Keys where ObjTyp = %d and KeyNam like '%%%%/create_objects'))
            """ % (self.id, self.type_id)
            
            projects_to_remove = []
            cursor.execute(query)
            for line in cursor:
                projects_to_remove.append(line[0])
                logging.info('project to clean up %s', line[0])
            
            if projects_to_remove:
                # remove all other project belongings for objects belonging to the project to remove
                # we have added the objects as internal to the parent's project so that we can see them on enlighten 
                # but we need to remove this belonging in order to correctly cleanup 
                clean = self.kb.ObjPro.delete().where(self.kb.ObjPro.c.idobj.in_(
                    select([
                        self.kb.ObjPro.c.idobj
                        ]).where(self.kb.ObjPro.c.idpro.in_(projects_to_remove)))).where(~self.kb.ObjPro.c.idpro.in_(projects_to_remove))
                        
                self.kb.engine.execute(clean)
                
                
            # delete jbs and use normal proc to delete
            cursor.execute("""
            delete from UsrProJob
                where IdUsrPro = %d and
                      Prop = -1 and
                      IdJob in (select IdJob from AnaJob 
                                 where JobTyp = %d)""" % (self.id, self.type_id))
            
            
            self.kb.raw_connection.commit()
            self.kb._execute_function(cursor, 'UsrPro_CleanUp')
            self.kb.raw_connection.commit()
        except:
            logging.warning('%s', traceback.format_exc())
            self.kb.raw_connection.rollback()
        
        # global cleanup of dlm 
        self._reset_dlm_missing_plugins()
    
    def _reset_dlm_missing_plugins(self):
        """
        Reset the validated/ignored produced by plugins not here anymore.
        """
        # get the active plugin name list
        active_plugin_names = []
        
        for plugin in get_plugins():
            name = plugin.get_name()
            active_plugin_names.append(name)
            active_plugin_names.append(name + ' validate')
            active_plugin_names.append(name + ' ignore')
        
        Acc = reflect_table('Acc', self.kb.metadata, self.kb.engine)
        FusAcc = reflect_table('FusAcc', self.kb.metadata, self.kb.engine)
        ObjDsc = reflect_table('ObjDsc', self.kb.metadata, self.kb.engine)
        
        links = select([FusAcc.c.idacc]).select_from(FusAcc.join(ObjDsc, 
                                                                 and_(ObjDsc.c.inftyp == -1,
                                                                      ObjDsc.c.infsubtyp == 0,
                                                                      ObjDsc.c.infval.notin_(active_plugin_names),
                                                                      ObjDsc.c.idobj == FusAcc.c.idfus)))

        up = Acc.update().where(Acc.c.idacc.in_(links)).values(prop = bitand(Acc.c.prop, -98305, self.kb.engine))
        self.kb.engine.execute(up)
        
        # reset the property values for reviewed by...
        delete = ObjDsc.delete().where(and_(ObjDsc.c.inftyp == -1,
                                            ObjDsc.c.infsubtyp == 0,
                                            ObjDsc.c.infval.notin_(active_plugin_names)))
        self.kb.engine.execute(delete)
        
    def _calculate_project_list(self):
        """
        Precalculate the list of result projects of that application.
        """
        cursor = self.kb.create_cursor()
        
        
        
        # first query with prodep : modern approach
        cursor.execute("select distinct(IdPro) from ProDep where IdProMain in (select IdRoot from UsrProRoot where IdUsrPro = %s)" % self.id)
        p1 = set([x[0] for x in cursor])
        
        # second query with proroot : legacy. For example DB2 ZOS.
        # dotnet have lines in it but it generates None Projects...
        cursor.execute("select distinct(IdPro) from ProRoot where IdRoot in(select IdRoot from UsrProRoot where IdUsrPro = %s)" % self.id)
        p2 = set([x[0] for x in cursor])
        
        # take both
        self.projects_ids = list(p1 | p2)
        
        self.projects = []
        
        for identifier in self.projects_ids:
            try:
                project = self.kb._load_object(identifier)
                if project:
                    self.projects.append(project)
            except KeyError:
                # for example metamodel type id does not exists anymore : skip
                pass
        
        for project in self.projects:
            if project:
                project.application = self
                self.projects_by_id[project.id] = project
        
        # prodep relationship
        cursor.execute("select IdProMain, IdPro from ProDep where IdProMain in (select IdRoot from UsrProRoot where IdUsrPro = %s)" % self.id)
        for x in cursor:
            try:
                parent = self.projects_by_id[x[0]]
                child = self.projects_by_id[x[1]]
                
                if parent != child:
                    parent._dependent_projects.append(child)
                    child._depends_on.append(parent)
                
            except:
                pass
        
#         # @todo temporary try
#         # used to locks update CSV 
#         self._available_types = set()
#         self._available_types_per_project = defaultdict(set)
#         # calculate the list of used types/per projects
#         # there is a little risk that update_csv has not been done in 'standalone' cases
#         cursor.execute("select distinct APPLICATION_ID, OBJECT_TYPE from CTT_OBJECT_APPLICATIONS")
#         for line in cursor:
#             self._available_types.add(line[1])
#             try:
#                 self._available_types_per_project[self.projects_by_id[line[0]]] = self.kb.metamodel.get_category(id=line[1])
#             except KeyError:
#                 pass
#         
        self.kb.raw_connection.commit()
        
        cursor.close()
        
    def _get_link_saver(self):
        
        # @todo : apply authorisation matrix
        
        if self.kb.engine.dialect.name == 'sqlite':
            return self._get_raw_saver()
        else:
            return self._get_amt_saver()
        
    def _get_amt_saver(self):
        
        current_phase = 'end_application' # default
        if hasattr(self, '_current_phase'):
            current_phase = getattr(self, '_current_phase')
            
        # here current_phase is in ['end_application_create_objects', 'end_application'] or some other steps
        
        
        if not self.amt_saver:
            
            plugin_name = self.current_plugin.get_name() if self.current_plugin else ''
            logging.debug('plugin name is %s', plugin_name)
            """
            plugin_name is generally of the form : a.b.c
            plugin_name is a directory name
            
            name can be anything
            
            job name will be 
            
            - application_name/plugin_id for end_application
            - application_name/plugin_id/create_objects for end_application_create_objects
            
            
            
            """
            job_name = '%s/%s' % (self.name, plugin_name)
            if current_phase == 'end_application_create_objects':
                job_name += '/create_objects'
            
            self.amt_saver = Saver(self, None, job_name, self.current_plugin.get_name(), self.current_plugin.get_version())
        
        return self.amt_saver

    def _run_amt_saver(self):
        """
        Finalisation phase called after current plugin execution
        """
        
        if self.amt_saver:
            
            current_phase = 'end_application' # default
            if hasattr(self, '_current_phase'):
                current_phase = getattr(self, '_current_phase')
            
            
            # all saving at the end
            plugin_name = self.current_plugin.get_name() if self.current_plugin else ''
            
            # here, if we want to have create_link available at other steps we will need to generate new names for jobs
            job_name = '%s/%s' % (self.name, plugin_name)
            
            # for example, here we create a new job for the new sub step 'create objects' 
            if current_phase == 'end_application_create_objects':
                job_name += '/create_objects'
            
            job_id = self.create_job(job_name)
            self.amt_saver.job_id = job_id
            
            self.amt_saver.save()
            # reset for next plugin : very important
            self.amt_saver = None
        
        # force raw saver for some cleanups (cleanup of reviewed links)
        self._get_raw_saver()
        
        if hasattr(self.current_plugin, "raw_saver") and self.current_plugin.raw_saver:
            self.current_plugin.raw_saver.save()
            # reset for next plugin : very important
            self.current_plugin.raw_saver = None
                

    def _get_raw_saver(self):
        
        # attach saver on application object
        if not hasattr(self.current_plugin, "raw_saver"):
            setattr(self.current_plugin, "raw_saver", None)
        
        if not self.current_plugin.raw_saver:
            saver = RawSaver(self)
            self.current_plugin.raw_saver = saver
        
        return self.current_plugin.raw_saver
            
    
    
    def _get_projects(self, o):
        
        cursor = self.kb.create_cursor()
        cursor.execute("select distinct(IdPro) from ObjPro where IdObj = %s" % o.id)
        return [self.projects_by_id[project_id[0]] for project_id in cursor]

    def _get_in_project_query(self):
        """
        Return a sqlalchemy query that filter ids of objects in the application.
        
        so that someone can the write : 
        
        select * from keys where idkey in 
                                           (...) -- application._get_in_project_query()
        
        
        .. versionadded:: 1.6.4
        """
        return select([self.kb.ObjPro.c.idobj]).where(self.kb.ObjPro.c.idpro.in_(_get_in_project(self)))
 
    
        
    def _unlock(self):
        
        cursor = self.kb.create_cursor()
        cursor.execute("SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname='postgres' AND state = 'idle in transaction'")
        cursor.close()
        
    def __repr__(self):
        return 'Application(name=%s)' % (self.get_name())

    
class DatabaseSubset(Object):
    """
    A particular object that is a database subset
    """
    def __init__(self, kb, identifier, name, typ):
        Object.__init__(self, kb, identifier, name, typ)

    def __repr__(self):
        return 'DatabaseSubset(%s, %s)' % (self.get_name(), self.get_type())


class File(Object):
    """
    A kb object representing a source file.
    """
    def __init__(self, kb, identifier, name, typ, additional_values=None):
        Object.__init__(self, kb, identifier, name, typ, additional_values)
        self.path = None
        if additional_values and 'path' in additional_values:
            self.path = additional_values['path']
        
        # CAST_DotNet_File has no path, but fullname is path
        if not self.path and self.type and self.type.inherit_from(kb.metamodel.get_category(id=138870)):
            self.path = self.fullname
        
        # UA files, when using preprocessor, have path in temp and fullname is source path      
        if self.type and self.type.inherit_from(kb.metamodel.get_category(id=1000007)) and self.fullname:
            self.path = self.fullname
        
        # WSB_FILE have fullname as path
        if self.type and self.type.id == 888:
            self.path = self.fullname
        
        self.sub_objects_loaded = False            
            
    def __repr__(self):
        return 'File(%s, %s)' % (self.get_name(), self.get_type())

    def get_path(self):
        """
        Get the source file path
        
        :rtype: str
        """
        
        # cached value
        if self.path:
            return self.path
        
        cursor = self.kb.create_cursor()
        cursor.execute("select Path from RefPath where IdFilRef in (select IdFilRef FROM ObjFilRef where IdObj=%s)" % self.id)

        line = cursor.fetchone()
        if line:
            self.path = line[0]

        return self.path

    def load_objects(self):
        """
        Load the objects contained in the file.
        """
        if not self.sub_objects_loaded:
            self.sub_objects = []
            for o in self.kb._load_objects(self):
                self.sub_objects.append(o)
            
            self.sub_objects_loaded = True
            
        return self.sub_objects
    
    def _get_code_from_last_snapshot(self):
        """
        Gives the source code from the last snapshot
        """
        # select * from dss_sourceidtranslation -- map kb_sourceid of a file to a dss_sourceid 
        # select * from dss_code_sources -- map source_id (dss_sourceidtranslation.dss_sourceid) to the source_code
        #  --> apparently not always...
        # so using dss_source_positions.panel
        
        dss_source_positions = reflect_table('dss_source_positions', self.kb.metadata, self.kb.engine)
        dss_code_sources = reflect_table('dss_code_sources', self.kb.metadata, self.kb.engine)
        
        
        query = select([dss_code_sources.c.source_code]
                       ).where(dss_code_sources.c.source_id.in_(
                                                                select([distinct(dss_source_positions.c.source_id)]
                                                                       ).where(dss_source_positions.c.panel == self.id)
                                                                ))
        
        for line in self.kb.engine.execute(query):
            return line[0]        
        
        return ""

class DatabaseOwner(Object):
    """
    A kb object representing a database owner/Schema object.
    """
    def __init__(self, kb, identifier, name, typ, additional_values=None):
        Object.__init__(self, kb, identifier, name, typ, additional_values)
        
    def get_tables(self):
        """
        Get the tables of the schema.
        
        :rtype: list of :class:`cast.application.Object`
        """
        self.load_children()
        return [ child for child in self.children if child.type.inherit_from('Database Table') ]
        
    def get_views(self):
        """
        Get the views of the schema.
        
        :rtype: list of :class:`cast.application.Object`
        """
         
        self.load_children()
        return [ child for child in self.children if child.type.inherit_from('Database View') ]
        
    def get_procedures(self):
        """
        Get the procedures of the schema.
        
        :rtype: list of :class:`cast.application.Object`
        """
         
        self.load_children()
        return [ child for child in self.children if child.type.inherit_from('Database Procedure') ]
        
    def get_functions(self):
        """
        Get the functions of the schema.
        
        :rtype: list of :class:`cast.application.Object`
        """
         
        self.load_children()
        return [ child for child in self.children if child.type.inherit_from('Database Function') ]

    def __repr__(self):
        return 'Database Owner(%s, %s)' % (self.get_name(), self.get_type())
        

class Database(DatabaseOwner):
    """
    A kb object representing a database object.
    """
    def __init__(self, kb, identifier, name, typ, additional_values=None):
        DatabaseOwner.__init__(self, kb, identifier, name, typ, additional_values)
        self.legacy = False
        if typ.name in [ 'DATABASE', 'CAST_SQL_Instance' ]:
            self.legacy = True
        if typ.name in [ 'CAST_Oracle_Instance', 'CAST_SQL_Instance' ]:
            self.databaseType = 'ORACLE'
        else:
            self.databaseType = 'TSQL'
        
    def get_owners(self, is_sorted=False):
        """
        Get all the schemas of the database.
        
        :rtype: iterable of :class:`cast.application.DatabaseOwner`
        
        """ 
        self.load_children(None, is_sorted)
        
        owners = []
        try:
            owners.extend([ child for child in self.children if child.type.inherit_from('CAST_SQL_OwnerContainer') ])
            owners.extend([ child for child in self.children if child.type.inherit_from('SQL_SCHEMA') ])
            owners.extend([ child for child in self.children if child.type.inherit_from('CAST_SQL_Schema') ])
        except:
            try:
                owners.extend([ child for child in self.children if child.type.inherit_from('SQL_SCHEMA') ])
                owners.extend([ child for child in self.children if child.type.inherit_from('CAST_SQL_Schema') ])
            except:
                pass
        
        owners.extend([ child for child in self.children if child.type.inherit_from('UDBSCHEMA') ])
            
        return owners

    def __repr__(self):
        return 'Database(%s, %s)' % (self.get_name(), self.get_type())


class Project(Database):
    """
    A particular object that is the result of an Analysis Unit
    
    @todo:
    - get_path on csproj
    
    """
    def __init__(self, kb, identifier, name, typ, additional_values=None):
        Database.__init__(self, kb, identifier, name, typ, additional_values)
        self._dependent_projects = []
        self._depends_on = []

    def get_objects(self, internal=True, external=False):
        """
        Return a iterable collection of all the objects of the project
        
        :rtype: list of :class:`cast.application.Object`
        """
        return self.kb._get_objects([self.id], internal, external)
    
    def objects(self):
        """
        return a query for all the objects of this project.
        :rtype: :class:`cast.application.ObjectQuery`
        
        .. versionadded:: 1.5.9
        """
        
        return self.application.objects().in_projects([self])

    def __repr__(self):
        return 'Project(%s, %s)' % (self.get_name(), self.get_type())




def create_link(link_type, caller, callee, bookmark=None):
    """
    Creates a link between two objects.

    Only accessible in one specific event : end_application; will warn and skip.

    :param str link_type: name of the link type
    :param cast.application.Object caller: source of the link 
    :param cast.application.Object callee: destination of the link 
    :param cast.application.Bookmark bookmark: position of the link 

    :rtype: list of :class:`cast.application.create_link.AMTLink`
    """
    class AMTLink(KnowledgeBaseElement):
        """
        A link created by create_link.
        """
        def __init__(self, identifier, application):
            self.__id = identifier
            self.__application = application
            self.kb = application.kb
        
        def save_property(self, prop, value):
            """
            Save a property on current link.
            
            :param prop: the property to save. Either a string for the fullname of the property or an integer for the property id. 
            :param value: the value to set, either a integer, a string or a list of those
    
            The current plugin needs no declaration at all for this.  
            """
            
            _prop = self._convert_into_property(prop)
            
            if type(value) is list:
                for v in value:
                    self.__application._get_amt_saver().add_property(self.__id, _prop, v)
            else:
                self.__application._get_amt_saver().add_property(self.__id, _prop, value)
                
        def mark_as_not_sure(self):
            """
            Indicate that the link is not really certain. This link may then be
            validated or not through Dynamic Link Manager calibration tool.
            """
            self.save_property('physicalLink.ignorable', 1)

        def add_bookmark(self, bookmark):
            """
            Add a bookmark on the link.
            
            :param cast.application.Bookmark bookmark: additional position of the link
            
            Any number of bookmarks can be added.
            """
            self.__application._get_amt_saver().add_link_bookmark(self.__id, bookmark)

    try:
        # not 'patchable' so import from 'real one'
        from cast.application.internal import get_current_event
        
        # get the step and check...
        if get_current_event() and get_current_event() != 'end_application':
            logging.warning('create_link is only authorized during end_application_create_objects, end_application : skipping')
            return
    except ImportError:
        # caip version < 8.3 : get_current_event does not exists
        # but as we are in the correct event, we can create link
        pass
    
    application = cast.application.internal.get_current_application()
    
    # handling of CustomObjects
    
    # here is_instance does not work due to 'patching'
    if type(caller).__name__ == 'CustomObject':
        # take the id for this case
        caller = caller._id
        if not caller:
            # not saved --> error
            raise RuntimeError('create_link : CustomObject caller must be saved')
    if type(callee).__name__ == 'CustomObject':
        callee = callee._id
        if not callee:
            # not saved --> error
            raise RuntimeError('create_link : CustomObject callee must be saved')
    
    return AMTLink(application._get_link_saver().add_link(link_type, caller, callee, bookmark), application)


class CustomObject(KnowledgeBaseElement):
    """
    For creating new objects at application level.
    
    Bookmarks (position) cannot be saved for now.
    """
    def __init__(self):
        """
        Create a new custom object.
        """
        self.type = None
        self.name = ''
        self.external = False
        self.parent = None

        # assigned by user or auto calculated by save
        self.fullname = None
        self.guid = None

        # auto calculated
        self.children = []
        self._internal_fullname = None

        # given by save
        self._id = None
        
        self.application = cast.application.internal.get_current_application()
        self.kb = self.application.kb
        
        # authorization matrix
        try:
            # not 'patchable' so import from 'real one'
            from cast.application.internal import get_current_event
            
            # get the step and check...
            if get_current_event() and get_current_event() != 'end_application':
                raise RuntimeError('CustomObject is only authorized during end_application_create_objects')
        except ImportError:
            # caip version < 8.3 : get_current_event does not exists
            # but as we are in the correct event, we can create link
            pass
        
        current_phase = 'end_application' # default
        if hasattr(self.application, '_current_phase'):
            current_phase = getattr(self.application, '_current_phase')
        
        if current_phase != 'end_application_create_objects':
            raise RuntimeError('CustomObject is only authorized during end_application_create_objects')
        

    def set_name(self, name):
        """
        Set the object name.

        :param name: object's name. String
        """
        self.name = name

    def set_fullname(self, fullname):
        """
        Set the object's fullname. Optional, if not provided, save() will
        calculate one : <parent's full name>.<name>

        :param name: object's fullname. String
        """
        self.fullname = fullname

    def set_type(self, typename):
        """
        Set the type name.

        :param typename: Metamodel type name. String

        Type must respect some constraints for the object to be saved.
        ...

        """
        self.type = self.application.kb.metamodel.get_category(typename)

    def set_parent(self, parent):
        """
        Set the parent.

        :param parent: the parent of type cast.application.Object

        """
        if not isinstance(parent, (cast.application.Object, cast.application.CustomObject)):
            raise RuntimeError('CustomObject.set_parent : parent should be of type cast.application.Object or cast.application.CustomObject; here %s' % str(type(parent)))
        
        self.parent = parent

    def set_guid(self, guid):
        """
        Set the GUID of the object. Optional, if not provided, save() will
        calculate one : <typeid>?<fullname>

        Generally speaking one does not have to bother about guids.

        :param guid: object's GUID. String
        """
        self.guid = guid

    def get_fullname(self):
        
        return self.fullname

    def set_external(self):
        """
        Set object as external.
        
        .. versionadded:: 1.6.15
        """
        self.external = True

    def save(self):
        """
        Save the object to Analysis Service.

        Object require a non empty name, a saved parent and a type.
        The type must also follow constraints
        """
        if self._id:
            raise RuntimeError('CustomObject.save() : object already saved')
        
        if not self.name:
            raise RuntimeError('CustomObject.save() : name is mandatory')

        if not self.type:
            raise RuntimeError('CustomObject.save() : type is mandatory')

        if not self.parent:
            raise RuntimeError('CustomObject.save() : parent is mandatory')

        if type(self.parent).__name__ == 'CustomObject' and not self.parent._id:
            raise RuntimeError('CustomObject.save() : parent must have been saved')
        
        # calculate defaults
        if not self.fullname:
            
            self.fullname = self.parent.get_fullname() + '.' + self.name
        
        # calculate defaults
        if not self.guid:
            
            self.guid = self.type.get_name() + '?' + self.fullname
        
        saver = self.application._get_link_saver()
        # @type saver:cast.application.internal.amt_saver.Saver
        # or RawSaver in case of unit tests
        
        parent = self.parent
        if type(self.parent).__name__ == 'CustomObject':
            parent = self.parent._id
        
        self._id = saver.add_object(self.name, self.fullname, self.guid, self.type, parent, self.__get_ancestor(), self.external)

    def save_property(self, prop, value):
        """
        Save a property on an object.

        :param prop: the property to save. Either a string for the fullname of the property or an integer for the property id.    
        :param value: property value. String or Integer

        Object require to be saved.
        """
        if not self._id:
            raise RuntimeError('CustomObject.save_property() : object must have been saved')
        
        _prop = self._convert_into_property(prop)
        
        if self.kb.engine.dialect.name == 'sqlite':
            # in case of unit tests
            saver = self.application._get_raw_saver()
            # @type saver: cast.application.RawSaver
            self.id = self._id # for raw saver
            saver.add_property(self, _prop, value)
        else:
            
            if type(value) is list:
                for v in value:
                    self.application._get_amt_saver().add_property(self._id, _prop, v)
            else:
                self.application._get_amt_saver().add_property(self._id, _prop, value)


    def __get_ancestor(self):
        
        if type(self.parent).__name__ == 'CustomObject':
            return self.parent.__get_ancestor()
        else:
            return self.parent
                    


def publish_report(name, status, label, value, secondary_label=None, secondary_value=None, detail_report_path=None):
    """
    Publish a custom report that will be visible in CAST-MS.
    
    @param name: str
    @param status: one of 'OK', 'KO', 'Warning' or None
    @param label: str
    @param value: str
    @param secondary_label: str or None
    @param secondary_value: str or None
    @param detail_report_path: str or None
    
    Available in 8.3 and above.
    
    .. versionadded:: 1.5.12
    """
    from cast.application.internal import _add_report
    _add_report(name, status, label, value, secondary_label, secondary_value, detail_report_path)



#########################
## Queries on objects and links through method chaining API
## See for example : http://stackoverflow.com/questions/21785689/python-class-method-chaining


class PropertyLoader:
    
    def __init__(self, application):
        
        self.__application = application
    
    def _load_property(self, propety_or_properties):
        """
        Ask for loading of one or some properties.
        
        Note that loading one or several properties takes longer to perform the query.
        
        Has no effect when query is used in a ObjectQuery. 
        
        :param properties: str or int of list of those. 
        :rtype: :class:`cast.application.LinkQuery`
        """
        result = copy.copy(self)
        kb = self.__application.kb
        
        def _get_property(name_or_id):
            
            _type = type(name_or_id)
            
            if _type is str:
                return kb.metamodel.get_property(name=name_or_id)
            elif _type is int:
                return kb.metamodel.get_property(id=name_or_id)
                
            
        _properties = []
        if type(propety_or_properties) is list:
            for t in propety_or_properties:
                _properties.append(_get_property(t))
        else:
            _properties = [_get_property(propety_or_properties)]
        
        
        result._loaded_properties += _properties
        return result
        
    def _get_properties_query(self, not_sure=False):
        """
        Select.append_column()
        """
        
        kb = self.__application.kb
        
        kb._load_infsub_types()
        
        objdsc = reflect_table('ObjDsc', kb.metadata, kb.engine)

        objinf = reflect_table('ObjInf', kb.metadata, kb.engine)

        """
        @todo : 
        - multi lines strings...
        - multivalues
        """
        
        string_properties = [prop for prop in self._loaded_properties if prop.get_type() == 'string']
        integer_properties = [prop for prop in self._loaded_properties if prop.get_type() == 'integer']
        
        if not_sure:
            
            class ValidatedByProperty:
                def __init__(self):
                    self.inftyp = -1
                    self.infsubtyp = 0
            
            string_properties.append(ValidatedByProperty())
        
        select_dsc = None
        
        if string_properties:
            select_dsc = select([objdsc.c.idobj, objdsc.c.inftyp, objdsc.c.infsubtyp, objdsc.c.infval.label('string_value'), literal_column('null').label('int_value'), objdsc.c.blkno, objdsc.c.ordnum.label("ordnum")])
            select_dsc = select_dsc.where(or_((and_(objdsc.c.inftyp == prop.inftyp, 
                                                    objdsc.c.infsubtyp == prop.infsubtyp) for prop in string_properties)))
        
        select_inf = None
        if integer_properties:
        
            select_inf = select([objinf.c.idobj, objinf.c.inftyp, objinf.c.infsubtyp, literal_column('null').label('string_value'), objinf.c.infval.label('int_value'), objinf.c.blkno, literal_column('0').label("ordnum")])
            select_inf = select_inf.where(or_((and_(objinf.c.inftyp == prop.inftyp, 
                                                    objinf.c.infsubtyp == prop.infsubtyp) for prop in integer_properties)))
            
        # need one or both depending...
        properties = None
        
        if not select_dsc is None and not select_inf is None:
            properties = union(select_dsc, select_inf)
        elif not select_dsc is None:
            properties = select_dsc
        else:
            properties = select_inf
            
        return properties

    def _load_violations(self, propety_or_properties):
        """
        Ask for loading of one or some violations.
        
        Note that loading one or several violations takes longer to perform the query.
        
        Has no effect when query is used in a ObjectQuery. 
        
        :param properties: str or int of list of those. 
        :rtype: :class:`cast.application.LinkQuery`
        """
        result = copy.copy(self)
        kb = self.__application.kb
        
        def _get_property(name_or_id):
            
            _type = type(name_or_id)
            
            if _type is str:
                return kb.metamodel.get_property(name=name_or_id)
            elif _type is int:
                return kb.metamodel.get_property(id=name_or_id)
            else:
                return name_or_id
            
        _properties = []
        if type(propety_or_properties) is list:
            for t in propety_or_properties:
                _properties.append(_get_property(t))
        else:
            _properties = [_get_property(propety_or_properties)]
        
        
        result._loaded_violations += _properties
        return result
    
    def _get_violations_query(self):
        """

        """
        kb = self.__application.kb
        
        violations = reflect_table('DSS_Positions', kb.metadata, kb.engine) 

        query = select([violations.c.objectid,
                        violations.c.positionid,
                        violations.c.positionindex,
                        violations.c.propertyid,
                        violations.c.linestart,
                        violations.c.colstart,
                        violations.c.lineend,
                        violations.c.colend,
                        kb.Keys.c.idkey,
                        kb.RefPath.c.path,
                        kb.Keys.c.keynam,
                        kb.Keys.c.objtyp,
                        kb.ObjFulNam.c.fullname,
                        ]).select_from(violations.join(kb.ObjFilRef, 
                                                       kb.ObjFilRef.c.idobj == violations.c.sourceid,
                                                       isouter=True).join(kb.RefPath,
                                                                          kb.RefPath.c.idfilref == kb.ObjFilRef.c.idfilref,
                                                                          isouter=True).join(kb.Keys,
                                                                                             kb.Keys.c.idkey == violations.c.sourceid,
                                                                                             isouter=True).join(kb.ObjFulNam,
                                                                                                                kb.Keys.c.idkey == kb.ObjFulNam.c.idobj,
                                                                                                                isouter=True))
        
        # for given properties
        query = query.where(violations.c.propertyid.in_([prop.id for prop in self._loaded_violations]))
        query = query.where(violations.c.objectid.in_(self._get_object_query()))
        
        # order matters for grouping elements
        query = query.order_by(violations.c.objectid, violations.c.propertyid, violations.c.positionid, violations.c.positionindex)
        
        return query
    

class ObjectQuery(PropertyLoader):
    """
    A query on objects.
    
    Follow the method chaining pattern.
    """
    def __init__(self, application=None):
        """
        :param application: the application we want to get all the objects 
        :param object_query: an ObjectQuery to clone
        """
        PropertyLoader.__init__(self, application)
        self.__application = None
        
        self.__select_internal = False
        self.__select_external = False
        
        # things to build the final query
        self.__project_ids = None
        self.__types = set()
        self.__filter_on_types = False
        # explain : 
        #
        self.__modifiers_cpp = []
        self.__virtual_dotnet = None
        self.__modifiers_jad = []
        
        self.__is_caller_queries = []
        self.__is_callee_queries = []
        
        # additional filter (optional) : usefull to restrict initial object set
        self.__additional_filter = None
        self.__accept_projects = False
        self.__reject_objects = False
                
        # properties to load
        self._loaded_properties = []
        # violations to load
        self._loaded_violations = []
        
        self.__violation_iterator = None
        self.__last_read_violation = None
        
        # all object of application
        self.__application = application
        self.__project_ids = application.projects_ids
        
        self.__used_in_project = False
        
        self.__set_filters = []
        self.__not_set_filters = []
        
        self.__not_set_queries = []
        
        # for in_query(...)
        self.__in_query_filters = []
        
        # for load_positions
        self.__load_bookmark = False
        
        self.__bookmark_iterator = None
        self.__last_read_bookmark = None
        
        
    
    def has_type(self, _types_or_categories):
        """
        Filter and return a query that takes only objects of some certain types or categories
        
            .has_type(['Java', 'C++']) : all types inheriting from Java or C++
        
            .has_type('Java').has_type('Method') all types inheriting from Java and Method
        
        :param _types_or_categories: category name, id or list of those. If a list is provided, it will act as a logical or.
        :rtype: :class:`cast.application.ObjectQuery`
        """
        return self.__filter_type(_types_or_categories)

    def not_has_type(self, _types_or_categories):
        """
        Filter and return a query that takes only objects that do not have certain types or categories
        
            .not_has_type(['Java', 'C++']) : all types except those inheriting from Java or C++
        
            .not_has_type('Java').not_has_type('Method') all types not inheriting from Java and not inheriting from Method
        
        :param _types_or_categories: category name, id or list of those. If a list is provided, it will act as a logical or.
        :rtype: :class:`cast.application.ObjectQuery`
        
        .. versionadded:: 1.5.9
        """
        return self.__filter_type(_types_or_categories, inclusive=False)

    def __filter_type(self, _types_or_categories, inclusive=True):
        result = copy.copy(self)
        
        kb = self.__application.kb
        
        def _get_category(name_or_id):
            
            _type = type(name_or_id)
            
            if _type is str:
                return kb.metamodel.get_category(name=name_or_id)
            elif _type is int:
                return kb.metamodel.get_category(id=name_or_id)
            elif _type.__name__ in ('Type', 'Category'):
                return name_or_id
            
        types = []
        if type(_types_or_categories) in [list, set]:
            for t in _types_or_categories:
                types += _get_category(t).get_sub_types()
        else:
            types = _get_category(_types_or_categories).get_sub_types()

        type_ids = [t.id for t in types]

        # new mode
        if not result.__types:
            # default is all persistent types
            result.__types = set([typ.id for typ in kb.metamodel.get_category(id=1023).get_sub_types()])
        
        # intersect with previous
        if inclusive:
            result.__types = result.__types & set(type_ids)
        else:
            # remove the types
            result.__types = result.__types - set(type_ids)
            
        result.__filter_on_types = True

        return result

    def load_property(self, propety_or_properties):
        """
        Ask for loading of one or some properties.
        
        Note that loading one or several properties takes longer to perform the query.
        
        Has no effect when query is used as sub query of a LinkQuery. 
        
        :param properties: str or int of list of those. 
        :rtype: :class:`cast.application.ObjectQuery`
        """
        return self._load_property(propety_or_properties)

    def load_violations(self, propety_or_properties):
        """
        Ask for loading of one or some violations.
        
        Note that loading one or several violations takes longer to perform the query.
        
        Has no effect when query is used as sub query of a LinkQuery. 
        
        :param properties: str or int of list of those. 
        :rtype: :class:`cast.application.ObjectQuery`
        
        .. versionadded:: 1.5.7
        """
        
        return self._load_violations(propety_or_properties)

    def load_positions(self):
        """
        Force loading of positions of object.
        
        .. versionadded:: 1.5.22
        
        :rtype: :class:`cast.application.ObjectQuery`
        """
        result = copy.copy(self)
        result.__load_bookmark = True
        return result

    def is_internal(self):
        """
        Filter internal objects.
        
        .. versionadded:: 1.5.4
        """
        if self.__select_external:
            raise RuntimeError('is_internal and is_external are mutually exclusive')
        
        result = copy.copy(self)
        result.__select_internal = True
        return result
        
        
    def is_external(self):
        """
        Filter internal objects.
        
        .. versionadded:: 1.5.4
        """
        if self.__select_internal:
            raise RuntimeError('is_internal and is_external are mutually exclusive')

        result = copy.copy(self)
        result.__select_external = True
        return result

    def is_public(self):
        """
        Filter and return a query that takes only objects that are public.
        
        Works for C++, Java, .Net, ABAP only and will only return object of those types.

        :rtype: :class:`cast.application.ObjectQuery`
        """
        return self.__internal(8, 2)
        
    def is_private(self):
        """
        Filter and return a query that takes only objects that are private.

        Works for C++, Java, .Net, ABAP only and will only return object of those types.

        :rtype: :class:`cast.application.ObjectQuery`
        """
        return self.__internal(32, 8)

    def is_protected(self):
        """
        Filter and return a query that takes only objects that are protected.

        Works for C++, Java, .Net, ABAP only and will only return object of those types.

        :rtype: :class:`cast.application.ObjectQuery`
        """
        return self.__internal(16, 4)

    def is_static(self):
        """
        Filter and return a query that takes only objects that are static.

        Works for C++, Java, .Net, ABAP only and will only return object of those types.

        :rtype: :class:`cast.application.ObjectQuery`
        """
        return self.__internal(4, 16)

    def is_virtual(self):
        """
        Filter and return a query that takes only objects that uses late binding.
        So 
        
        * virtual, virtual by inheritance C+ methods
        * virtual, overrides and interface .Net methods
        
        Works for C++, .Net only and will only return object of those types.

        :rtype: :class:`cast.application.ObjectQuery`
        """
        
        result = copy.copy(self)

        # new mode 
        result.__modifiers_cpp.append(1024+8388608)
        result.__virtual_dotnet = True
        
        # restrict to methods
        result = result.has_type('APM Methods')
        # restrict to C++/dotnet
        result = result.has_type(['CAST_DotNet_DotNet', 'C/C++'])
        
        return result

    def is_abstract(self):
        """
        Filter and return a query that takes only objects that are abstract. I.e. with empty implementation and 'virtual'.

        Works for C++, Java, .Net, ABAP only and will only return object of those types.

        :rtype: :class:`cast.application.ObjectQuery`
        """
        return self.__internal(128, 32)
        
    def is_caller(self, link_query):
        """
        Objects that are caller of a given link query.
        
        :param linkquery: :class:`cast.application.LinkQuery`
        :rtype: :class:`cast.application.ObjectQuery`
        """
        if type(link_query) == LinkQuery:
            # case for object query : restrict to idkey
            result = copy.copy(self)
            result.__is_caller_queries.append(link_query)
            return result
        else:
            raise RuntimeError("Unsupported type")
    
    def is_callee(self, link_query):
        """
        Objects that are callee of a given link query.
        
        :param linkquery: :class:`cast.application.LinkQuery`
        :rtype: :class:`cast.application.ObjectQuery`
        """
    
        if type(link_query) == LinkQuery:
            # case for object query : restrict to idkey
            result = copy.copy(self)
            result.__is_callee_queries.append(link_query)
            return result
        else:
            raise RuntimeError("Unsupported type")
    
    def is_dbms(self):
        """
        Objects that come from a database.

        :rtype: :class:`cast.application.ObjectQuery`
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_dbms())
    
    def is_directory(self):
        """
        Objects that are directories.

        :rtype: :class:`cast.application.ObjectQuery`
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_directory())
    
    def is_program(self):
        """
        Objects that are programs.

        :rtype: :class:`cast.application.ObjectQuery`
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_program())
    
    def is_class(self):
        """
        Objects that are class or interfaces.

        :rtype: :class:`cast.application.ObjectQuery`
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_class())
    
    def is_executable(self):
        """
        Objects that are executable : function, method, trigger, ...
        But not programs.

        :rtype: :class:`cast.application.ObjectQuery`
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_executable())
    
    def is_package(self):
        """
        Objects that are package, namespace, module, schema, etc...

        :rtype: :class:`cast.application.ObjectQuery`
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_package())
    
    def is_variable(self):
        """
        Objects that are variable, field, member variable, something that can receive an assignment.

        :rtype: :class:`cast.application.ObjectQuery`
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_variable())

    def is_table(self):
        """
        Objects that are table or view.

        :rtype: :class:`cast.application.ObjectQuery`
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_table())
    
    def is_index(self):
        """
        Objects that are index.

        :rtype: :class:`cast.application.ObjectQuery`
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_index())
    
    def is_foreignkey(self):
        """
        Objects that are foreign key.

        :rtype: :class:`cast.application.ObjectQuery`
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_foreignkey())

    def is_web_service_operation(self):
        """
        Objects that are web service handler server side REST (get, post, ...) or SOAP.

        :rtype: :class:`cast.application.ObjectQuery`
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_web_service_operation())

    def is_web_service_call(self):
        """
        Objects that are web service call (client side).

        :rtype: :class:`cast.application.ObjectQuery`
        
        .. versionadded:: 1.5.9
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_web_service_call())

    def is_rest_web_service_call(self):
        """
        True when object is a REST call (client side).

        .. versionadded:: 1.6.23
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_rest_web_service_call())

    def is_rest_web_service_receive(self):
        """
        True when object is a web REST receive (server side).

        .. versionadded:: 1.6.23
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_rest_web_service_receive())

    def is_soap_web_service_call(self):
        """
        True when object is a SOAP call (client side).

        .. versionadded:: 1.6.23
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_soap_web_service_call())

    def is_soap_web_service_receive(self):
        """
        True when object is a SOAP receive (server side).

        .. versionadded:: 1.6.23
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_soap_web_service_receive())
        
    def is_nosql_collection(self):
        """
        Objects that are nosql collections (similar to table).

        :rtype: :class:`cast.application.ObjectQuery`
        
        .. versionadded:: 1.6.7
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_nosql_collection())

    def is_form(self):
        """
        Objects that are forms, controls and events.

        :rtype: :class:`cast.application.ObjectQuery`
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_form())
    
    def is_program_call(self):
        """
        Objects that are call to program.

        :rtype: :class:`cast.application.ObjectQuery`
        
        .. versionadded:: 1.6.14
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_program_call())

    def is_bean(self):
        """
        Objects that are beans.

        :rtype: :class:`cast.application.ObjectQuery`
        
        .. versionadded:: 1.6.14
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_bean())

    def is_cloud_function(self):
        """
        Objects that are cloud functions.

        :rtype: :class:`cast.application.ObjectQuery`
        
        .. versionadded:: 1.6.14
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_cloud_function())

    def is_cloud_function_call(self):
        """
        Objects that are calls to cloud function.

        :rtype: :class:`cast.application.ObjectQuery`
        
        .. versionadded:: 1.6.14
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_cloud_function_call())
    
    def is_rpc_receive(self):
        """
        Objects that are receiving of RPC call.

        :rtype: :class:`cast.application.ObjectQuery`
        
        .. versionadded:: 1.6.14
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_rpc_receive())
    
    def is_rpc_call(self):
        """
        Objects that are call to RPC.

        :rtype: :class:`cast.application.ObjectQuery`
        
        .. versionadded:: 1.6.14
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_rpc_call())
    
    def is_message_receive(self):
        """
        Objects that are receiving of message.

        :rtype: :class:`cast.application.ObjectQuery`
        
        .. versionadded:: 1.6.14
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_message_receive())
    
    def is_message_send(self):
        """
        Objects that are send of message.

        :rtype: :class:`cast.application.ObjectQuery`
        
        .. versionadded:: 1.6.14
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_message_send())

    def is_query(self):
        """
        Objects that are query.

        :rtype: :class:`cast.application.ObjectQuery`
        
        .. versionadded:: 1.6.18
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_query())
    
    def is_entity(self):
        """
        Objects that are ORM entity.

        :rtype: :class:`cast.application.ObjectQuery`
        
        .. versionadded:: 1.6.18
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_entity())
    
    def is_entity_operation(self):
        """
        Objects that are ORM entity operation.

        :rtype: :class:`cast.application.ObjectQuery`
        
        .. versionadded:: 1.6.18
        """
        return self.has_type(self.__application.kb._get_metamodel_wrapper().get_entity_operation())
    
    def in_set(self, set_name_or_id_or_list):
        """
        Filter objects that are part of a given set.
        
            .in_set(['set1', 'set2']) : all objects in set or set2
        
            .in_set('set1').in_set('set2') all objects in set and set2
        
        :param set_name_or_id_or_list: set name, id or list of those. If a list is provided, it will act as a logical or.
        :rtype: :class:`cast.application.ObjectQuery`
        
        .. versionadded:: 1.5.9
        """
        result = copy.copy(self)
        
        result.__set_filters.append(set_name_or_id_or_list)
        
        return result

    def not_in_set(self, set_name_or_id_or_list):
        """
        Filter objects that are not_part of a given set.
        
            .not_in_set(['set1', 'set2']) : all objects not in set or set2
        
            .not_in_set('set1').not_in_set('set2') all objects not in set and not set2
        
        :param set_name_or_id_or_list: set name, id or list of those. If a list is provided, it will act as a logical or.
        :rtype: :class:`cast.application.ObjectQuery`
        
        .. versionadded:: 1.5.9
        """
        result = copy.copy(self)
        
        result.__not_set_filters.append(set_name_or_id_or_list)
        
        return result

    def not_in(self, object_query):
        """
        Filter objects that are not_part of a given query.
        
        
        :param object_query: `cast.application.ObjectQuery`
        :rtype: :class:`cast.application.ObjectQuery`
        
        .. versionadded:: 1.5.9
        """
        result = copy.copy(self)
        
        result.__not_set_queries.append(object_query)
        
        return result


    def in_projects(self, projects):
        """
        Filter objects that are part of a given set.
        
            .in_projects([p1, p2]) : all objects in p1 or p2
        
            .in_projects([p1]).in_projects([p2]) all objects in p1 and p2
        
        :param projects: list of `cast.application.Project`.
        :rtype: :class:`cast.application.ObjectQuery`
        
        .. versionadded:: 1.5.9
        """
        result = copy.copy(self)

        # filter out...
        result.__project_ids = list(set(result.__project_ids) & set([p.id for p in projects]))
        result.__used_in_project = True # marker
        return result
    
    def in_query(self, sqlalchemyquery):
        """
        Filter objects that are part of a given query.
        
        :param sqlalchemyquery: sqlalchemy.Query 
            a query that selects idkey
        :rtype: :class:`cast.application.ObjectQuery`

        .. versionadded:: 1.5.13
        """
        result = copy.copy(self)

        # filter out...
        result.__in_query_filters.append(sqlalchemyquery)
        
        return result
 
    def _save_as(self, set_name):
        """
        Save content of the query as a set with name set_name
        If the set already exists, owerwrite it.
        
        .. versionadded:: 1.5.9
        """
        kb = self.__application.kb
        kb._ensure_additional_tables()
        
        # get the id
        subset_id = None
        query = select([kb.pmc_subsets.c.subset_id]).where(kb.pmc_subsets.c.subset_name == set_name)
        for o in kb._execute_sqlalchemyquery2(query):
            subset_id = o[0]
            
        if not subset_id:
            # create a new one
            query = select([func.max(kb.pmc_subsets.c.subset_id)])
            result = kb.engine.execute(query)
            max_id = result.fetchone()[0]
            if max_id:
                subset_id = max_id + 1
            else:
                subset_id = 1
            ins = kb.pmc_subsets.insert().values(subset_name = set_name, subset_id=subset_id)
            result = kb.engine.execute(ins)
            
        else:
                      
            # clear the set
            d = kb.pmc_subset_objects.delete().where(kb.pmc_subset_objects.c.subset_id==subset_id)
            kb.engine.execute(d)
        
        # insertion
        query = select([literal_column(str(subset_id)), kb.Keys.c.idkey])
        query = self._filter_query(query, self.__application.kb.Keys)
        
        ins = kb.pmc_subset_objects.insert().from_select(['subset_id', 'object_id'], query)
        kb.engine.execute(ins)
        
        return subset_id
    
    def count(self):
        """
        Returns the number of objects in this query.
        
        Execute a count(*) ...
        
        .. versionadded:: 1.5.9
        """
        query = select([func.count()]).select_from(self._get_object_query().alias('o'))
        for result in self.__application.kb.engine.execute(query):
            return result[0]
    
    
    def __get_violations(self, idkey):
        """
        Return all lines read for a given idkey
        """
        # will contain all lines concerning current object
        lines = []
#         print('---- looking for ', idkey, self.__last_read_violation)
        if self.__last_read_violation:
            
            # last read line
            if idkey ==  self.__last_read_violation[0]:
                lines.append(self.__last_read_violation)
                self.__last_read_violation = None
            else:
                return []
            
        # read the rest ...
        if not self.__violation_iterator.closed:
            
            for line in self.__violation_iterator:
                
                if line[0] != idkey:
                    
                    self.__last_read_violation = line
                    return lines
                
                lines.append(line)
        
        return lines
    
    def __get_bookmarks(self, idkey):
        
        lines = []
        
        if self.__last_read_bookmark:
            
            if idkey ==  self.__last_read_bookmark[0]:
                lines.append(self.__last_read_bookmark)
                self.__last_read_bookmark = None
            else:
                return []
        
        # read the rest ...
        if not self.__bookmark_iterator.closed:
            
            for line in self.__bookmark_iterator:
                
                if line[0] != idkey:
                    
                    self.__last_read_bookmark = line
                    return lines
                
                lines.append(line)
        
        return lines
    
    def __create_object(self, idkey, objtyp, name, fullname):
        
        kb = self.__application.kb
        result = kb._build_object_wrapper(idkey, objtyp, name, {'application':self.__application, 'fullname':fullname}) 
        
        if self.__load_bookmark:
            
            result.positions = []
            
            for line in self.__get_bookmarks(idkey):
                
                
                
                
                if line['file_type']:
                    
                    bookmark = Bookmark(kb._build_object_wrapper(line['file_id'],
                                                                 line['file_type'],
                                                                 line['file_name'],
                                                                 {'application':self.__application,
                                                                  'path':line['file_path']
                                                                 }), 
                                        line['begin_line'], 
                                        line['begin_column'], 
                                        line['end_line'], 
                                        line['end_column'])
                    
                    result.positions.append(bookmark)
                else:
                    # wsdl bookmark files are not stored the same way
                    if objtyp == 366 and fullname and fullname.startswith('['):
                        bookmark = Bookmark(kb._build_object_wrapper(idkey,
                                                                     objtyp,
                                                                     name,
                                                                     {'application':self.__application,
                                                                      'path':fullname[1:-1]
                                                                     }), 
                                            line['begin_line'], 
                                            line['begin_column'], 
                                            line['end_line'], 
                                            line['end_column'])
                        
                        result.positions.append(bookmark)
        
        if self._loaded_violations:
            # sub-query loading
            lines = self.__get_violations(idkey)
            
            current_position_id = None
            current_violation = None
            current_property = None
            
            setattr(result, '_violations', {})
            
            # process lines to feed object    
            for line in lines:
                
                position_id = line[1]
                
                if current_position_id != position_id:
                    # new violation
                    if current_violation:
                        # add it on object
                        if not current_property in result._violations:
                            result._violations[current_property] = []
                        result._violations[current_property].append(current_violation)
                    
                    current_position_id = position_id
                    current_property = kb.metamodel.get_property(id=line[3])
                    current_violation = []
                
                _file = kb._build_object_wrapper(line[8], 
                                                 line[11],
                                                 line[10],
                                                 {'path':line[9],
                                                  'fullname':line[12],
                                                  'application':self.__application
                                                  })
                
                bookmark = Bookmark(_file, 
                                    line[4],
                                    line[5],
                                    line[6],
                                    line[7])
                
                if not current_violation:
                    current_violation = (current_property, bookmark, [])
                else:
                    current_violation[2].append(bookmark)
                
            # last one 
            if current_violation:
                # add it on object
                if not current_property in result._violations:
                    result._violations[current_property] = []
                
                result._violations[current_property].append(current_violation)
            
            setattr(result, '_loaded_violations', True)
            
        return result
        
     
    def __iter__(self):
        """
        Execute query and return an iterator on objects so that we can do for loop on self.
        """
        
        # new mode
        kb = self.__application.kb
        
        query = kb._get_select_object()
        
        query = self._filter_query(query, kb.Keys)
        
        
        if self.__load_bookmark:
            
            # create a separate query for loading bookmarks
            file_alias = alias(kb.Keys)
            
            myjoin = kb.ObjPos.join(kb.ObjFilRef, 
                                             kb.ObjFilRef.c.idobj == kb.ObjPos.c.idobjref,
                                             isouter=True).join(kb.RefPath,
                                                                kb.RefPath.c.idfilref == kb.ObjFilRef.c.idfilref,
                                                                isouter=True).join(file_alias,
                                                                                   kb.ObjFilRef.c.idobj == file_alias.c.idkey,
                                                                                   isouter=True)
            
            
            bookmark_query = select([kb.ObjPos.c.idobj.label('object_id'),
                                     kb.ObjPos.c.info1.label('begin_line'),
                                     kb.ObjPos.c.info2.label('begin_column'),
                                     kb.ObjPos.c.info3.label('end_line'),
                                     kb.ObjPos.c.info4.label('end_column'),
                                     kb.ObjFilRef.c.idobj.label('file_id'),
                                     kb.RefPath.c.path.label('file_path'),
                                     file_alias.c.objtyp.label('file_type'),
                                     file_alias.c.keynam.label('file_name')
                                     ]).select_from(myjoin).where(kb.ObjPos.c.idobj.in_(self._get_object_query()))
            
            bookmark_query = bookmark_query.order_by(kb.ObjPos.c.idobj.asc())
            
            self.__bookmark_iterator = kb.engine.execute(bookmark_query)
        
        
        # handling of sub query for violations        
        if self._loaded_violations:
        
            violation_query = self._get_violations_query()
            self.__violation_iterator = kb.engine.execute(violation_query)
        
        if not self._loaded_properties:
            
            for o in kb._execute_sqlalchemyquery2(query):
                yield self.__create_object(o[0], o[1], o[2], o[3])
             
        else:
             
            query = self._load_properties(query)
            
            # this cursor returns several lines for the same object 
            current_object = None
            
            current_inftyp = None
            current_infsubtyp = None
            current_blocknumber = None
            
            for line in kb.engine.execute(query):
                
#                 print(line)
                current_object_id = current_object.id if current_object else None
                object_id = line['idkey']
     
                # true when we have changed object
                is_new_object_line = object_id != current_object_id

                # add property to current object
                inftyp = line['inftyp']
                infsubtyp = line['infsubtyp']
                prop = kb._search_property(inftyp, infsubtyp)
                
                block_number = line['blkno'] # multivalued
                  
                if is_new_object_line:
                    # create new object
                    old_object = current_object
                    
                    current_object = self.__create_object(line['idkey'], line['objtyp'], line['keynam'], line['fullname'])
#                     current_object = kb._build_object_wrapper(line['idkey'], line['objtyp'], line['keynam'], {'application':self.__application, 'fullname':line['fullname']})
                    
                    # reset
#                     print("reset")
                    current_inftyp = inftyp
                    current_infsubtyp = infsubtyp
                    current_blocknumber = None
                    
                    for _prop in self._loaded_properties:
                        current_object._declare_property_loaded(_prop)
                    
                      
                
                # handle large string values/multivalued 
                if prop:
                    string_value = line['string_value']
                    int_value = line['int_value']
                    
                    value = int_value if not int_value is None else string_value
                    
#                     print(current_inftyp, inftyp)
#                     print(current_infsubtyp, infsubtyp)
#                     print(current_blocknumber, block_number)
                    
                    if current_inftyp == inftyp and current_infsubtyp == infsubtyp and current_blocknumber == block_number:
#                         print("_concat_property_value", prop, value)
                        # concat value
                        current_object._concat_property_value(prop, value)
                    else:
                        # multi value
#                         print("_add_property_value", prop, value)
                        current_object._add_property_value(prop, value)
                    
                    
                else:
                    # object has no property at all : still put it empty
                    if not hasattr(current_object, '_properties'):
                        setattr(current_object, '_properties', {})
                
                # set
                current_inftyp = inftyp
                current_infsubtyp = infsubtyp
                current_blocknumber = block_number
                
                # return the previous object when finished
                if is_new_object_line and old_object:
                    yield old_object
             
            # the last one
            if current_object:
                yield current_object
        

    def _get_object_query(self):
        """
        Return a query usable for idkey in (...)
        """
        
        query = select([self.__application.kb.Keys.c.idkey])
        query = self._filter_query(query, self.__application.kb.Keys)
        
        return query
        
    def _filter_query(self, query, keys_table):
        """
        Add filters on a query on Keys
        
        Uses only key table
        """
        kb = self.__application.kb
        
        # projects        
        is_in_project = kb._get_project_filter(self.__application if not self.__used_in_project else self.__project_ids, # TONS OF PROJECTS 
                                               internal=self.__select_internal, 
                                               external=self.__select_external)
        
        if not self.__reject_objects:
            query = query.where(keys_table.c.idkey.in_(is_in_project))
        
        if not self.__accept_projects:
            query = query.where(~keys_table.c.idkey.in_(_get_in_project(self.__application) if not self.__used_in_project else self.__project_ids # TONS OF PROJECTS
                                                        ))
        
        # types is non empty
        if self.__filter_on_types:
            if not self.__types:
                # filter on types but empty so not satisfiable
                query = query.where(False)
                return query
            
            query = query.where(keys_table.c.objtyp.in_(self.__types))
        
        if self.__modifiers_cpp:
            # modifiers
            
            cpp_types =    set([typ.id for typ in kb.metamodel.get_category(id=140009).get_sub_types()]) & set([typ.id for typ in kb.metamodel.get_category(id=1023).get_sub_types()])
            dotnet_types = set([typ.id for typ in kb.metamodel.get_category(id=138102).get_sub_types()]) & set([typ.id for typ in kb.metamodel.get_category(id=1023).get_sub_types()])
            java_types =   set([typ.id for typ in kb.metamodel.get_category(id=6009).get_sub_types()]) & set([typ.id for typ in kb.metamodel.get_category(id=1023).get_sub_types()])
            abap_types =   set([typ.id for typ in kb.metamodel.get_category(id=6021).get_sub_types()]) & set([typ.id for typ in kb.metamodel.get_category(id=1023).get_sub_types()])
            
            others = dotnet_types | java_types | abap_types
            
            # reduce quantity of allowed types
            if self.__types:
                cpp_types = cpp_types & self.__types
                others = others & self.__types
                dotnet_types = dotnet_types & self.__types
                
            # create final filter
            
            # each techno has it's own bitfield (in fact C++ is different than the others)
            # so for C++ we : 
            # get the C++ types compatible with the .has_type(...) requirement
            # and build a filter : 
            #    Keys.keyprop & bitfield != 0 and Keys.objtyp in (<c++ types allowed>)
            # we do this for dotnet/java/abap
            # then we do a big or on those filters
            
            _filters = []
            
            if cpp_types and self.__modifiers_cpp:
                _filter_cpp = and_((bitand(keys_table.c.keyprop, x, kb.engine) != 0 for x in self.__modifiers_cpp))
                _filter_cpp = and_(_filter_cpp, keys_table.c.objtyp.in_(cpp_types))
                _filters.append(_filter_cpp)
                
            if others and self.__modifiers_jad:
                _filter_other = and_((bitand(keys_table.c.keyprop, x, kb.engine) != 0 for x in self.__modifiers_jad))
                _filter_other = and_(_filter_other, keys_table.c.objtyp.in_(others))
                _filters.append(_filter_other)
            
            if dotnet_types and self.__virtual_dotnet:
                # special for is_virtual dotnet
                # more complex because of interfaces
                kb._ensure_additional_tables()
                
                # works for 7.3, for 8.0 ? 
                interfaces = select([kb.Keys.c.idkey]).where(kb.Keys.c.objtyp.in_(set([typ.id for typ in kb.metamodel.get_category(id=137034).get_sub_types()])))
                
                children_of_interface = select([kb.KeyPar.c.idkey]).where(kb.KeyPar.c.idparent.in_(interfaces))
                
                _filter_dotnet = or_(bitand(keys_table.c.keyprop, 32768+262144, kb.engine) != 0,
                                     keys_table.c.idkey.in_(children_of_interface)
                                     )
                _filter_dotnet = and_(_filter_dotnet, keys_table.c.objtyp.in_(dotnet_types))
                _filters.append(_filter_dotnet)
            
            if _filters:
                # finally an or of all those
                _filter = or_((f for f in _filters))
                query = query.where(_filter)
            else:
                # if at the end we have empty filter then it is not satisfiable
                # e.g. is_virtual().has_type('Java')
                query = query.where(False)
                
            
        for caller_query in self.__is_caller_queries:
            
            query = query.where(keys_table.c.idkey.in_(caller_query._get_object_query(as_caller=True)))
            
        for callee_query in self.__is_callee_queries:
            
            query = query.where(keys_table.c.idkey.in_(callee_query._get_object_query(as_caller=False)))
        
        if not self.__additional_filter is None:
            query = query.where(self.__additional_filter)
        
        # sets filter
        # @todo optim when no other filter and when _get_object_query ?
        def create_query_or_set(sets):
            """ create the or when list of set is provided """
            subset_id_filters = [s for s in sets if type(s) is int]
            subset_name_filters = [s for s in sets if type(s) is str]
        
            subset_name_query = select([kb.pmc_subsets.c.subset_id]).where(kb.pmc_subsets.c.subset_name.in_(subset_name_filters))
            
            subset_query = select([kb.pmc_subset_objects.c.object_id])
            if subset_id_filters and subset_name_filters:
                subset_query = subset_query.where(or_(kb.pmc_subset_objects.c.subset_id.in_(subset_id_filters),
                                                      kb.pmc_subset_objects.c.subset_id.in_(subset_name_query)))
            elif subset_id_filters:
                subset_query = subset_query.where(kb.pmc_subset_objects.c.subset_id.in_(subset_id_filters))
            elif subset_name_filters:
                subset_query = subset_query.where(kb.pmc_subset_objects.c.subset_id.in_(subset_name_query))
            return subset_query 
            
        for s in self.__set_filters:
            if type(s) is list:
                subset_query = create_query_or_set(s)
                query = query.where(keys_table.c.idkey.in_(subset_query))
            if type(s) is int:
                subset_query = select([kb.pmc_subset_objects.c.object_id]).where(kb.pmc_subset_objects.c.subset_id == s)
                query = query.where(keys_table.c.idkey.in_(subset_query))
            if type(s) is str:
                subset_name_query = select([kb.pmc_subsets.c.subset_id]).where(kb.pmc_subsets.c.subset_name == s)
                subset_query = select([kb.pmc_subset_objects.c.object_id]).where(kb.pmc_subset_objects.c.subset_id.in_(subset_name_query))
                query = query.where(keys_table.c.idkey.in_(subset_query))
        
        for q in self.__in_query_filters:
            query = query.where(keys_table.c.idkey.in_(q))
        
        for s in self.__not_set_filters:
            if type(s) is list:
                subset_query = create_query_or_set(s)
                query = query.where(~keys_table.c.idkey.in_(subset_query))
            if type(s) is int:
                subset_query = select([kb.pmc_subset_objects.c.object_id]).where(kb.pmc_subset_objects.c.subset_id == s)
                query = query.where(~keys_table.c.idkey.in_(subset_query))
            if type(s) is str:
                subset_name_query = select([kb.pmc_subsets.c.subset_id]).where(kb.pmc_subsets.c.subset_name == s)
                subset_query = select([kb.pmc_subset_objects.c.object_id]).where(kb.pmc_subset_objects.c.subset_id.in_(subset_name_query))
                query = query.where(~keys_table.c.idkey.in_(subset_query))
        
        for q in self.__not_set_queries:
            query = query.where(~keys_table.c.idkey.in_(q._get_object_query()))
        
        return query

    def _load_properties(self, query):
        """
        Select.append_column()
        """
        if not self._loaded_properties:
            return query
        
        properties = self._get_properties_query()
        
        properties = properties.alias('properties')
        object_query = query.alias('object_query')
        myjoin = outerjoin(object_query, properties, object_query.c.idkey == properties.c.idobj) 
        
        query = select([object_query, 
                        properties.c.inftyp, 
                        properties.c.infsubtyp, 
                        properties.c.string_value,
                        properties.c.int_value,
                        properties.c.blkno]).select_from(myjoin)

        # works but what is the default ordering acc or desc ?
        query = query.order_by(object_query.c.idkey, properties.c.inftyp, properties.c.infsubtyp, properties.c.blkno, properties.c.ordnum)
        
        return query

    def _add_additional_filter(self, filter):
        """
        Add a filter in plus of application object set.
        """
        self.__additional_filter = filter

    def _accept_projects(self):
        """
        Accept also projects
        """
        self.__accept_projects = True
    
    def _reject_objects(self):
        """
        Reject classical (non project) objects
        """
        self.__reject_objects = True

    def __internal(self, cpp, others):

        result = copy.copy(self)

        # new mode 
        result.__modifiers_cpp.append(cpp)
        result.__modifiers_jad.append(others)

        return result



class EnlightenLink(KnowledgeBaseElement, WithProperties):
    """
    A link in enlighten.
    
    It is made of a caller, a callee, and some types of link.
    """
    
    def __init__(self, identifier, idfus, acctyplo, acctyphi, caller, callee, kb, application, project_data, prop):
        self.id = identifier
        self.idfus = idfus
        self.__application = application
        self.__acctyplo = acctyplo
        self.__acctyphi = acctyphi
        self.__kb = kb
        self.kb = kb
        self.__caller_data = caller
        self.__additional_caller_positions = []
        self.__caller = None
        self.__callee_data = callee
        self.__callee = None
        self.__bookmarks = []
        self.__project_data = project_data
        self.__project = None
        self.__prop = prop
        
        # list of plugin ids of plugin that have review this not sure link
        self._reviewed_by = None
        
    def get_caller(self):
        """
        Access to caller object

        :rtype: :class:`cast.application.Object`
        """
        # lazy
        if not self.__caller:
            self.__caller = self.__kb._build_object_wrapper(*self.__caller_data)
            for position in self.__additional_caller_positions:
                self.__caller._add_position(*position)
                
        return self.__caller

    def get_callee(self):
        """
        Access to called object

        :rtype: :class:`cast.application.Object`
        """
        # lazy
        if not self.__callee:
            self.__callee = self.__kb._build_object_wrapper(*self.__callee_data)
        return self.__callee
    
    def get_project(self):
        """
        Access to project of link.
        """
        # lazy
        if not self.__project:
            self.__project = self.__kb._build_object_wrapper(*self.__project_data)
        return self.__project

    def get_type_names(self):
        """
        Access to list of link type names.
        """
        return LinkType.decode_type_names(self.__acctyplo, self.__acctyphi)
        
    def get_types(self):
        """
        Access to list of link types.
        """
        return LinkType.decode_types(self.__acctyplo, self.__acctyphi)

    def get_acctyp(self):
        
        return self.__acctyplo, self.__acctyphi
    
    def get_prop(self):
        
        return self.__prop

    def get_property(self, prop):
        """
        Return a link property.
        
        :param str or int prop: the property fullname, or property id to get
        """
        return self._get_property(prop)

    def get_positions(self):
        """
        Returns the positions of the links, if loaded.
        
        It is loaded if it comes from link query constructed with :meth:`cast.application.LinkQuery.load_positions`
         
        :rtype: list of cast.application.Bookmark.
        """
        return self.__bookmarks

    def get_code(self, additional_lines=0):
        """
        Returns one total line of code containing the links.
        
        :param additional_lines: additional lines (before and after) to be returned.
        
        Example :
        
        for a link to 'CodeDetail'
        
        >>> pos.get_code_line() 
        lstReadyForAdmin.DataValueField = "CodeDetail";
        >>> pos.get_code_line(2)
        lstReadyForAdmin.DataSource = dataSet.Tables[1];
        lstReadyForAdmin.DataTextField = "Description";
        lstReadyForAdmin.DataValueField = "CodeDetail";
        lstReadyForAdmin.DataBind();
        lstReadyForAdmin.Items.Insert(0, new ListItem("*All", string.Empty));        
        
        If the bookmark spans on several lines, this method returns an empty string.
        
        """
        if not self.__bookmarks:
            return ""
        
        return self.__bookmarks[0].get_code_line(additional_lines)

    def save_property(self, prop, value):
        """
        Save a property on current link.
        
        :param prop: the property to save. Either a string for the fullname of the property or an integer for the property id. 
        :param value: 
            the value to set, either a integer, a string or a list of those
            integers should be 32 bits integer (i.e. ranging from [ -2^31+1, 2^31-1])

        The current plugin must have declared the property has his own.  
        :see :meth:`cast.application.Application.declare_property_ownership`
        """
        _property = self._convert_into_property(prop)
        
        # @todo : apply authorisation matrix
        
        self.__application._get_raw_saver().add_link_property(self, _property, value)

    def is_validated(self):
        """
        True when the link is not sure and has been marked as valid.
        Need to have made a LinkQuery with is_not_sure().
        
        .. versionadded:: 1.5.27
        """
        return self.__prop & 1 and self.__prop & 32768

    def is_ignored(self):
        """
        True when the link is not sure and has been marked as invalid.
        Need to have made a LinkQuery with is_not_sure().
        
        .. versionadded:: 1.5.27
        """
        return self.__prop & 1 and self.__prop & 65536

    def is_reviewed(self):
        """
        True when the link is not sure and has been reviewed (marked as valid or invalid).
        Need to have made a LinkQuery with is_not_sure().
        
        .. versionadded:: 1.5.27
        """
        return self.is_ignored() or self.is_validated()

    def is_to_be_reviewed(self):
        """
        True when the link is not sure and has not been been reviewed (marked as valid or invalid).
        Need to have made a LinkQuery with is_not_sure().
        
        .. versionadded:: 1.5.27
        """
        return self.__prop & 1 and not self.is_reviewed()

    def get_reviewer_plugin(self):
        """
        When the link has been validated by an extension, return the id of that extension 
        When the link has been reviewed but not through extension SDK api, then returns None 
        Need to have made a LinkQuery with is_not_sure().
        :rtype: str
        
        .. versionadded:: 1.5.27
        """
        if self._reviewed_by:
            return self._reviewed_by
        return None

    def validate(self):
        """
        Mark current link as valid according to DLM.
        """
        # @todo : apply authorisation matrix
        self.__application._get_raw_saver().validate(self)

    def ignore(self):
        """
        Mark current link as ignored according to DLM.
        """
        # @todo : apply authorisation matrix
        self.__application._get_raw_saver().ignore(self)

    def _get_code_line_from_snapshot(self, additional_lines=0):

        if not self.__bookmarks:
            return ""
        
        return self.__bookmarks[0]._get_code_line_from_snapshot(additional_lines)

    def _add_position(self, file, begin_line, begin_column, end_line, end_column):
        
        self.__bookmarks.append(Bookmark(file, begin_line, begin_column, end_line, end_column))
    
    def _add_caller_position(self, file, begin_line, begin_column, end_line, end_column):
        
        self.__additional_caller_positions.append((file, begin_line, begin_column, end_line, end_column))
    
    def __repr__(self):
        """
        Print.
        """
        return "Link(" + str(self.get_type_names()) + ',' + str(self.get_caller()) + "," + str(self.get_callee()) +")"


class LinkType:
    """
    The list of link types
    """
    use = (0x00200000, 0x00000000)
    useSelect = (0x00200000, 0x00000008)
    useUpdate = (0x00200000, 0x00000002)
    useInsert = (0x00200000, 0x00000001)
    useDelete = (0x00200000, 0x00000004)
    
    call = (0x00000800, 0x00000000)
    callProg = (0x00000800, 0x00010000)
    callTransac = (0x00000800, 0x00020000)
    callPerform = (0x00000800, 0x00040000)
    callGoto = (0x00000800, 0x00080000)

    access = (0x01000000, 0x00000000)
    accessExec = (0x01000000, 0x00000004)
    accessMember = (0x01000000, 0x00000008)
    accessMemberExec = (0x01000000, 0x0000000C)
    accessArray = (0x01000000, 0x00000010)
    accessRead = (0x01000000, 0x00000200)
    accessWrite = (0x01000000, 0x00000400)
    accessOpen = (0x01000000, 0x04000000)
    accessClose = (0x01000000, 0x08000000)
    accessPageInclude = (0x01000000, 0x00000800)
    accessPageForward = (0x01000000, 0x00001000)

    inherit = (0x02000000, 0x00000000)
    inheritExtend = (0x02000000, 0x00000020)
    inheritImplement = (0x02000000, 0x00000040)
    inheritHide = (0x02000000, 0x00008000)
    inheritOverride = (0x02000000, 0x00004000)

    fire = (0x00400000, 0x00000000)
    fireBefore = (0x00400000, 0x00000010)
    fireAfter = (0x00400000, 0x00000020)
    fireInsteadOf = (0x00400000, 0x00000040)
    fireForEachRow = (0x00400000, 0x00000080)
    fireForAllRows = (0x00400000, 0x00000100)
    fireInsert = (0x00400000, 0x00000001)
    fireUpdate = (0x00400000, 0x00000002)
    fireDelete = (0x00400000, 0x00000004)
    fireSelect = (0x00400000, 0x00000008)

    monitor = (0x00800000, 0x00000000)
    monitorBefore = (0x00800000, 0x00000010)
    monitorAfter = (0x00800000, 0x00000020)
    monitorInsteadOf = (0x00800000, 0x00000040)
    monitorForEachRow = (0x00800000, 0x00000080)
    monitorForAllRows = (0x00800000, 0x00000100)
    monitorInsert = (0x00800000, 0x00000001)
    monitorUpdate = (0x00800000, 0x00000002)
    monitorDelete = (0x00800000, 0x00000004)
    monitorSelect = (0x00800000, 0x00000008)

    contain = (0x10000000, 0x00000000)
    containDefine = (0x10000000, 0x00100000)
    containDeclare = (0x10000000, 0x00200000)

    relyon = (0x00008000, 0x00000000)
    
    mention = (0x00001000, 0x00000000)

    prototype = (0x00040000, 0x00000000)
    
    include = (0x00080000, 0x00000000)
    
    match = (0x08000000, 0x00000000)

    refer = (0x00010000, 0x00000000)
    referCascade = (0x00010000, 0x00000400)
    referSetnull = (0x00010000, 0x00000800)
    referInsert = (0x00010000, 0x00000001)
    referUpdate = (0x00010000, 0x00000002)
    referDelete = (0x00010000, 0x00000004)

    relyonIsInstanceOf = (0x00008000, 0x00002000)
    
    ddl = (0x00000100, 0x00000000)
    ddlCreate = (0x00000100, 0x00000010)
    ddlAlter = (0x00000100, 0x00000020)
    ddlReplace = (0x00000100, 0x00000040)
    ddlDrop = (0x00000100, 0x00000080)
    
    join = (0x00000080, 0x00000000)
    joinSpForeignKey = (0x00000080, 0x00200000)
    joinSpCommonKey = (0x00000080, 0x00400000)
    joinNonSysCatalog = (0x00000080, 0x00800000)

    catch = (0x00000002, 0x00000000)
    
    friend = (0x00000004, 0x00000000)
    
    raise_ = (0x00002000, 0x00000000)
    
    throw = (0x00004000, 0x00000000)
    
    lock = (0x00020000, 0x00000000)
    
    gothrough = (0x00000040, 0x00000000)
    
    internallyEscalated = (0x20000000, 0x00000000)
    
    dynamic = (0x00000200, 0x00000000)
    
    static = (0x00000400, 0x00000000)

    @staticmethod
    def decode_type_names(acctyplo, acctyphi):
        """
        Returns a list of link type names corresponding to (acctyplo, acctyphi)        
        """
        
        result = []
        
        for type_name in dir(LinkType):
            try:
                
                link_type = getattr(LinkType, type_name)
                
                if (acctyplo & link_type[0] == link_type[0]) and (acctyphi & link_type[1] == link_type[1]):
                    result.append(type_name)
            except:
                pass
                
        return result
        
    @staticmethod
    def decode_types(acctyplo, acctyphi):
        """
        Returns a list of elementary link types corresponding to (acctyplo, acctyphi)
        """
        
        result = []
        
        for type_name in dir(LinkType):
            try:
                
                link_type = getattr(LinkType, type_name)
                
                if (acctyplo & link_type[0] == link_type[0]) and (acctyphi & link_type[1] == link_type[1]):
                    result.append(link_type)
            except:
                pass
                
        return result


class DLMEnum:
    ignored = 1
    validated = 2
    to_be_reviewed = 3
    not_ignored = 4
    
class LinkQuery(PropertyLoader):
    """
    A query on links.
    
    Follows the Method chaining pattern.
    """
    def __init__(self, application=None):
        """
        Build a query on link either from an existing one or from an application
        """
        PropertyLoader.__init__(self, application)
        self.__Acc = None
        self.__FusAcc = None
        self.__application = None
        
        # aliases
        self.__caller_Keys = None
        self.__callee_Keys = None
        self.__project_Keys = None
        
        # query
        self.__caller_filters = []
        self.__callee_filters = []
        self.__types = []
        self.__project_ids = []
        self.__raw_initial_query = None
        
        # for dlm
        self.__not_sure = False 
        # sub state of dlm : none, ignored, validated, to be reviewed, not ignored
        self.__not_sure_substate = None # DLMEnum
        
        self.__load_bookmark = False
        self._loaded_properties = []
        
        # a secondary query for properties
        self.__property_query = None
        
        # an iterator on properties
        self.__property_iterator = None
        self.__last_read_property_line = None 
        self.__last_read_idfus = None
        self.__last_read_properties = None
        
        
        self.__application = application
        kb = application.kb
        project_ids = application.projects_ids
        
        self.__project_ids = project_ids
        
        Acc = reflect_table('Acc', kb.metadata, kb.engine)
        FusAcc = reflect_table('FusAcc', kb.metadata, kb.engine)
        
        self.__caller_Keys = alias(kb.Keys)
        caller_ObjFulNam = alias(kb.ObjFulNam)
        caller_key_fullname = outerjoin(self.__caller_Keys, caller_ObjFulNam, self.__caller_Keys.c.idkey == caller_ObjFulNam.c.idobj) 
    
        self.__callee_Keys = alias(kb.Keys)
        callee_ObjFulNam = alias(kb.ObjFulNam)
        callee_key_fullname = outerjoin(self.__callee_Keys, callee_ObjFulNam, self.__callee_Keys.c.idkey == callee_ObjFulNam.c.idobj) 
        
        self.__project_Keys = alias(kb.Keys)
        project_ObjFulNam = alias(kb.ObjFulNam)
        project_key_fullname = outerjoin(self.__project_Keys, project_ObjFulNam, self.__project_Keys.c.idkey == project_ObjFulNam.c.idobj) 
        
        query = select([Acc.c.idacc, 
                        Acc.c.acctyplo, 
                        Acc.c.acctyphi,
                        FusAcc.c.idfus,
                        self.__caller_Keys.c.idkey.label('caller_idkey'),
                        self.__caller_Keys.c.objtyp.label('caller_objtyp'),
                        self.__caller_Keys.c.keynam.label('caller_keynam'),
                        caller_ObjFulNam.c.fullname.label('caller_fullname'),
                        self.__callee_Keys.c.idkey.label('callee_idkey'),
                        self.__callee_Keys.c.objtyp.label('callee_objtyp'),
                        self.__callee_Keys.c.keynam.label('callee_keynam'),
                        callee_ObjFulNam.c.fullname.label('callee_fullname'),
                        self.__project_Keys.c.idkey.label('project_idkey'),
                        self.__project_Keys.c.objtyp.label('project_objtyp'),
                        self.__project_Keys.c.keynam.label('project_keynam'),
                        project_ObjFulNam.c.fullname.label('project_fullname'),
                        Acc.c.prop.label('prop')
                        ]).select_from(
                       Acc.join(FusAcc, 
                                Acc.c.idacc == FusAcc.c.idacc).join(caller_key_fullname, 
                                                                    Acc.c.idclr == self.__caller_Keys.c.idkey).join(callee_key_fullname, 
                                                                                                                    Acc.c.idcle == self.__callee_Keys.c.idkey).join(project_key_fullname,
                                                                                                                                                                    Acc.c.idpro == self.__project_Keys.c.idkey))
        # all links of application
        # will now stand TONS OF PROJECTS
        query = query.where(Acc.c.idpro.in_(_get_in_project(application)))
        
        # accknd in (0, 4096, 262144, 1048576) --> do not know but every where 
        query = query.where(Acc.c.accknd.in_((0, 4096, 262144, 1048576)))
        query = query.order_by(FusAcc.c.idfus.asc(), Acc.c.idacc.asc())
        
        # prop&65536 == 0 --> not ignored
        # removed because we want to be access all links
        # reanalysis do not reset those flags
        # query = query.where(Acc.c.prop.op('&')(65536) == 0)    
        
        
        self.__Acc = Acc
        self.__FusAcc = FusAcc
        self.__raw_initial_query = query
        
    
    """
    Method chaining pattern
    
    """    
    def has_caller(self, object_query):
        """
        Filter the links so that caller is in object_query
        
        :param object_query: :class:`cast.application.ObjectQuery` or iterable of :class:`cast.application.Object`
        :rtype: :class:`cast.application.LinkQuery`
        """
        result = copy.copy(self)
        
        if type(object_query) == ObjectQuery:
            result.__caller_filters.append(object_query)
        else:
            # try to convert to ids...
            try:
                temp = []
                for o in object_query:
                    temp.append(o.id)
                object_query = temp
                
                result.__caller_filters.append(object_query)
            except:
                raise RuntimeError('has_caller : parameter %s is not supported' % str(object_query))
        
        return result
     
    def has_callee(self, object_query):
        """
        Filter the links so that callee is in object_query

        :param object_query: :class:`cast.application.ObjectQuery` or iterable of :class:`cast.application.Object`
        :rtype: :class:`cast.application.LinkQuery`
        """
        result = copy.copy(self)
        
        if type(object_query) == ObjectQuery:
            
            result.__callee_filters.append(object_query)
            
        else:
            # try to convert to ids...
            try:
                temp = []
                for o in object_query:
                    temp.append(o.id)
                object_query = temp
                result.__callee_filters.append(object_query)
            except:
                raise RuntimeError('has_caller : parameter %s is not supported' % str(object_query))
        
        return result
    
    def is_not_sure(self):
        """
        Filter only not sure links.
        i.e., links that are eligible to dynamic link manager.
        
        Those links are considered as 'not sure' because they are created from weak strategies.

        :rtype: :class:`cast.application.LinkQuery`
        """
        result = copy.copy(self)
        result.__not_sure = True
        
        return result

    def is_to_be_reviewed(self):
        """
        Filter only not sure links that need to be reviewed.

        :rtype: :class:`cast.application.LinkQuery`

        .. versionadded:: 1.5.9
        """
        result = copy.copy(self)
        result.__not_sure = True
        result.__not_sure_substate = DLMEnum.to_be_reviewed
        
        return result
        
    def is_ignored(self):
        """
        Filter only not sure links that are ignored.

        :rtype: :class:`cast.application.LinkQuery`

        .. versionadded:: 1.5.9
        """
        result = copy.copy(self)
        result.__not_sure = True
        result.__not_sure_substate = DLMEnum.ignored
        
        return result

    def is_not_ignored(self):
        """
        Filter only not sure links that are not ignored.

        :rtype: :class:`cast.application.LinkQuery`

        .. versionadded:: 1.5.9
        """
        result = copy.copy(self)
        result.__not_sure = True
        result.__not_sure_substate = DLMEnum.not_ignored
        
        return result

    def is_validated(self):
        """
        Filter only not sure links that are validated.

        :rtype: :class:`cast.application.LinkQuery`

        .. versionadded:: 1.5.9
        """
        result = copy.copy(self)
        result.__not_sure = True
        result.__not_sure_substate = DLMEnum.validated
        
        return result

    def has_type(self, types):
        """
        Filter the links so that type is in types
        
        - .has_type(LinkType.call)                 : call links
        - .has_type([LinkType.use, LinkType.call]) : use or call links
        
        
        :see :class:`cast.application.LinkType` for known link types
        
        :param list or link type types: link type(s) allowed

        :rtype: :class:`cast.application.LinkQuery`
        """
        result = copy.copy(self)
        
        if type(types) is list:

            if result.__types:
                result.__types = result.__types & set(types)
            else:
                result.__types = set(types)
            
        else:

            if result.__types:
                result.__types = result.__types & set([types])
            else:
                result.__types = set([types])
        
        return result

    def load_positions(self):
        """
        Force loading of positions of link and caller.

        :rtype: :class:`cast.application.LinkQuery`
        """
        result = copy.copy(self)
        result.__load_bookmark = True
        return result

    def load_property(self, propety_or_properties):
        """
        Ask for loading of one or some properties.
        
        Note that loading one or several properties takes longer to perform the query.
        
        Has no effect when query is used in a ObjectQuery. 
        
        :param properties: str or int of list of those. 
        :rtype: :class:`cast.application.LinkQuery`
        """
        return self._load_property(propety_or_properties)
    
    def count(self):
        """
        Returns the number of links in this query.
        
        Execute a count(*) ...
        
        .. versionadded:: 1.5.9
        """
        query = select([func.count()]).select_from(self._get_object_query(as_link=True).alias('l'))
        for result in self.__application.kb.engine.execute(query):
            return result[0]

    def _get_object_query(self, as_caller=True, as_link=False):
        """
        Get a query usable for a caller or callee or link (idacc)
        
        @see ObjectQuery
        """
        Acc = self.__Acc
        
        table = None
        
        if self.__caller_filters and self.__callee_filters:
            table = Acc.join(self.__caller_Keys, Acc.c.idclr == self.__caller_Keys.c.idkey).join(self.__callee_Keys, Acc.c.idcle == self.__callee_Keys.c.idkey)
        elif self.__caller_filters:
            table = Acc.join(self.__caller_Keys, Acc.c.idclr == self.__caller_Keys.c.idkey)
        elif self.__callee_filters:
            table = Acc.join(self.__callee_Keys, Acc.c.idcle == self.__callee_Keys.c.idkey)
        else:
            table = Acc
        
        if as_link:
            FusAcc = self.__FusAcc
            query = select([FusAcc.c.idfus]).select_from(table.join(FusAcc, Acc.c.idacc == FusAcc.c.idacc))
        elif as_caller:
            query = select([Acc.c.idclr]).select_from(table)
        else:
            query = select([Acc.c.idcle]).select_from(table)
                   
        query = query.where(Acc.c.idpro.in_(_get_in_project(self.__application)))
        
        if self.__not_sure:
            query = query.where(bitand(Acc.c.prop, 1, self.__application.kb.engine) != 0) 
        
        """
        accknd in (0, 4096, 262144, 1048576) --> do not know but every where 
        prop&65536 == 0 --> not ignorable
        """
        query = query.where(Acc.c.accknd.in_((0, 4096, 262144, 1048576)))
        
        query = self._filter_query(query)
        
        return query


    def _filter_query(self, query):
        """
        Filter an existing query on acc
        
        add the filtering on 
        - types
        - caller
        - callee
        """
        
        if self.__types:
            
            type_filter = or_((and_(bitand(self.__Acc.c.acctyplo, lt[0], self.__application.kb.engine) == lt[0], 
                                    bitand(self.__Acc.c.acctyphi, lt[1], self.__application.kb.engine) == lt[1]) for lt in self.__types))
            query = query.where(type_filter)
        
        for object_query in self.__caller_filters:
            if type(object_query) == ObjectQuery:
                query = object_query._filter_query(query, self.__caller_Keys)
            else:
                query = query.where(self.__Acc.c.idclr.in_(object_query))
            
        for object_query in self.__callee_filters:
            if type(object_query) == ObjectQuery:
                query = object_query._filter_query(query, self.__callee_Keys)
            else:
                query = query.where(self.__Acc.c.idcle.in_(object_query))
        
        if self.__not_sure:
            # dlm link (marked as not sure)
            query = query.where(bitand(self.__Acc.c.prop, 1, self.__application.kb.engine) != 0)
            
            if self.__not_sure_substate == DLMEnum.ignored:
                query = query.where(bitand(self.__Acc.c.prop, 65536, self.__application.kb.engine) != 0)
            elif self.__not_sure_substate == DLMEnum.validated:
                query = query.where(bitand(self.__Acc.c.prop, 32768, self.__application.kb.engine) != 0)
            elif self.__not_sure_substate == DLMEnum.not_ignored:
                query = query.where(bitand(self.__Acc.c.prop, 65536, self.__application.kb.engine) == 0)
            elif self.__not_sure_substate == DLMEnum.to_be_reviewed:
                query = query.where(bitand(self.__Acc.c.prop, 65536, self.__application.kb.engine) == 0)
                query = query.where(bitand(self.__Acc.c.prop, 32768, self.__application.kb.engine) == 0)
            
        else:
            # all links BUT still remove those marked as ignored
            query = query.where(bitand(self.__Acc.c.prop, 65536, self.__application.kb.engine) == 0)
            
        return query

    def __get_property(self, idfus):
        """
        Get the properties values associated with an identifier.
        
        Scan another query result. 
        """
        result = []
        
        if self.__last_read_property_line:
            
            if self.__last_read_property_line[0] != idfus:
                return result
            
            result.append(self.__last_read_property_line)
            self.__last_read_property_line = None # reset
        
        # when reaching the end of the query result, the iterator is 'closed'
        if not self.__property_iterator.closed:
            
            for line in self.__property_iterator:
                
                if line[0] != idfus:
                    
                    self.__last_read_property_line = line
                    return result
                
                result.append(line)
        
        return result
        
        
    def _create_enlighten_link(self, idacc, idfus, acctyplo, acctyphi, caller_data, callee_data, kb, application, project_data, prop):
        
        result = EnlightenLink(idacc, idfus, acctyplo, acctyphi, caller_data, callee_data, kb, application, project_data, prop)
        if self._loaded_properties or self.__not_sure:

            for _prop in self._loaded_properties:
                result._declare_property_loaded(_prop)
            
            current_inftyp = None
            current_infsubtyp = None
            current_blocknumber = None
            
            properties = None
            
            # several acc can have the same idfus
            if self.__last_read_idfus == idfus:
                properties = self.__last_read_properties
            else:
                properties = self.__get_property(idfus)
                self.__last_read_idfus = idfus
                self.__last_read_properties = properties
                
#             print('properties:', idacc, properties)
            
            for line in properties:
                
                # add property to current object
                inftyp = line['inftyp']
                infsubtyp = line['infsubtyp']
                
                block_number = line['blkno'] # multivalued
                
                prop = kb._search_property(inftyp, infsubtyp)
                # handle large string values/multivalued 
                if prop:
                    string_value = line['string_value']
                    int_value = line['int_value']
                    
                    value = int_value if not int_value is None else string_value
                    
#                     print(current_inftyp, inftyp)
#                     print(current_infsubtyp, infsubtyp)
#                     print(current_blocknumber, block_number)
                    
                    if current_inftyp == inftyp and current_infsubtyp == infsubtyp and current_blocknumber == block_number:
#                         print("_concat_property_value", prop, value)
                        # concat value
                        result._concat_property_value(prop, value)
                    else:
                        # multi value
#                         print("_add_property_value", prop, value)
                        result._add_property_value(prop, value)
                else:
                    # a property not in metamodel
                    if inftyp == -1 and infsubtyp == 0:
                        # for example : validatedBy     
                        result._reviewed_by = line['string_value']
                        
                current_inftyp = inftyp
                current_infsubtyp = infsubtyp
                current_blocknumber = block_number

            # object has no property at all : still put it empty
            if not hasattr(result, '_properties'):
                setattr(result, '_properties', {})
                                
        return result
        
    def __iter__(self):
        """
        Execute query and return an iterator on links so that we can do for loop on self.
        """
        application = self.__application
        kb = application.kb
        
        query = self.__raw_initial_query
        query = self._filter_query(query)
        
#         print(query)
        
        # subquery handling for properties
        if self._loaded_properties or self.__not_sure:
            
            properties = self._get_properties_query(self.__not_sure).alias('properties')
            link_query = self._get_object_query(as_caller=False,as_link=True)
            
            properties_query = select([properties]).select_from(properties).where(properties.c.idobj.in_(link_query))
            
            properties = properties_query.order_by(properties.c.idobj.asc(),
                                                   properties.c.inftyp.asc(),
                                                   properties.c.infsubtyp.asc(),
                                                   properties.c.blkno.asc(), 
                                                   properties.c.ordnum.asc())
            
#             print('properties')
#             print(str(properties.compile(compile_kwargs={"literal_binds": True})))
            
            self.__property_iterator = kb.engine.execute(properties)
            
#             print('done')
        
        if not self.__load_bookmark:
            
#           print('query')
#           print(str(query.compile(compile_kwargs={"literal_binds": True})))
            
#             raise StopIteration
            
            # simple case : no bookmark loading
            for line in kb.engine.execute(query):
                caller_data = (line['caller_idkey'], line['caller_objtyp'], line['caller_keynam'], {'application':application, 'fullname':line['caller_fullname']})
                callee_data = (line['callee_idkey'], line['callee_objtyp'], line['callee_keynam'], {'application':application, 'fullname':line['callee_fullname']})
                project_data = (line['project_idkey'], line['project_objtyp'], line['project_keynam'], {'application':application, 'fullname':line['project_fullname']})
                
                idacc = line['idacc']
                acctyplo = line['acctyplo']
                acctyphi = line['acctyphi']
                idfus = line['idfus']
                prop = line['prop']
                
                yield self._create_enlighten_link(idacc, idfus, acctyplo, acctyphi, caller_data, callee_data, kb, application, project_data, prop)

        else:
            # load bookmarks
            query = self.__add_bookmark(query)
            
            current_link = None
            old_link = None
            current_file = None
            current_caller_first_line = None

#            print('query')
#           print(query)
            
            for line in kb.engine.execute(query):
                
#                 print(line['link_file_id'], line['caller_file_id'])
#                 print(line)
                idacc = line['idacc']
                current_link_id = current_link.id if current_link else None
                
                is_new_link_line = idacc != current_link_id
                
                if is_new_link_line:
                    
                    old_link = current_link

                    additional_caller_data = {'application':application, 'fullname':line['caller_fullname']}

                    caller_file_id = line['caller_file_id']
                    if caller_file_id:
                        
                        typ = kb.metamodel.get_category(id=line['caller_file_type'])
                        
                        current_file = File(kb, caller_file_id, line['caller_file_name'], typ, {'path':line['path']})
                        additional_caller_data['file'] = current_file
                        additional_caller_data['begin_line'] = line['caller_begin_line']
                        additional_caller_data['begin_column'] = line['caller_begin_column']
                        additional_caller_data['end_line'] = line['caller_end_line']
                        additional_caller_data['end_column'] = line['caller_end_column']
                        current_caller_first_line = line['caller_begin_line']
                    
                    caller_data = (line['caller_idkey'], line['caller_objtyp'], line['caller_keynam'], additional_caller_data)
                    callee_data = (line['callee_idkey'], line['callee_objtyp'], line['callee_keynam'], {'application':application, 'fullname':line['callee_fullname']})
                    project_data = (line['project_idkey'], line['project_objtyp'], line['project_keynam'], {'application':application, 'fullname':line['project_fullname']})
                    
                    acctyplo = line['acctyplo']
                    acctyphi = line['acctyphi']
                    idfus = line['idfus']
                    prop = line['prop']
                    
                    current_link = self._create_enlighten_link(idacc, idfus, acctyplo, acctyphi, caller_data, callee_data, kb, application, project_data, prop)
                    
                caller_file_id = line['caller_file_id']
                if current_file and caller_file_id and line['caller_file_id'] != current_file.id:
                    
                    # new position for caller
                    current_file = File(kb, caller_file_id, line['caller_file_name'], typ, {'path':line['path']})
                    current_link._add_caller_position(current_file, line['caller_begin_line'], line['caller_begin_column'], line['caller_end_line'], line['caller_end_column'])
                    current_caller_first_line = line['caller_begin_line']
                    
                
                link_file_id = line['link_file_id']
                if link_file_id and current_file and link_file_id == current_file.id:
                    
                    current_link._add_position(current_file, 
                                               line['link_begin_line'] + current_caller_first_line - 1, 
                                               line['link_begin_column'], 
                                               line['link_end_line'] + current_caller_first_line - 1, 
                                               line['link_end_column'])
                    
                
                if is_new_link_line and old_link:
                    yield old_link
                
                
            # the last one
            if current_link:
                yield current_link
    
    def __add_bookmark(self, query):
        """
        First try
        
        Need to think about several tricky cases :
        
        - case 1 : 
          - caller1 --link type 1--> callee1
          - caller1 --link type 2--> callee1
          - how many links/positions ?
        
        - multiposition caller ... do not work (for example : C declaration/definition)
          need to add a join with accbook.prop and caller.objpos.prop ...
        
        """
        kb = self.__application.kb
        
        AccBook = reflect_table('AccBook', kb.metadata, kb.engine)
        
        query = query.alias('link_query')
        
        file_alias = alias(kb.Keys)
        
        idfus = query.c.idfus
        idacc = query.c.idacc
        
        # this one is tricky!
        # position of link is inside position of caller by design
        # we restrict to accbook and objpos on the same file
        # we get the path through ObjFilref -> RefPath
        query = select([query, 
                        kb.ObjPos.c.info1.label('caller_begin_line'),
                        kb.ObjPos.c.info2.label('caller_begin_column'),
                        kb.ObjPos.c.info3.label('caller_end_line'),
                        kb.ObjPos.c.info4.label('caller_end_column'),
                        AccBook.c.info1.label('link_begin_line'),
                        AccBook.c.info2.label('link_begin_column'),
                        AccBook.c.info3.label('link_end_line'),
                        AccBook.c.info4.label('link_end_column'),
                        kb.RefPath.c.path,
                        AccBook.c.blkno.label('link_file_id'),
                        kb.ObjFilRef.c.idobj.label('caller_file_id'),
                        file_alias.c.objtyp.label('caller_file_type'),
                        file_alias.c.keynam.label('caller_file_name')
                        ]).select_from(query.join(AccBook, 
                                                  query.c.idacc == AccBook.c.idacc, 
                                                  isouter=True).join(kb.ObjPos,
                                                                     and_(query.c.caller_idkey == kb.ObjPos.c.idobj, 
                                                                          AccBook.c.blkno == kb.ObjPos.c.idobjref,
                                                                          AccBook.c.prop == kb.ObjPos.c.prop), # for multiposition objects, 
                                                                     isouter=True).join(kb.ObjFilRef,
                                                                                        and_(kb.ObjFilRef.c.idobj == kb.ObjPos.c.idobjref, 
                                                                                             AccBook.c.blkno == kb.ObjFilRef.c.idobj),
                                                                                        isouter=True).join(kb.RefPath,
                                                                                                           kb.RefPath.c.idfilref == kb.ObjFilRef.c.idfilref,
                                                                                                           isouter=True).join(file_alias,
                                                                                                                              kb.ObjFilRef.c.idobj == file_alias.c.idkey,
                                                                                                                              isouter=True))
        query = query.order_by(idfus.asc(), idacc.asc(), kb.ObjFilRef.c.idobj.asc())
        
        return query
        



Reference = collections.namedtuple('Reference', ['pattern_name',
                                                 'object',
                                                 'value',
                                                 'bookmark'])
"""
A reference found
"""


class ReferenceFinder:
    """
    Search for patterns in a text or file.
    """
    def __init__(self):
        self.token_specification = [
                ('NEWLINE', r'\n'),  # Line endings
            ]

    def add_pattern(self, name, before, element, after):
        """
        Add a search pattern.
        
        :param str name: name of the pattern

        :param str element: a regular expression that is searched
        
        :param str before: a regular expression that should match before the searched element, may be empty but cannot be of variable length
       
        :param str after: a regular expression that should match after the searched element, may be empty
        
        So we search element preceded by before and followed directly by after.
        
        You may add several patterns. 
        First matching pattern will be recognised, so adding overlapping patterns is not recommended.
        
        """
        self.token_specification.append((name,
                                         '(?<=%s)%s(?=%s)' % (before,
                                                              element,
                                                              after)))

    def find_references_in_file(self, file):
        """
        Find references inside a file.
        
        :param file: either a file path or a File object
        
        :rtype: iterable of :class:`cast.application.Reference`
        """
        path = None
        file_object = None
        if type(file) is str:
            path = file
        else:
            path = file.get_path()
            file_object = file
        
        try:
            content = self.read(path)
            return self._find_references(content, file_object)
        except FileNotFoundError:
            return []

    def read(self, path):
        
        try:
            with open_source_file(path) as f:
                return f.read()
        except:
            return ""
        
    def _find_references(self, string, file_object=None):
        """
        Returns all references found as an iterable.
        
        :param iterable of Reference
        """
        
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in self.token_specification)
        # search instead of match to cope with non expressed elements...
        get_token = re.compile(tok_regex, re.MULTILINE).search
        line = 1
        
        # line_start is the position in file of the last begin line
        pos = line_start = 0
        mo = get_token(string)
        while mo is not None:
            typ = mo.lastgroup
            pos = mo.end()
            if typ == 'NEWLINE':
                line_start = pos
                line += 1
            elif typ != 'SKIP':
                val = mo.group(typ)
                
                column = mo.start() - line_start + 1
                
                end_column = column + len(val)
                
                # number of new lines 
                newlines = val.count('\n')
                
                last_newline = val.rfind('\n')
                
                if last_newline != -1:
                    end_column = len(val) - last_newline - 1
                
                yield Reference(typ,
                                file_object if not file_object else file_object.find_most_specific_object(line, column),
                                val,
                                Bookmark(file_object, line, column, line + newlines, end_column)) 
                
                # @todo use 
                line += newlines
                line_start = pos - end_column
                
            mo = get_token(string, pos)



def replace_special_variables(query):
    """
    Replaces inside a text :
        §

    """
    
    # strip comments
    query = sqlparse.format(query, strip_comments=True)
    
    # check for presence of old non standard things...
    if any(x in query for x in ['§']):
        
        query = query.replace('§', '')
        
        logging.warning('you are using a deprecated feature. You can avoid this warning by replacing your query by the following one : %s', query)
        
    return query


def _remove_last_comma(statement):
    
    for i in range(len(statement) - 1, -1, -1):
        c = statement[i]
        if c != ' ' and c != '\t' and c != '\n' and c != '\r':
            if c == ';':
                return statement[:i]
            else:
                return statement[:i + 1]



# see : http://stackoverflow.com/questions/6043463/split-unicode-string-into-300-byte-chunks-without-destroying-characters
def split_utf8(s, n):
    """Split UTF-8 s into chunks of maximum length n."""
    while len(s) > n:
        k = n
        while (ord(s[k]) & 0xc0) == 0x80:
            k -= 1
        yield s[:k]
        s = s[k:]
    yield s
    


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


class RawSaver:
    """
    A raw saver for thing unhandled by AMT saving 
    """
    def __init__(self, application):
        
        self.application = application
        self.kb = application.kb
        self.kb._load_infsub_types()
        
        self.ObjPro = application.kb.ObjPro
        self.Keys = application.kb.Keys
        self.ObjDsc = reflect_table('ObjDsc', self.kb.metadata, self.kb.engine)
        self.ObjInf = reflect_table('ObjInf', self.kb.metadata, self.kb.engine) 
        self.Violations = reflect_table('DSS_Positions', self.kb.metadata, self.kb.engine) 
        
        self.__possessions = []
        self.__properties = []
        self.__violations = []
        # for handling duplicates
        self.__saved_properties = set()
        self.__saved_violations = set()

        self.__link_possessions = []
        self.__link_properties = []

        # links to be marked as validated/ignored
        self.__validated_links = []
        self.__ignored_links = []
        
        self.__validated_idacc = set()
        self.__ignored_idacc = set()
        
        self.__external = []
        
        
        # Following are created during unit tests for sql lite only
        
        # links
        self.__unit_test_links = []
        # objects
        self.guids = set()

    
    def declare_property(self, types, _property):
        """
        Declare possession of a property on some object types
        
        :param types: a list of types
        :param _property: a property with inftyp/infsubtyp
        """
        if not hasattr(_property,'inftyp') or not hasattr(_property,'infsubtyp'):
            raise RuntimeError('Cannot declare the possession of a property that do not have inftyp/infsubtyp')
        
        self.__possessions.append((types, _property))

    def declare_link_property(self, links, _property):
        """
        Declare possession of a property on some links
        
        :param links: a LinkQuery
        :param _property: a property with inftyp/infsubtyp
        """
        if not hasattr(_property,'inftyp') or not hasattr(_property,'infsubtyp'):
            raise RuntimeError('Cannot declare the possession of a property that do not have inftyp/infsubtyp')
        
        self.__link_possessions.append((links, _property))
    
    def add_property(self, _object, _property, value):
        if not self._check(_object, _property):
            return
        
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
        
        
        # check for duplicate saving...
        if (_object.id, _property) in self.__saved_properties or (_object.id, _property) in self.__saved_violations:
            raise RuntimeError('Property already saved for object')
        
        self.__saved_properties.add((_object.id, _property))
        
        self.__properties.append((_object.id, _property, value))
        
    
    def add_link_property(self, link, _property, value):
        """
        Add a property in a link.
        """
        self._check_link_property(link, _property)
        
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
        
        self.__properties.append((link.idfus, _property, value))
    
    
    def add_violation(self, _object, _property, bookmark, additional_bookmarks=[]):
        if not self._check(_object, _property):
            return

        if _property.get_type() != 'integer':
            raise RuntimeError('Property should be integer type for a violation')
        
        if (_object.id, _property) in self.__saved_properties:
            raise RuntimeError('Property already saved for object')
        
        self.__saved_violations.add((_object.id, _property))
        
        self.__violations.append((_object.id, _property, bookmark, additional_bookmarks))
    
    def add_object(self, name, fullname, guid, object_type, parent, ancestor, external):
        """
        Create a new custom object (in case of unit tests only)
        
        :param parent: int or cast.application.Object
        :param ancestor: cast.application.Object, the ancestor of this object that is present in KB
        
        """
        if self.kb.engine.dialect.name != 'sqlite':
            raise RuntimeError('invalid call to add_link')
        
        # guid unicity...
        if guid in self.guids:
            logging.warning('Duplicate GUID %s (fullname %s), objects with that GUID will not be saved.' % (guid,fullname))
            # what to do ???
        self.guids.add(guid)

        if not self.application.get_projects():
            return
        
        # randomly take one project
        project_id = self.application.get_projects()[0].id

        return create_test_object(self.kb.engine, 
                                  project_id, 
                                  name, 
                                  object_type.id,
                                  parent if type(parent) is int else parent.id, 
                                  not external, 
                                  fullname=fullname)
    
    def validate(self, link):
        """
        Mark a link as validated.
        """
        current_plugin_name = self.application.current_plugin.get_name()
        reviewer_plugin = link.get_reviewer_plugin()
        
        if reviewer_plugin and reviewer_plugin != current_plugin_name:
            return
        
        if link.id in self.__validated_idacc:
            return
        self.__validated_idacc.add(link.id)

        self.__validated_links.append(link)

    def ignore(self, link):
        """
        Mark a link as validated.
        """
        # if the link has already been validated by another plugin : then log + skip
        # avoid nasty issues.. do not really work
        current_plugin_name = self.application.current_plugin.get_name()
        reviewer_plugin = link.get_reviewer_plugin()
        
        if reviewer_plugin and reviewer_plugin != current_plugin_name:
            return

        if link.id in self.__ignored_idacc:
            return
        self.__ignored_idacc.add(link.id)

        self.__ignored_links.append(link)

    def save(self):
        
        try:
            # 1. clean all possessed properties and violations
            self._clean()
            self._clean_links()
    
            # warning : order counts
            self._save_violations()
            self._save_properties()
            
            # unsure links
            self._clean_reviewed_links()
            self._save_not_sure_links()
        
            # saving test links
            self._save_test_links()
        
            # putting objects as external
            self._save_as_external()
            
            # et voila!
        except:
            self.kb.raw_connection.rollback()
            raise
            
    def add_link(self, link_type, caller, callee, bookmark=None):
        """
        Create a link between 2 objects.
        
        ONLY for sqllite, it is a very limited implementation : no cleanup etc...
        
        @param link_type: either an integer, a string or a Type
        @param caller: either an integer or an Object
        @param callee: either an integer or an Object
        """
        if self.kb.engine.dialect.name != 'sqlite':
            raise RuntimeError('invalid call to add_link')
        
        
        link_type_object = None
        if type(link_type) is int:
            link_type_object = self.kb.metamodel.get_category(id=link_type)
        elif type(link_type) is str:
            link_type_object = self.kb.metamodel.get_category(name=link_type)
        else:
            link_type_object = link_type
        
        self.__unit_test_links.append((link_type_object, 
                                       caller if type(caller) is int else caller.id,
                                       callee if type(callee) is int else callee.id, 
                                       bookmark))
        
        
    def set_as_external(self, o):
        """
        Set an object and all its children as external
        """
        self.__external.append(o.id)
        
    def _clean(self):
        """
        Clean owned properties
        """
        # cleanup phase
        for possession in self.__possessions:
            
            # query object in project and type is the current possession
            # important to clean also external objects...
            is_in_project = select([self.ObjPro.c.idobj]).where(self.ObjPro.c.idpro.in_(self.application.projects_ids))

            query = select([self.Keys.c.idkey])
            query = query.where(self.Keys.c.idkey.in_(is_in_project))
            query = query.where(self.Keys.c.objtyp.in_([t.id for t in possession[0]]))
            
            prop = possession[1]
            
            inftyp = prop.inftyp
            infsubtyp = prop.infsubtyp
            
            if prop.get_type() == 'string':
                # delete from objdsc
                d = delete(self.ObjDsc).where(self.ObjDsc.c.inftyp == inftyp).where(self.ObjDsc.c.infsubtyp == infsubtyp).where(self.ObjDsc.c.idobj.in_(query))
                self.kb.engine.execute(d)
                self.kb.raw_connection.commit()
                
            elif prop.get_type() == 'integer':
                # delete from objinf
                d = delete(self.ObjInf).where(self.ObjInf.c.inftyp == inftyp).where(self.ObjInf.c.infsubtyp == infsubtyp).where(self.ObjInf.c.idobj.in_(query))
                self.kb.engine.execute(d)
                self.kb.raw_connection.commit()
                
            # delete from violations
            d = delete(self.Violations).where(self.Violations.c.objectid.in_(query)).where(self.Violations.c.propertyid == prop.id)
            self.kb.engine.execute(d)
            self.kb.raw_connection.commit()
    
    def _clean_links(self):
        
        # cleanup phase
        for possession in self.__link_possessions:
            
            # rewrite link query
            query = possession[0]._get_object_query(as_link=True)
            
            prop = possession[1]
            
            inftyp = prop.inftyp
            infsubtyp = prop.infsubtyp
            
            if prop.get_type() == 'string':
                # delete from objdsc
                d = delete(self.ObjDsc).where(self.ObjDsc.c.inftyp == inftyp).where(self.ObjDsc.c.infsubtyp == infsubtyp).where(self.ObjDsc.c.idobj.in_(query))
                self.kb.engine.execute(d)
            
            elif prop.get_type() == 'integer':
                # delete from objinf
                d = delete(self.ObjInf).where(self.ObjInf.c.inftyp == inftyp).where(self.ObjInf.c.infsubtyp == infsubtyp).where(self.ObjInf.c.idobj.in_(query))
                self.kb.engine.execute(d)
        
    
    def _clean_reviewed_links(self):
        """
        Mark as not reviewed all links that where previously reviewed by the current plugin
        """
        # only if we are in end_application
        if hasattr(self.application, '_current_phase') and getattr(self.application, '_current_phase') != 'end_application':
            return
        
        current_plugin_name = self.application.current_plugin.get_name()
        Acc = reflect_table('Acc', self.kb.metadata, self.kb.engine)
        FusAcc = reflect_table('FusAcc', self.kb.metadata, self.kb.engine)
        
        links = select([FusAcc.c.idacc]).select_from(FusAcc.join(self.ObjDsc, 
                                                                 and_(self.ObjDsc.c.inftyp == -1,
                                                                      self.ObjDsc.c.infsubtyp == 0,
                                                                      self.ObjDsc.c.infval.in_((current_plugin_name, # for migration from previous api version 
                                                                                                current_plugin_name + ' validate',
                                                                                                current_plugin_name + ' ignore')),
                                                                      self.ObjDsc.c.idobj == FusAcc.c.idfus)))

        # we need to restrict to links inside application
        up = Acc.update().where(Acc.c.idacc.in_(links)).where(Acc.c.idpro.in_(_get_in_project(self.application))).values(prop = bitand(Acc.c.prop, -98305, self.kb.engine))
        self.kb.engine.execute(up)
        
        # reset the property values for reviewed by...
        delete = self.ObjDsc.delete().where(and_(self.ObjDsc.c.inftyp == -1,
                                                 self.ObjDsc.c.infsubtyp == 0,
                                                 self.ObjDsc.c.infval.in_((current_plugin_name, # for migration from previous api version 
                                                                          current_plugin_name + ' validate',
                                                                          current_plugin_name + ' ignore'))))
        self.kb.engine.execute(delete)
        
        
            
    def _get_values_and_violations(self):
        
        # stores object -> property -> integer : the violation count
        property_values = defaultdict(dict)
                
        # object -> property -> list of (bookmark, additional_bookmarks)
        ordered_violations = defaultdict(dict)
        
        # order and count violations
        for violation in self.__violations:
            object_id, _property, bookmark, additional_bookmarks = violation
            
            temp = ordered_violations[object_id]
            
            if _property in temp:
                temp[_property].append((bookmark, additional_bookmarks))
            else:
                temp[_property] = [(bookmark, additional_bookmarks)]

            temp = property_values[object_id]
            if _property in temp:
                temp[_property] += 1
            else:
                temp[_property] = 1
                
        return property_values, ordered_violations
    
    def _save_violations(self):
        # 2. insert violations 
        
        # get the next violation id
        query = select([func.max(self.Violations.c.metricpositionid)])
        result = self.kb.engine.execute(query)
        max_metric_position_id = result.fetchone()[0]
        if not max_metric_position_id:
            max_metric_position_id = 0
        
        metric_position_id = max_metric_position_id+1  
        
        violation_content = []
        
        property_values, ordered_violations = self._get_values_and_violations()
        
        
        # dss_positions works the following way : 
        # for each couple (objectid, propertyid) we have a unique metric_position_id
        # then we must have a reltively unique positionid to distinguish the distinct violation patterns for the same (objectid, propertyid) 
        # then we must have distinct position_index for the several bookmarks of a same violation pattern

        # paranoid : we change positionid every line
        positionid = 1
        
        # scan violation but following object, prop order
        for object_id in ordered_violations.keys():
            
            t1 = ordered_violations[object_id]
            for _property in t1.keys():
                # list of couple bookmark, additional_bookmarks
                vs = t1[_property]
                
                for bookmark, additional_bookmarks in vs:
                    position_index = 1 # starts at one 
                    
                    violation_content.append((metric_position_id, # == unique per (objectid, property)
                                              object_id,
                                              _property.id,
                                              bookmark.file.id,
                                              positionid, 
                                              position_index,
                                              bookmark.begin_line,
                                              bookmark.begin_column,
                                              bookmark.end_line,
                                              bookmark.end_column
                                              ))
                    
                    for additional in additional_bookmarks:
                        position_index += 1 # same violation next bookmark
                        violation_content.append((metric_position_id,
                                                  object_id,
                                                  _property.id,
                                                  additional.file.id,
                                                  positionid, 
                                                  position_index,
                                                  additional.begin_line,
                                                  additional.begin_column,
                                                  additional.end_line,
                                                  additional.end_column
                                                  ))
                
                    positionid += 1 # increased for each violation
                
                metric_position_id += 1 # increased for each property
                
            metric_position_id += 1 # and object


        
        if violation_content:
            ins = self.Violations.insert()
            cursor = self.kb.create_cursor()
            cursor.executemany(str(ins.compile()), violation_content)
            self.kb.raw_connection.commit()
        
        # automatically fill integer properties to be setted with the violation count
        for objectid in property_values:
            for prop in property_values[objectid]:
                self.__properties.append((objectid, prop, property_values[objectid][prop])) 
    
    def _save_properties(self):
        # 3. insert the values for properties
        integer_values = []
        string_values = []
        for object_id, prop, value in self.__properties:
            
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
            ins = self.ObjDsc.insert()
            cursor = self.kb.create_cursor()
            cursor.executemany(str(ins.compile()), string_values)
            self.kb.raw_connection.commit()

        if integer_values:
            # bulk insert
            ins = self.ObjInf.insert()
            cursor = self.kb.create_cursor()
            cursor.executemany(str(ins.compile()), integer_values)
            self.kb.raw_connection.commit()

    def _check(self, _object, _property):
        """
        Check that _object is allowed for _property
        """
        for possession in self.__possessions:
            if possession[1] == _property and _object.type in possession[0]:
                return True
        
        raise RuntimeError('Property %s was not declared as handled for that type %s, see http://cast-projects.github.io/Extension-SDK/doc/code_reference.html?highlight=save_property#cast.application.Object.save_property and http://cast-projects.github.io/Extension-SDK/doc/code_reference.html?highlight=save_property#cast.application.Application.declare_property_ownership' % (str(_property), str(_object.type)))
        return False
    
    def _check_link_property(self, link, _property):
        """
        Not much we can do except evaluate the query itself.
        At least check that we have _property registered
        """
        
        for possession in self.__link_possessions:
            if possession[1] == _property:
                return True

        raise RuntimeError('Property %s was not declared as handled for links, see http://cast-projects.github.io/Extension-SDK/doc/code_reference.html?highlight=save_property#cast.application.EnlightenLink.save_property and http://cast-projects.github.io/Extension-SDK/doc/code_reference.html?highlight=save_property#cast.application.Application.declare_property_ownership' % (str(_property)))
        return False
    
    def _save_not_sure_links(self):
        
        # only if we are in end_application
        if hasattr(self.application, '_current_phase') and getattr(self.application, '_current_phase') != 'end_application':
            return
        
        Acc = reflect_table('Acc', self.kb.metadata, self.kb.engine)
        FusAcc = reflect_table('FusAcc', self.kb.metadata, self.kb.engine)
        
        if self.__validated_links:
            link_ids = [link.id for link in self.__validated_links if not(link.id in self.__ignored_idacc and link.id in self.__validated_idacc)]
            
            # do it by chunks
            # limited to something like 32000 
            for link_chunk in chunks(link_ids, 30000):
                up = Acc.update().where(Acc.c.idacc.in_(link_chunk)).values(prop = bitand(Acc.c.prop, -98305, self.kb.engine).op('|')(32768)) 
                self.kb.engine.execute(up)
        
        if self.__ignored_links:
            link_ids = [link.id for link in self.__ignored_links  if not(link.id in self.__ignored_idacc and link.id in self.__validated_idacc)]
            
            # do it by chunks
            # limited to something like 32000 
            for link_chunk in chunks(link_ids, 30000):
             
                up = Acc.update().where(Acc.c.idacc.in_(link_chunk)).values(prop = bitand(Acc.c.prop, -98305, self.kb.engine).op('|')(65536)) 
                self.kb.engine.execute(up)
        
        # mark links as reviewed by...
        # it can be complex as we need to enforce unique constraint
        # there are several extension and each one can review
        # a fus link can be made of several links so we can also have "duplicates"
        
        # 1. get the links that already are validated by someone (in fact other extensions)
        _from = FusAcc.join(self.ObjDsc,
                            and_(self.ObjDsc.c.inftyp == -1,
                                 self.ObjDsc.c.infsubtyp == 0,
                                 self.ObjDsc.c.idobj == FusAcc.c.idfus))
        
        
        application_acc = select([Acc.c.idacc]).where(Acc.c.idpro.in_(_get_in_project(self.application)))
        application_fusacc = select([FusAcc.c.idfus]).where(FusAcc.c.idacc.in_(application_acc))
        links = select([FusAcc.c.idfus,
                        self.ObjDsc.c.blkno
                        ]).select_from(_from).where(FusAcc.c.idfus.in_(application_fusacc))
        
        # for each links already having the property, gives the max blkno
        validated = {}
        
        for line in self.kb.engine.execute(links):
            idfus = line[0]
            try:
                validated[idfus] = max(validated[idfus], line[1])
            except KeyError:
                validated[idfus] = 0
                
        string_values = []
        current_plugin_name = self.application.current_plugin.get_name()
        existing_idfus = set()
        for link in self.__ignored_links + self.__validated_links:
            
            if link.id in self.__ignored_idacc and link.id in self.__validated_idacc:
                # conflict : skip
                logging.warning('Link %s was both validated and ignored => skipping.', str(link.id))
                continue
            
            action = ' '
            if link.id in self.__ignored_idacc:
                action += 'ignore'
            if link.id in self.__validated_idacc:
                action += 'validate'
            
            if link.idfus in existing_idfus:
                # twice validated/invalidated
                continue
            existing_idfus.add(link.idfus)
            
            blkno = 0
            try:
                blkno = validated[link.idfus] + 1
            except KeyError:
                pass
            string_values.append((link.idfus,
                                  -1,
                                  0,
                                  blkno,
                                  0,
                                  0,
                                  current_plugin_name + action))
        
        if string_values:
            ins = self.ObjDsc.insert()
            cursor = self.kb.create_cursor()
            cursor.executemany(str(ins.compile()), string_values)
            self.kb.raw_connection.commit()
    
        # clean memory
        self.__validated_idacc = set()
        self.__validated_links = []
        self.__ignored_idacc = set()
        self.__ignored_links = []
        
    def _save_test_links(self):
        
        if not self.application.get_projects():
            return
        
        # randomly take one project
        project = self.application.get_projects()[0].id
        
        for link_type, caller, callee, bookmark in self.__unit_test_links:
            
            link = create_test_link(self.kb.engine, project, caller, callee, getattr(LinkType,link_type.get_name()[:-4]))
            if bookmark:
                add_link_position(self.kb.engine, 
                                  link, 
                                  bookmark.file.id, 
                                  bookmark.begin_line,
                                  bookmark.begin_column,
                                  bookmark.end_line,
                                  bookmark.end_column)
            
            
    def _save_as_external(self):
        
        if not self.__external:
            return
        
        # working but binding is a little brutal (may have hundreds of values)
        # sqlite : ok
        # css : ok
        # oracle : ?
        # ms : ok
        if self.kb.engine.dialect.name in ['mssql', 'oracle']:
            # for ms/oracle
            query = """
    WITH all_objects(IdKey) AS (
      
      select IdKey from Keys where IdKey in (%s) UNION ALL 
      SELECT parent.IdKey
      FROM KeyPar parent, all_objects aob
      WHERE parent.IdParent = aob.IdKey
    ) 
        update ObjPro set Prop=1 where IdObj in (select IdKey from all_objects);
            """ % ','.join(str(v) for v in self.__external)

        else:
                
            query = """
    
    update ObjPro set Prop=1 where IdObj in (
    WITH RECURSIVE all_objects(IdKey) AS (
      
      select IdKey from Keys where IdKey in (%s) UNION ALL 
      SELECT parent.IdKey
      FROM KeyPar parent, all_objects aob
      WHERE parent.IdParent = aob.IdKey
    ) 
    select IdKey from all_objects
    );
            """ % ','.join(str(v) for v in self.__external)
            
        cursor = self.kb.create_cursor()
        
        self.kb._execute_raw_query(cursor, query)

    
def open_source_file(path, encoding=None):
    """
    Equivalent of python open(path) that autotdetects encoding.
    
    handles long path, UNC paths
    
    :param encoding: specified encoding (optional) 
    
    :rtype: file 
    """
    from chardet.universaldetector import UniversalDetector
    
    # for long pathes : see https://stackoverflow.com/questions/29557760/long-paths-in-python-on-windows
    local_path = path
    
    if sys.platform.startswith('win32'):
        constant = '\\\\?\\'
        
        if not local_path.startswith(constant):
            local_path = local_path.replace('/', '\\')
            if local_path.startswith(r'\\'):
                local_path = r'\\?\UNC' + local_path[1:]
            elif os.path.isabs(local_path):
                local_path = constant + local_path
    
    if not encoding:
        detector = UniversalDetector()
        with open(local_path, 'rb') as f:
            count = 0
            for line in f:
                detector.feed(line)
                count += 1
                if detector.done or count > 100: 
                    break
        detector.close()
    
        encoding = detector.result['encoding']
        logging.debug('File %s has %s as detected encoding' % (path, encoding))
    try:
        result = open(local_path, 'r', encoding=encoding, errors='replace')
    except LookupError:
        logging.info('Lookup error with wrong unknown encoding, try by forcing UTF-8 encoding')
        result = open(local_path, 'r', encoding='UTF-8', errors='replace')

    return result


######################
# Central part
######################


class CentralBase(CastSchema):
    """
    A connection to a central base
    """
    
    def __init__(self, name, engine=None):
        
        CastSchema.__init__(self, name, engine)
        self._package_name = "ADG_CENTRAL"
        
        self.dss_objects = reflect_table('DSS_OBJECTS', self.metadata, self.engine)
        self.dss_object_info = reflect_table('DSS_OBJECT_INFO', self.metadata, self.engine)
        self.dss_translation = reflect_table('DSS_TRANSLATION_TABLE', self.metadata, self.engine)
        self.dss_snapshots = reflect_table('DSS_SNAPSHOTS', self.metadata, self.engine)
        
        # DO NOT ADD CODE ABOVE OR DOWN as it wont upgrade...
    
    def __repr__(self):
        return 'CentralBase(%s)' % self.name
    
    def get_applications(self):
        """
        Access to applications.
        
        :rtype: list of :class:`cast.application.managment.Application`
        
        .. versionadded:: 1.5.8
        """
        query = select([self.dss_objects.c.object_id, 
                        self.dss_objects.c.object_name]).where(self.dss_objects.c.object_type_id == -102)
        
        result = []
        by_id = {}
        
        for line in self._execute_sqlalchemyquery2(query):
            application = CentralApplication(line[0], line[1], self)
            result.append(application)
            by_id[line[0]] = application
        
        setattr(self, 'applications_by_id', by_id)
        
        return result
    
    def get_application(self, name):
        """
        Access to application by name.
        
        :rtype: :class:`cast.application.managment.Application`
        
        .. versionadded:: 1.5.8
        """
        
        for application in self.get_applications():
            if application.name == name:
                return application
        
        
    def get_snapshots(self):
        """
        Access to snapshots.
        
        :rtype: :class:`cast.application.managment.Snapshot`
        @return: cast.application.managment.Snapshot
        """
        
        query = select([self.dss_snapshots.c.snapshot_id, 
                        self.dss_snapshots.c.application_id,
                        self.dss_snapshots.c.snapshot_name])
    
        result = []
    
        for line in self._execute_sqlalchemyquery2(query):
            
            result.append(CentralSnapshot(line[0], line[2], line[1]))
    
        return result
        

class CentralApplication:
    """
    Application in the central base.
    
    .. versionadded:: 1.5.8
    """
    def __init__(self, identifier, name, central):
        
        self.name = name
        self.id = identifier
        self.central = central
        self.managment = None # managment base associated with the application
        
    def get_central(self):
        """
        Central base of the application.
        """
        return self.central

    def get_managment_base(self):
        """
        Access to managment base.
        
        :return: :class:`cast.application.managment.ManagmentBase`
    
        WARNING : 
           this version only works for combined install on the same server.
           Future version of CAIP will leverage this limitation.
           
           Not working on sqlserver
        
        .. versionadded:: 1.5.8
        """
        if not hasattr(self, 'managment'):
            setattr(self, 'managment', None)
        
        if not self.managment:
            
            central_name = self.central.name

            if not central_name:
                # ms with database encoded in the connectio nstring ...
                url = str(self.kb.engine.url)
                result = re.search('DATABASE=(.*);', url)
                central_name = result.group(1)
#                 print(central_name)
            
            if central_name.lower().endswith('_central'):
                # case sensisitve ms
                if central_name.endswith('_central'):
                    postfix = '_mngt'
                else:
                    postfix = '_MNGT'
                
                mngt_name = central_name[:-8] + postfix
                self.managment = ManagmentBase(mngt_name, self.central.engine) 
        
        if not self.managment:
            logging.warning('get_managment_base is only working for combined installs')
            
        return self.managment

    def get_application_configuration(self):
        """
        Access to managment base application.
        
        :return: :class:`cast.application.managment.Application`
    
        WARNING : 
           this version only works for combined install on the same server.
           Future version of CAIP will leverage this limitation.
        
        .. versionadded:: 1.5.8
        """
        try:
            mngt = self.get_managment_base()
            return mngt.get_application(self.name)
        except:
            logging.warning('get_application_configuration is unsupported')
            return None

    def __repr__(self):
        
        return 'Application(%s)' % self.name
    
    def _run_amt_saver(self):
        """For compat"""
        pass
    
    
class CentralSnapshot:
    
    def __init__(self, identifier, name, application_id):
        
        self.name = name
        self.id = identifier
            
    
######################
# Managment part
######################


class ManagmentBase(CastSchema):
    """
    A connection to a management base
    """

#     @todo : 
#     
#     - do not do the same mistake twice...
#       - table loading should be delayed up to usefull...
#     - try on a sqlserver case sensitive
# 
#     Miscelaneous information 
#     
#     cms_dynamicfields contains uuids it seems to be 
#     - uuid.uuid4()
    
    def __init__(self, name, engine=None):
        
        CastSchema.__init__(self, name, engine)
        self._package_name = "PMC_MAIN"
        
        """
        Interesting tables :
        - application
        - module
        - synchronisation translation
        """
        self.cms_dynamicfields = reflect_table("cms_dynamicfields", self.metadata, self.engine)
        
        self.cms_objectlinks = reflect_table("cms_objectlinks", self.metadata, self.engine)
        
        self.cms_sync_translation = reflect_table("cms_sync_translation", self.metadata, self.engine)

        
        self.cms_portf_application = reflect_table("cms_portf_application", self.metadata, self.engine)
    
        self.cms_portf_module = reflect_table("cms_portf_module", self.metadata, self.engine)

        self.cms_inf_snapshot = reflect_table("cms_inf_snapshot", self.metadata, self.engine) 

        self.cms_portf_system = reflect_table("cms_portf_system", self.metadata, self.engine) 
    
    
        # infrastructure
        self.cms_inf_css_centraldb = reflect_table("cms_inf_css_centraldb", self.metadata, self.engine)
        self.cms_inf_css_localdb = reflect_table("cms_inf_css_localdb", self.metadata, self.engine)

        self.cms_inf_ora_centraldb = reflect_table("cms_inf_ora_centraldb", self.metadata, self.engine)
        self.cms_inf_ora_localdb = reflect_table("cms_inf_ora_localdb", self.metadata, self.engine)

        self.cms_inf_sqlsrv_centraldb = reflect_table("cms_inf_sqlsrv_centraldb", self.metadata, self.engine)
        self.cms_inf_sqlsrv_localdb = reflect_table("cms_inf_sqlsrv_localdb", self.metadata, self.engine)

    
        # connections
        self.cms_inf_store_css = reflect_table("cms_inf_store_css", self.metadata, self.engine)
        
        self.cms_inf_store_oracle = reflect_table("cms_inf_store_oracle", self.metadata, self.engine)
        self.cms_inf_ora_accesssid = reflect_table("cms_inf_ora_accesssid", self.metadata, self.engine)
        self.cms_inf_ora_accesssrv = reflect_table("cms_inf_ora_accesssrv", self.metadata, self.engine)
        
        self.cms_inf_store_sqlserver = reflect_table("cms_inf_store_sqlserver", self.metadata, self.engine)
        self.cms_inf_sqlsrv_accessinst = reflect_table("cms_inf_sqlsrv_accessinst", self.metadata, self.engine)
        self.cms_inf_sqlsrv_accessport = reflect_table("cms_inf_sqlsrv_accessport", self.metadata, self.engine)
        
        
        # delivery and deploy
        self.delivery_path = None
        self.deploy_path = None
        
        cms_pref_sources = reflect_table("cms_pref_sources", self.metadata, self.engine)  
        
        query = select([cms_pref_sources.c.serverpath, 
                        cms_pref_sources.c.deploypath])
        
        for line in self._execute_sqlalchemyquery2(query):
            
            self.delivery_path = line[0]
            self.deploy_path = line[1]
        
        # DO NOT ADD CODE ABOVE OR DOWN as it wont upgrade...
    
    def __repr__(self):
        
        return "Managment(%s)" %self.name
        
    def get_applications(self):
        """
        Get the applications defined in the base.
        
        :rtype: list of :class:`cast.application.managment.Application`
        """
        
        table_join = self.cms_portf_application.join(self.cms_dynamicfields,
                                                     self.cms_portf_application.c.object_id == self.cms_dynamicfields.c.object_id)
        
        table_join = table_join.join(self.cms_sync_translation,
                                     self.cms_dynamicfields.c.field_value == self.cms_sync_translation.c.entryobjpmc)
        
        
        query = select([distinct(self.cms_portf_application.c.object_id), # may have several entries so distinct
                        self.cms_portf_application.c.object_name, 
                        self.cms_portf_application.c.deploypath,
                        self.cms_dynamicfields.c.field_value,
                        self.cms_sync_translation.c.idobjservice,
                        self.cms_portf_application.c.localdb_id,
                        self.cms_portf_application.c.mail]).select_from(table_join).where(self.cms_sync_translation.c.adapterclass == 'com.castsoftware.pmc.connection.synchro.UserProjectOptionAdapter')
        
        result = []
        
        application_ids = set()
        
        for line in self._execute_sqlalchemyquery2(query):
            
            if line[0] not in application_ids:
                result.append(ManagmentApplication(self, line[0], line[1], line[2], line[3], line[4], line[5], line[6]))
                application_ids.add(line[0])
        
        return result
        
    def get_application(self, name):
        """
        Access to an application by name.
        
        :param str name: the name of the application

        :rtype: :class:`cast.application.managment.Application`
        """
        for app in self.get_applications():
            if app.name == name:
                return app
            
        return None
    
    def get_delivery_path(self):
        """
        Access to delivery path.
        
        :rtype: str
        """
        return self.delivery_path
    
    def get_deploy_path(self):
        """
        Access to deploy path.

        :rtype: str
        """
        return self.deploy_path
        
    def get_dmt_application(self, name):
        """
        Access to an application in DMT inside the delivery folder.
        
        :rtype: cast.application.DMTApplication

        .. versionadded:: 1.6.17
        """
        folder_path = os.path.join(self.delivery_path, 'data')
        uuid = _get_guid_from_dmt_index(folder_path, name)
        if uuid:
            result = DMTApplication(name)
            result.delivery_path = self.delivery_path
            result.guid = uuid
            result.mngt = self
            return result
        
    def _get_server_engine(self, server_id, server_type):
        """
        Find a server by id
        """
        

        if server_type == "css":
            
            query = select([self.cms_inf_store_css.c.host,
                            self.cms_inf_store_css.c.port,
                            self.cms_inf_store_css.c.username,
                            self.cms_inf_store_css.c.password]).where(self.cms_inf_store_css.c.object_id == server_id)
            
            for line in self._execute_sqlalchemyquery2(query):           
                
                message = get_message(line[3][9:])
                return create_postgres_engine(line[2], message, line[0], line[1])
            
            
        elif server_type == "ora":
            # checked with 'service' name
            # @todo : check if working with SID
            _from = outerjoin(self.cms_inf_store_oracle, 
                              self.cms_inf_ora_accesssid, 
                              self.cms_inf_store_oracle.c.access_id == self.cms_inf_ora_accesssid.c.object_id)
            
            _from = outerjoin(_from,
                              self.cms_inf_ora_accesssrv,
                              self.cms_inf_store_oracle.c.access_id == self.cms_inf_ora_accesssrv.c.object_id)
            
            query = select([self.cms_inf_store_oracle.c.host,
                            self.cms_inf_store_oracle.c.port,
                            self.cms_inf_store_oracle.c.username,
                            self.cms_inf_store_oracle.c.password,
                            self.cms_inf_ora_accesssid.c.service,
                            self.cms_inf_ora_accesssrv.c.service]).select_from(_from).where(self.cms_inf_store_oracle.c.object_id == server_id)
                            
            for line in self._execute_sqlalchemyquery2(query):           
                
                message = get_message(line[3][9:])
                return create_oracle_engine(line[2], message, line[0], line[1], line[4], line[5])

        elif server_type == "sqlsrv":
            # @todo
            # not working properly because of connection sqlserver needing 'schema'
            
#             raise RuntimeError('Why are you using sqlserver? Please use css instead.')
                        
            _from = outerjoin(self.cms_inf_store_sqlserver, 
                              self.cms_inf_sqlsrv_accessinst, 
                              self.cms_inf_store_sqlserver.c.access_id == self.cms_inf_sqlsrv_accessinst.c.object_id)
            
            _from = outerjoin(_from,
                              self.cms_inf_sqlsrv_accessport,
                              self.cms_inf_store_sqlserver.c.access_id == self.cms_inf_sqlsrv_accessport.c.object_id)
            
            query = select([self.cms_inf_store_sqlserver.c.host,
                            self.cms_inf_store_sqlserver.c.username,
                            self.cms_inf_store_sqlserver.c.password,
                            self.cms_inf_store_sqlserver.c.trusted,
                            self.cms_inf_sqlsrv_accessinst.c.instance,
                            self.cms_inf_sqlsrv_accessport.c.port]).select_from(_from).where(self.cms_inf_store_sqlserver.c.object_id == server_id)
                            
            for line in self._execute_sqlalchemyquery2(query):           
                
                message = get_message(line[2][9:])
                return create_sqlserver_engine(line[1], message, line[0], '', line[5], line[4], line[3])
        
        
                


class ManagmentApplication:
    """
    The definition of an application in CMS
    """
    def __init__(self, mb, identifier, name, deploy_path, uuid, kb_id, local_mngt_id, mail):
        self.mb = mb
        self.id = identifier
        self.uuid = uuid
        self.name = name
        self.deploy_path = deploy_path
        self.kb_id = kb_id
        # the mngt id of the 'local service'
        self.local_mngt_id = local_mngt_id
        
        self.__mail = mail 
        # kb
        self.analysis_service = None
        
        # centrals
        self.dashboard_services = []
        
        # source code packages (repositories)
        self.packages = []
        

    def get_packages(self):
        """
        Get the source packages of the application.

        :rtype: list of :class:`cast.application.managment.Package`
        """
        self.repositories_ids = self._calculate_repositories()
        return self.packages

    def get_analysis_units(self):
        """
        Get the analysis units of the application.

        :rtype: list of :class:`cast.application.managment.AnalysisUnit`
        """
        # source code repositories ids
        self.repositories_ids = self._calculate_repositories()
        self.analysis_units = self._calculate_analysis_units()
        return self.analysis_units

    def get_modules(self):
        """
        Access to modules definitions
        
        :rtype: list of :class:`cast.application.managment.Module`
        """
        self.modules = self._calculate_module_list()
        return self.modules
    
    def get_module(self, name):
        """
        Get a module definition

        :rtype: :class:`cast.application.managment.Module`
        """
        self.modules = self._calculate_module_list()
        for module in self.modules:
            if module.name == name:
                return module
            
        return None
    
    def get_snapshots(self):
        """
        Get the snapshots of the application.

        :rtype: list of :class:`cast.application.managment.Snapshot`
        """
        self.snapshots = self._calculate_snapshots()
        return self.snapshots

    def get_analysis_service(self):
        """
        Access to analysis service of the application
        
        :rtype: :class:`cast.application.KnoweldgeBase`
        """
        if not self.analysis_service:
            
            name = None
            server_id = None
            
            cursor = self.mb.create_cursor()

            self.mb._execute_raw_query(cursor, 
                                       """select object_name, server_id, server_type 
                                          from (      select object_id, object_name, server_id, 'css' as server_type from cms_inf_css_localdb 
                                                union select object_id, object_name, server_id, 'ora' as server_type from cms_inf_ora_localdb 
                                                union select object_id, object_name, server_id, 'sqlsvr' as server_type from cms_inf_sqlsrv_localdb) temp 
                                          where temp.object_id = (%s)""" % self.local_mngt_id)
            
            for line in cursor:
                name = line[0]
                server_id = line[1]
                server_type = line[2]
                
                engine = self.mb._get_server_engine(server_id, server_type)
                
                try:
                    self.analysis_service = Server.get_server(engine).get_schema(name)
                except:
                    # connection refused...
                    raise RuntimeError('Connection refused to %s' % str(engine))
            
        return self.analysis_service
        
    def get_dashboard_services(self):
        """
        Access to analysis service of the application

        :rtype: list of :class:`cast.application.central.CentralBase`
        """

        if not self.dashboard_services:
            
            # get the services id
            system_link = join(self.mb.cms_portf_system, 
                               self.mb.cms_objectlinks, 
                               self.mb.cms_portf_system.c.object_id == self.mb.cms_objectlinks.c.caller_id) 
            
            query = select([self.mb.cms_portf_system.c.central_id]).select_from(system_link)
            query = query.where(self.mb.cms_objectlinks.c.symbol == 'applications')
            query = query.where(self.mb.cms_objectlinks.c.callee_id == self.id)
            
            services_id = []
            
            for line in self.mb._execute_sqlalchemyquery2(query):
                
                services_id.append(line[0])
                
            # locate them in centradb tables
            cursor = self.mb.create_cursor()

            self.mb._execute_raw_query(cursor, 
                                       """select object_name, server_id, server_type 
                                          from (      select object_id, object_name, server_id, 'css' as server_type from cms_inf_css_centraldb 
                                                union select object_id, object_name, server_id, 'ora' as server_type from cms_inf_ora_centraldb 
                                                union select object_id, object_name, server_id, 'sqlsvr' as server_type from cms_inf_sqlsrv_centraldb) temp 
                                          where temp.object_id in (%s)""" % ','.join([str(service_id) for service_id in services_id]))
            
            for line in cursor:
                name = line[0]
                server_id = line[1]
                server_type = line[2]

                engine = self.mb._get_server_engine(server_id, server_type)
                
                try:
                    self.dashboard_services.append(Server.get_server(engine).get_schema(name))
                except:
                    # connection refused...
                    print('connection refused')
                    pass
        
        return self.dashboard_services

    
    def get_email_to_send_reports(self):
        """
        If configured, returns the email to send reports to.
        
        :rtype: str
        """
        return self.__mail
    
    def get_database_subset_strategy(self):
        """
        Return the database subset strategy associated with the application.
        
        Possible values are:
        'Inactive'
        'Interface'
        'Full'
        
        .. versionadded:: 1.6.3
        """
        
        query = select([
                        self.mb.cms_dynamicfields.c.field_value
                       ]).where(self.mb.cms_dynamicfields.c.field_guid=='dbSubsetStrategy').where(self.mb.cms_dynamicfields.c.object_id==self.id)
                       
        
        for line in self.mb._execute_sqlalchemyquery2(query):
            
            if line[0] == 'DBSubsetTypeInactive':
                return 'Inactive'
            elif line[0] == 'DBSubsetTypeInterface':
                return 'Interface'
            elif line[0] == 'DBSubsetTypeFull':
                return 'Full'

        
    def _calculate_repositories(self):
        """
        CMS 'sources' folders than contains Analysis units
        """
        repository_types = ['bo', 'dbudb', 'dbzosextract', 'file', 'formsextract', 
                            'mfextract', 'oracleextract', 'sapextract', 'sqlserverextract',
                            'sybaseextract', 'uiextract']
    
        result = []
    
        for t in repository_types:
            
            try:
                    
                cursor = self.mb.create_cursor()
                self.mb._execute_raw_query(cursor, 'select object_id, object_name, rootpath from cms_code_repo_%s where application_id = %s' % (t,self.id))
                
                for line in cursor:
                    result.append(line[0])
                    self.packages.append(Package(line[0], line[1], line[2], t))
                    
            except:
                # no such techno
                pass
            
            
        return result
    
    def _calculate_analysis_units(self):
        
        # special case for UA
        au_to_techno = defaultdict(set)
        
        cms_objectlinks = reflect_table('cms_objectlinks', self.mb.metadata, self.mb.engine)
        cms_ua_language = reflect_table('cms_ua_language', self.mb.metadata, self.mb.engine)
        cms_ua_analysis = reflect_table('cms_ua_analysis', self.mb.metadata, self.mb.engine)
        # loads all mapping AU --> UA techno name : here for manual UAs
        query = select([cms_objectlinks.c.caller_id, 
                        cms_ua_language.c.name]).where(cms_objectlinks.c.symbol == 'languages').where(cms_objectlinks.c.callee_id == cms_ua_language.c.object_id)
        
        for line in self.mb._execute_sqlalchemyquery2(query):
            au_to_techno[line[0]].add(line[1])
        
        
        # here for discovered UAs (do not ask me why)
        query = select([cms_ua_analysis.c.object_id, 
                        cms_ua_language.c.name]).where(cms_objectlinks.c.symbol 
                                                       == 'languages').where(cms_objectlinks.c.callee_id 
                                                                             == cms_ua_language.c.object_id).where(cms_objectlinks.c.caller_id
                                                                                                                   == cms_ua_analysis.c.project_id)
        for line in self.mb._execute_sqlalchemyquery2(query):
            au_to_techno[line[0]].add(line[1])
            
        # @todo remove
        cursor = self.mb.create_cursor()

        # loading of sources selections, we do not consider exotic extracts
           
        cms_code_sourcefile = reflect_table('cms_code_sourcefile', self.mb.metadata, self.mb.engine)
        cms_code_sourcefolder = reflect_table('cms_code_sourcefolder', self.mb.metadata, self.mb.engine)
        cms_code_sourcefilecpp = reflect_table('cms_code_sourcefilecpp', self.mb.metadata, self.mb.engine)
        cms_code_sourcefoldercpp = reflect_table('cms_code_sourcefoldercpp', self.mb.metadata, self.mb.engine)
        
        queries = [select([cms_code_sourcefile.c.object_id,
                           cms_code_sourcefile.c.usage,
                           cms_code_sourcefile.c.path 
                           ]),
                   select([cms_code_sourcefilecpp.c.object_id,
                           cms_code_sourcefilecpp.c.usage,
                           cms_code_sourcefilecpp.c.path 
                           ]),
                   select([cms_code_sourcefolder.c.object_id,
                           cms_code_sourcefolder.c.usage,
                           cms_code_sourcefolder.c.path 
                           ]),
                   select([cms_code_sourcefoldercpp.c.object_id,
                           cms_code_sourcefoldercpp.c.usage,
                           cms_code_sourcefoldercpp.c.path 
                          ])         
                ]
        
        if self.mb.get_caip_version() < StrictVersion("8.1.0"):
            
            
            cms_code_sourcefilenet = reflect_table('cms_code_sourcefilenet', self.mb.metadata, self.mb.engine)
            cms_code_sourcefoldernet = reflect_table('cms_code_sourcefoldernet', self.mb.metadata, self.mb.engine)
            
            queries.append(select([cms_code_sourcefilenet.c.object_id,
                                   cms_code_sourcefilenet.c.usage,
                                   cms_code_sourcefilenet.c.path 
                                  ]))
    
            queries.append(select([cms_code_sourcefoldernet.c.object_id,
                                   cms_code_sourcefoldernet.c.usage,
                                   cms_code_sourcefoldernet.c.path 
                                  ]))

        if self.mb.get_caip_version() >= StrictVersion("8.1.0"):
                        
            cms_code_additionalfilecpp = reflect_table('cms_code_additionalfilecpp', self.mb.metadata, self.mb.engine)
            cms_code_additionalfoldercpp = reflect_table('cms_code_additionalfoldercpp', self.mb.metadata, self.mb.engine)
    
            queries.append(select([cms_code_additionalfilecpp.c.object_id,
                                   cms_code_additionalfilecpp.c.usage,
                                   cms_code_additionalfilecpp.c.path 
                                  ]))
    
            queries.append(select([cms_code_additionalfoldercpp.c.object_id,
                                   cms_code_additionalfoldercpp.c.usage,
                                   cms_code_additionalfoldercpp.c.path 
                                  ]))

        
        # id of path --> usage + path
        pathes = {}
        for line in self.mb._execute_sqlalchemyquery2(union(*queries)):
            pathes[line[0]] = (line[1], line[2])

        
        # loading of association AU -> sources
        sources_of_au = defaultdict(list) 
        
        query = select([cms_objectlinks.c.caller_id, cms_objectlinks.c.callee_id]).where(cms_objectlinks.c.symbol == 'sources')
        
        for line in self.mb._execute_sqlalchemyquery2(query):
            sources_of_au[line[0]].append(line[1])
        
                
        # general case
        technos = ['asp', 
                   'bo',
                   'cobol',
                   'cpp',
                   'forms',
                   'j2ee',
                   'net',
                   'ora',
                   'pb',
                   'sap',
                   'sqlsrv',
                   'syb',
                   'ua',
                   'udb',
                   'ui',
                   'vb',
                   'zos']

        result = []
        aus = {}
        for techno in technos:
            
            try:
                table = reflect_table('cms_%s_analysis'%techno, self.mb.metadata, self.mb.engine)
                
                query = select([table.c.object_id,
                                table.c.object_name,
                                table.c.execlog,
                                table.c.execdate,
                                self.mb.cms_dynamicfields.c.field_value,
                                table.c.project_id,
                               ]).where(table.c.resource_id.in_(self.repositories_ids)).where(table.c.object_id 
                                                                                              == 
                                                                                              self.mb.cms_dynamicfields.c.object_id).where(self.mb.cms_dynamicfields.c.field_value.like('uuid%%'))
                
                for line in self.mb._execute_sqlalchemyquery2(query):
                    au_id = line[0]
                    au = AnalysisUnit(self.mb, au_id, line[1], techno, self, line[2], line[3], line[4])
                    aus[line[0]] = au
                    result.append(au)
                    
                    project_id = line[5]
                    
                    def _add_path(key_id):
                        try:
                            for source in sources_of_au[key_id]:
                                usage, path = pathes[source]
                                
                                if 'Include' in usage:
                                    au.included_pathes.append(path)
                                else:
                                    au.excluded_pathes.append(path) 
                            
                        except KeyError:
                            pass
                    _add_path(au_id)
                    _add_path(project_id)
                    
                    if au.get_technology() == 'ua':
                        try:
                            au.ua_technologies = au_to_techno[au_id]
                        except KeyError:
                            pass
                    
            except:
                # no such techno
                pass
                
        table_join = outerjoin(self.mb.cms_dynamicfields,
                               self.mb.cms_sync_translation,
                               self.mb.cms_dynamicfields.c.field_value == self.mb.cms_sync_translation.c.entryobjpmc)
        
        query = select([self.mb.cms_dynamicfields.c.object_id, self.mb.cms_sync_translation.c.object_id]).select_from(table_join).where(self.mb.cms_dynamicfields.c.object_id.in_(aus.keys()))
        
        for line in self.mb._execute_sqlalchemyquery2(query):
            aus[line[0]].local_id_setnam = line[1]
        
        return result
        
    def _calculate_module_list(self):
        
        # list modules of app
        
        table_join = self.mb.cms_portf_module.join(self.mb.cms_dynamicfields, 
                                                   self.mb.cms_portf_module.c.object_id == self.mb.cms_dynamicfields.c.object_id,
                                                   isouter=True)
        
        query = select([self.mb.cms_portf_module.c.object_id, 
                        self.mb.cms_portf_module.c.object_name,
                        self.mb.cms_dynamicfields.c.field_value]).select_from(table_join).where(self.mb.cms_portf_module.c.application_id == self.id)
        
        
        result = []
        
        for line in self.mb._execute_sqlalchemyquery2(query):
            
            result.append(Module(self.mb, line[0], line[1], line[2], self))

        return result
    
    def _calculate_snapshots(self):
        
        
        query = select([self.mb.cms_inf_snapshot.c.object_id,
                        self.mb.cms_inf_snapshot.c.object_name,
                        self.mb.cms_inf_snapshot.c.versionlabel,
                        self.mb.cms_inf_snapshot.c.functionaldate,
                        self.mb.cms_inf_snapshot.c.internal_timestamp,
                        self.mb.cms_inf_snapshot.c.central_id
                        ]).where(self.mb.cms_inf_snapshot.c.application_id == self.id)
                        
        result = []
        
        for line in self.mb._execute_sqlalchemyquery2(query):
            
            result.append(ManagmentSnapshot(self.mb, line[0], line[1], line[2], line[3], line[4], self, line[5]))

        return result
    
    def __repr__(self):
        return 'Application(name=%s)' % (self.name)

    
class Module:
    """
    The definition of a module
    """
    def __init__(self, mb, identifier, name, uuid, application):
        self.mb = mb
        self.id = identifier
        self.uuid = uuid
        self.name = name
        self.application = application
        
    def __repr__(self):
        return 'Module(name=%s)' % (self.name)


class Package:
    """
    A source code package.
    """
    def __init__(self, identifier, name, path, _type):
        
        self.id = identifier
        self.name = name
        self.path = path
        self.type = _type

    def get_name(self):
        """
        Name of the package
        """
        return self.name
    
    def get_path(self):
        """
        Deployment path of the package
        """
        return self.path
    
    def get_type(self):
        """
        Package type.
        
        :return: 'bo', 'dbudb', 'dbzosextract', 'file', 'formsextract', 
                 'mfextract', 'oracleextract', 'sapextract', 'sqlserverextract',
                 'sybaseextract', 'uiextract'
        """
        return self.type
    
    
    def __repr__(self):
        return 'Package(name=%s, path=%s)' % (self.name, self.path)
    

class AnalysisUnit:
    """
    The definition of an analysis unit.
    """

    def __init__(self, mb, identifier, name, technology, application, log, last_execution_date, uuid):
        self.mb = mb
        self.id = identifier
        self.uuid = uuid
        self.name = name
        self.technology = technology
        self.application = application
        self.local_id_setnam = None
        self.log = log
        self.last_execution_date = last_execution_date
        self.ua_technologies = [] # in case of ua
        self.included_pathes = [] # what path/folder are selected
        self.excluded_pathes = [] # what path/folder are excluded

    def get_technology(self):
        """
        Access to technology of the AU.
        
        :return: 'asp', 'bo', 'cobol', 'cpp', 'forms', 'j2ee', 'net', 'ora', 
                 'pb', 'sap', 'sqlsrv', 'syb', 'ua', 'udb', 'ui', 'vb', 'zos'        
        """
        return self.technology
    
    def get_technologies(self):
        """
        Generalized access to the technologies present in that AU. 
        For 'core' technology return a list of one element, e.g., : ['cpp'] ['j2ee'] 
        For Universal Analyzer return a list of selected technologies (there may be several in one UA analysis unit).
        
        .. versionadded:: 1.5.20
        """
        if self.ua_technologies:
            return list(self.ua_technologies)
        else:
            return [self.technology]
    
    def get_included_selection(self):
        """
        Return the pathes/folders selected as included in CMS.

        .. versionadded:: 1.5.20
        """
        return self.included_pathes
        
    def get_excluded_selection(self):
        """
        Return the pathes/folders selected as excluded in CMS.

        .. versionadded:: 1.5.20
        """
        return self.excluded_pathes
    
    def get_log(self):
        """
        Last analysis log path.
        """
        return self.log
    
    def get_last_execution_date(self):
        """
        Last execution date.
        """
        return self.last_execution_date
    
    def projects(self, kb):
        """
        Given a KnowledgeBase, gives the associated projects
        """
        return self._create_subset_query(kb, 'PRO')

    def heads(self, kb):
        """
        Given a KnowledgeBase, gives the associated head.
        """
        # hmm ... not sure of project restriction
        return self._create_subset_query(kb, 'AU_HEAD').has_type('project')
        
    def full(self, kb):
        """
        Given a KnowledgeBase, gives the associated full content
        """
        return self._create_subset_query(kb, 'AU_FULL')

    def jobs(self, kb):
        """
        Given a KnowledgeBase, gives the job associated with analysis unit.
        
        Probably bugged...
        """
        return self._create_subset_query(kb, 'JOB')

    def _create_subset_query(self, kb, subset_type):
        """
        subset_type in ('PRO', 'AU_HEAD', 'AU_FULL', 'JOB')
        """
        kb._ensure_additional_tables()
        
        # where 
        if kb.get_caip_version() >= StrictVersion("8.2.2"):
            subset_name = 'CMS_' + subset_type + '__' + str(self.uuid)
        else:
            subset_name = 'CMS_' + subset_type + '__' + str(self.id) 
        
        subset_join = outerjoin(kb.pmc_subsets, 
                                kb.pmc_subset_objects, 
                                kb.pmc_subsets.c.subset_id == kb.pmc_subset_objects.c.subset_id)
        subset_content = select([kb.pmc_subset_objects.c.object_id]).select_from(subset_join).where(kb.pmc_subsets.c.subset_name == subset_name)

        result = ObjectQuery(application=kb.get_application(self.application.name))
        result._add_additional_filter(kb.Keys.c.idkey.in_(subset_content))
        result._accept_projects()
        
        return result
        
    def __repr__(self):
        if self.technology == 'ua':
            return 'AnalysisUnit(techno=%s, name=%s)' % (self.ua_technologies, self.name)
        else:
            return 'AnalysisUnit(techno=%s, name=%s)' % (self.technology, self.name)


class ModuleContent:
    """
    Content of a module in knowledge base.
    
    """
#     @todo 
#     - move it to knowledge base ?
#     - choose if it is available at some particular steps ?
#     - or always ?
#     

    def __init__(self, application, definition=None, name=None):
        """
        :param application: cast.application.Application
        :param definition: cast.application.managment.Module
        """
        self.application = application
        self.name = None
        self.mngt_uuid = None
        self.mngt_id = None

        if definition:
            
            self.mngt_id = definition.id
            self.mngt_uuid = definition.uuid
            self.name = definition.name
            
            self._calculate_technical_modules()
        
    def get_technical_modules(self):
        """
        Get the technical modules of a module
        """
        if not self.mngt_id:
            raise RuntimeError('module preview is not available')

        return self.technical_modules
    
    def preview(self):
        """
        Access to module content preview as seen from CAST-MS.
        
        Available if module content comes from a ManagmentBase.
        
        Scans table PMC_SUBSET_OBJECTS. The setname comes from the CAST-MS id of the module.
        """
        
        if not self.mngt_id:
            raise RuntimeError('module preview is not available')
        
        kb = self.application.kb
        kb._ensure_additional_tables()
        
        # where 
        if kb.get_caip_version() >= StrictVersion("8.2.2"):
            subset_name = 'CMS_MOD__' + str(self.mngt_uuid) + '_Preparation2'
        else:
            subset_name = 'CMS_MOD__' + str(self.mngt_id) + '_Preparation2'
        
        subset_join = outerjoin(kb.pmc_subsets, 
                                kb.pmc_subset_objects, 
                                kb.pmc_subsets.c.subset_id == kb.pmc_subset_objects.c.subset_id)
        subset_content = select([kb.pmc_subset_objects.c.object_id]).select_from(subset_join).where(kb.pmc_subsets.c.subset_name == subset_name)
        
        result = ObjectQuery(self.application)
        result._add_additional_filter(kb.Keys.c.idkey.in_(subset_content))
        
        return result
    
    def objects(self):
        """
        Access to module content.
        
        APPSET
        """
        kb = self.application.kb
        
        object_filter = union(select([kb.objset.c.idobj]).where(kb.objset.c.idset.in_(self.technical_module_ids)),
                              select([kb.ObjPro.c.idobj]).where(kb.ObjPro.c.idpro.in_(self.technical_module_ids)).where(kb.ObjPro.c.prop == 0))
        
        result = ObjectQuery(self.application)
        result._add_additional_filter(kb.Keys.c.idkey.in_(object_filter))
        
        return result

    def diags(self):
        """
        Access to module content from metrics point of view
        
        Scans table CTT_OBJECT_APPLICATIONS.
        """
        kb = self.application.kb

        object_filter = select([kb.ctt_object_applications.c.object_id]).where(kb.ctt_object_applications.c.application_id.in_(self.technical_module_ids))
        
        result = ObjectQuery(self.application)
        result._add_additional_filter(kb.Keys.c.idkey.in_(object_filter))
        
        return result

    def _get_technical_modules_query(self):
        
        kb = self.application.kb
        kb._ensure_additional_tables()
        
        setname = 'MODULE_JOB_SPA_FROM_PMC#' + self.mngt_uuid
        
        appset_join = outerjoin(kb.appset,
                                kb.setroot,
                                kb.appset.c.idset == kb.setroot.c.idset)
        technical_modules = select([kb.setroot.c.idroot]).select_from(appset_join).where(kb.appset.c.idsetnam == setname)
        
        return technical_modules
    
    def _calculate_technical_modules(self):
        
        kb = self.application.kb
        
        query = self._get_technical_modules_query()
        
        self.technical_module_ids = []
        for line in kb._execute_sqlalchemyquery2(query):
            self.technical_module_ids.append(line[0])
        
        query = kb._get_select_object().where(kb.Keys.c.idkey.in_(self.technical_module_ids))
        
        self.technical_modules = list(kb._execute_query(query, self.application))
        
    def __repr__(self):
        
        return 'Module(name=%s)' % self.name


class ManagmentSnapshot:
    """
    A snapshot.
    """
    
    def __init__(self, mb, identifier, name, version, functional_date, computed_date, application, central_id):
        self.mb = mb
        self.identifier = identifier
        self.name = name
        self.version = version
        self.functional_date = functional_date
        self.computed_date = computed_date # do not work at all... 
        self.application = application
        self.central_id = central_id
        
    
    
    def get_version(self):
        
        return self.version

######################
# Server part
######################


class Combined:
    """
    The classical combination of a management, local, and central.
    
    Also known as 'triplet'. 
    """
    def __init__(self, server, name):
        
        self.server = server
        self.name = name
        
        self.local = None
        self.central = None
        self.mngt = None
        
    def get_local(self):
        """
        
        """
        if not self.local:
            
            self.local = KnowledgeBase(self.name + '_local', self.server.engine)
        
        return self.local
    
    def get_central(self):
        
        if not self.central:
            
            self.central = CentralBase(self.name + '_central', self.server.engine)
        
        return self.central
    
    def get_managment(self):
        
        if not self.mngt:

            self.mngt = ManagmentBase(self.name + '_mngt', self.server.engine)
        
        return self.mngt
    
    def update_license_key(self, license_key):
        """
        Change the license key
        
        .. versionadded:: 1.6.21
        """
        # not optimal, we do not need to load the schemas
        self.get_managment().update_license_key(license_key)
        self.get_local().update_license_key(license_key)
        self.get_central().update_license_key(license_key)
    
    def __repr__(self):
        
        return "Combined(%s)" %self.name
        
        

class Server:
    """
    Connection to a server.
    """
    # caching
    servers = {}
    
    def __init__(self, engine=None):
        
        self.engine = engine or create_postgres_engine()
        # connection sharing
        self.connection, self.raw_connection = ConnectionSharing.get_connections(self.engine)
        
        # storage for caching
        self.schemas = {}
        
        # caching
        Server.servers[self.engine] = self
        

    @staticmethod
    def get_server(engine):
        """
        Access to serve by engine
        """
        try:
            return Server.servers[engine]
        except:
            return Server(engine)
        
    def get_schema(self, name):
        """
        Open a schema by name and autodetect its nature.
        """
        
        # cache first
        try:
            return self.schemas[name]
        except:
            pass
        
        if self.engine.dialect.name == 'mssql':
            
            result = self.engine.execute("select * from [%s].dbo.SYS_PACKAGE_VERSION" % name)
            
        else:
            
            result = self.engine.execute("select * from %s.SYS_PACKAGE_VERSION" % name)
        
        names = set((line[0] for line in result))
        
        result = None
        
        if 'ADG_CENTRAL' in names:
            result = CentralBase(name, self.engine)
        elif 'PMC_MAIN'  in names:
            result = ManagmentBase(name, self.engine)
        elif 'APPW'  in names:
            result = KnowledgeBase(name, self.engine)
        else:
            raise RuntimeError('Schema "%s" is not an eligible CAST schema.' % name)
            
        self.schemas[name] = result
        return result
        

    def get_combined_installs(self):
        """
        Get all the triplets of a schema.
        """
        result = []
        
        all_schemas = self._get_all_schemas()
        for schema in all_schemas:
            
            if schema.lower().endswith('_mngt'):
                
                small_name = schema[:-5]
                
                if (schema.endswith('_mngt') and small_name + '_local' in all_schemas and small_name + '_central' in all_schemas)\
                    or (small_name + '_LOCAL' in all_schemas and small_name + '_CENTRAL' in all_schemas):
                    
                    combined = Combined(self, small_name)
                    
                    result.append(combined)
        
        return result
        
    def get_combined_install(self, name):
        """
        Get a triplet of a schema.
        """
        for triplet in self.get_combined_installs():
            
            if triplet.name == name:
                return triplet
        
    def get_managment_schemas(self):
        """
        Access to all management schemas in the server.
        
        @rtype: list 
        @todo : support non standard (_mngt) schemas
        """
        for schema in self._get_all_schemas():
            if schema.lower().endswith('_mngt'):
                yield self.get_schema(schema)
                
    def get_managment_schema_names(self):
        """
        Access to all management schemas in the server.
        
        @rtype: list 
        @todo : support non standard (_mngt) schemas
        """
        for schema in self._get_all_schemas():
            if schema.lower().endswith('_mngt'):
                yield schema

    def get_local_schemas(self):
        """
        Access to all local schemas in the server.
        
        @todo : support non standard (_local) schemas
        """
        for schema in self._get_all_schemas():
            if schema.lower().endswith('_local'):
                yield self.get_schema(schema)
        
            
    def get_managment_schema(self, name):
        """
        Access to a management schema in the server.
        """
        return self.get_schema(name)
    
    def has_license_key_expired(self, schema_name):
        """
        True if the license key has expired.
        
        .. versionadded:: 1.6.21
        """
        query = "select license_code from %s.sys_licenses" % schema_name
        
        today = date.today()
        expired = True
        for line in self.engine.execute(query):
            license = line[0]
            if get_expiration_date(license) >= today:
                expired = False
                break
        return expired
    
    def get_cast_schema_names(self):
        """
        Return a iterable of all cast schema names

        .. versionadded:: 1.6.21
        """
        result = list()
        for name in sorted(self._get_all_schemas()):
            if name.endswith(('_mngt', '_local', '_central')):
                result.append(name)
        return result
    
    def update_license_key(self, schema_name, license_key):
        """
        Update the license for a schema

        .. versionadded:: 1.6.21
        """
        logging.info('Update license key for %s', schema_name)
        query = "update %s.sys_licenses set license_code='%s'" % (schema_name, license_key)
        self.engine.execute(query)
    
    def update_license_for_all_expired_schemas(self, license_key):
        """
        Will update the license for all schemas with expired license

        .. versionadded:: 1.6.21
        """
        
        for schema_name in self.get_cast_schema_names():
            if self.has_license_key_expired(schema_name):
                self.update_license_key(schema_name, license_key)
        
    def _get_all_schemas(self):
        
        if self.engine.dialect.name == 'mssql':
            
            result = self.engine.execute("select name FROM sys.databases order by name;")
            return set((line[0] for line in result))
            
        else:
            insp = inspect(self.engine)
            return set(insp.get_schema_names())
        
    
class DMTApplication:
    """
    An application in DMT

    .. versionadded:: 1.6.17
    """
    def __init__(self, name):
        
        self.name = name
        self.delivery_path = None
        self.mngt = None
        self.guid = None
    
    def get_delivery_folder(self):
        
        return os.path.join(self.delivery_path, 'data', '{%s}'%self.guid)
    
    def get_version(self, name):
        
        uuid = _get_guid_from_dmt_index(self.get_delivery_folder(), name)
        if uuid:
            result = DMTVersion(name)
            result.application = self
            result.mngt = self.mngt
            result.guid = uuid
            result.delivery_path = self.delivery_path
            return result
        

class DMTVersion:
    """
    A version in DMT
    .. versionadded:: 1.6.17
    """
    
    def __init__(self, name):
        
        self.name = name
        self.delivery_path = None
        self.mngt = None
        self.application = None
        self.guid = None
        
    def get_delivery_folder(self):
        
        return os.path.join(self.application.get_delivery_folder(), '{%s}'%self.guid)
    
    def get_package(self, name):
        
        uuid = _get_guid_from_dmt_index(self.get_delivery_folder(), name)
        if uuid:
            result = DMTPackage(name)
            result.version = self
            result.mngt = self.mngt
            result.guid = uuid
            return result


class DMTPackage:
    """
    A package in DMT
    """
    def __init__(self, name):
        
        self.name = name
        self.delivery_path = None
        self.mngt = None
        self.version = None
        self.guid = None
    
    def remove_discoverer(self, name):
        """
        Remove discoverer.
        
        For example 
        - Visual C++ 2002-2008 project
        - Visual C++ 2010-2012 project
        """
        file_path = os.path.join(self.version.get_delivery_folder(), '%s.entity.xml'%self.guid)
        tree = eTree.parse(file_path)
        root = tree.getroot()
        
        for discover_root in root.findall('.//discoverers'):
            for element in discover_root.findall("./*[@name='%s']"%name):
                logger = logging.getLogger('cast.application')
                logger.info('Removing discoverer %s', element.tag)
                discover_root.remove(element)
                break
        
        tree.write(file_path)
        
        
    
        
######################
# Setup part
######################


class CASTAIP:
    """
    An install for CAIP.
    """
    def __init__(self, path):
        
        # location
        self.__path = path
        
        # deduced...
        self.__version = None
        self.__user_folder = None
        self.__all_users_path = None
        self.__current_user_temp_path = None
        self.__common_path = None
        self.__common_unversionned_path = None
        self.__plugin_root_path = None
        
        self.__read_cwbin()
        self.__read_ini()
        
        # @todo set the default values
        self.__lisa_path = None
        self.__ltsa_path = None
        self.__log_root_path = None
        
        self.__mail_host = None
        self.__mail_port = None
        self.__mail_from = None
        
        self.__mail_user = None
        self.__mail_password = None
        
        self.__read_cms_preferences()

    @staticmethod
    def get_running_caip():
        """
        Get the current CAIP running.
        """
        # the running python.exe indicates the flat location
        python_exe_path = sys.executable
        return CASTAIP(os.path.dirname(os.path.dirname(os.path.dirname(python_exe_path))))

    def get_version(self):
        """
        Version of the AIP.
        """
        return self.__version
    
    def get_path(self):
        """
        Get folder containing AIP install.
        """
        return self.__path

    def get_user_preferences_path(self):
        """
        Folder used to store preferences
        
        CAST_CURRENT_USER_WORK_PATH=%APPDATA%\\CAST\\CAST\\$CAST_MAJOR_VERSION$.$CAST_MINOR_VERSION$
        """
        return self.__user_folder
    
    def get_lisa_path(self):
        """
        Access to configured LISA path
        
        LISA stands for Large Intermediate Storage Area 
        This is the folder where AIP stores interchange data.
        
        """
        return self.__lisa_path
    
    def get_mail_server(self):
        """
        Returns the SMTP mail server if it has been configured in CMS.
        
        @see http://doc.castsoftware.com/display/DOC82/CMS+-+Preferences+-+Mail
        
        :returns: smtplib.SMTP
        """
        if self.__mail_host:
            
            import smtplib
            
            result = smtplib.SMTP(self.__mail_host, port=self.__mail_port)
            
            try:
                if self.__mail_user:
                    result.starttls()
                    result.login(self.__mail_user, self.__mail_password)
            except:
                logging.warning('Cannot login to mail server')
                raise
                
            return result
    
    def get_mail_from_address(self):
        """
        Get the address specified as the sender for automatic mail.
        
        @see http://doc.castsoftware.com/display/DOC82/CMS+-+Preferences+-+Mail 'Sender mail address'
        """
        return self.__mail_from
    
    def get_all_users_path(self):
        """
        see CastGlobalSettings.ini
        - CAST_ALL_USERS_PATH=%ALLUSERSPROFILE%\Application Data\CAST\CAST\$CAST_MAJOR_VERSION$.$CAST_MINOR_VERSION$
        """
        return self.__all_users_path
    
    def get_plugin_root_path(self):
        """
        .. versionadded:: 1.6.17
        """
        return self.__plugin_root_path
            
    class DependencyStrategy:
        """
        Handling of dependencies.
         
        We can have many other strategies, by coding it in python + api on extension folder.
        """
         
        # use the latest available
        latest = 1
        # use the minimum available
        minimal = 2
 
    
    def create_combined_schema(self, 
                               name, 
                               server, 
                               log_file_path=None, 
                               licence_key=None,
                               delivery_path=None, 
                               deploy_path=None,
                               extension_list=[], 
                               dependency_strategy=DependencyStrategy.minimal, 
                               all_users_dir=False, 
                               log_path=None, 
                               lisa_path=None, 
                               ltsa_path=None):
        """
        Create a combined install (triplet).
        
        :param name: name of the triplet
        :param log_file_path: a log file path : will be appended with _local.castlog, etc...
        
        :param extension_list: list of str or pair of str
        :param all_users_dir:bool if True will also install <all user dir> 
                                  compatibility extension. Kept for compatibility purpose
        :param log_path:str path for the log files
        :param lisa_path:str path for the lisa
        :param ltsa_path:str path for the ltsa
        
          extension_list=['com.castsoftware.python']
            --> will install latest available (on disk)
          extension_list=[('com.castsoftware.python', '1.0.0-beta1)]
            --> will install a specific version (if exists on disk)
        @todo: probably give the log when error happens
        """
        
        name = name.lower() # do not work otherwise
        
        extensions_text = self.__get_extension_text(extension_list, dependency_strategy, all_users_dir)
        log_file_path = os.path.abspath(log_file_path)
        
        try:
            self.create_knowledge_base(name + '_local', server, log_file_path + '_local.castlog', extensions_text)
            self.create_central_base(name + '_central', server, log_file_path + '_central.castlog', extensions_text)
            self.create_managment_base(name + '_mngt', server, log_file_path + '_mngt.castlog', extensions_text)
            self._ensure_cms_connection(server, name + '_mngt')
            
            if licence_key or delivery_path or deploy_path or log_path or lisa_path or ltsa_path:
                self.configure_platform_preference(server, 
                                                   name + '_mngt', 
                                                   key=licence_key, 
                                                   delivery_path=delivery_path,
                                                   deploy_path=deploy_path,
                                                   log_path=log_path,
                                                   lisa_path=lisa_path,
                                                   ltsa_path=ltsa_path)
            
        except Exception:
            
            # revert things done
            try:
                self.remove_schema(name + '_local', server)
            except:
                pass

            try:
                self.remove_schema(name + '_central', server)
            except:
                pass

            try:
                self.remove_schema(name + '_mngt', server)
            except:
                pass
            
            raise
        
        result = Combined(server, name)
        if delivery_path:
            self.update_dmt_plugins(result)
        
        return result

    def create_knowledge_base(self, name, server, log_file_path=None, extensions_text=''):

        self.create_cast_schema(name, server, 'local', log_file_path, packages="""
    <PackName>BASE_LOCAL</PackName>
    <PackName>ADG_LOCAL_APPW</PackName>
    <PackName>KMS_LOCAL</PackName>
    <PackName>KMS2_LOCAL</PackName>
        """, extensions_text=extensions_text)
        
    def create_central_base(self, name, server, log_file_path=None, extensions_text=''):
        
        self.create_cast_schema(name, server, 'central', log_file_path, packages="""
    <PackName>ADG_FULL_CENTRAL</PackName>        
        """, extensions_text=extensions_text)

    def create_managment_base(self, name, server, log_file_path=None, extensions_text=''):

        self.create_cast_schema(name, server, 'mngt', log_file_path, packages="""
    <PackName>PMC_MAIN</PackName>
        """, extensions_text=extensions_text)

    def download_extension(self, extension_id, extension_version=None, specific_server=None):
        """
        Try to download an extension from CAST servers.
        
        @param extension_id: id of the extension, e.g. com.castsoftware.jee
        @param extension_version: version of the extension, e.g. 1.4.0-funcrel, if not provided, will take the latest
        @param specific_server: a nuget server, if none will take a default one
        
        .. versionadded:: 1.5.26
        """
        downloader_exe = os.path.join(self.__path, 'ExtensionDownloader.exe')
        
        if specific_server:
            server = specific_server
        else:
            # choose the correct server due to convention
            if ".uc." in extension_id:
                server = "https://extend.castsoftware.com/uc"
            elif ".labs" in extension_id:
                server = "https://extend.castsoftware.com/labs"
            else:
                server = "https://extend.castsoftware.com/product" 
        
        
        def _download_extension_from_server(extension_id, specific_server, extension_version=None):
            """
            helper
            """
            if extension_version:
                rcode = subprocess.call([downloader_exe, "install", extension_id, "--version", extension_version, "--server", specific_server])
            else:
                rcode = subprocess.call([downloader_exe, "install", extension_id, "--server", specific_server])
            
            return rcode
        
        rcode = _download_extension_from_server(extension_id, server, extension_version)
        if rcode != 0:
            message = 'Could not download %s at version %s from server %s' %(extension_id, extension_version, server) if extension_version else 'Could not download %s from server %s' %(extension_id, server)
            raise RuntimeError(message)

    def get_enlighten_connection_profile(self, kb):
        """
        Try to find the name of a connection profile corresponding to _server or engine
        
        :param kb: KnowledgeBase
        
        .. versionadded:: 1.5.26
        """
        appdata = self.get_all_users_path()
        profile_path = os.path.join(appdata, "CWProfileConnection.INI")

        if not os.path.exists(profile_path):
            return
        
        return get_enlighten_connection_profile(profile_path, kb)

    def create_cast_schema(self, name, server, _type, log_file_path=None, extensions_text='', packages=''):
        """
        Create a knowledge base schema
        
        :param server: cast.application.server.Server
        :param name: name of the local
        :param log_file_path: log file path must ends with '.castlog'
        """
#         if not self.deployed:
#             raise RuntimeError("Cannot do this on a non deployed flat")
        
        engine = server.engine
        
        if engine.dialect.name != 'postgresql':
            raise RuntimeError('Operation available for CSS only')
        
        if log_file_path and not log_file_path.endswith('.castlog'):
            raise RuntimeError('log file path must ends with .castlog')
        
        # we need a schema
        if name in server._get_all_schemas():
            raise RuntimeError("schema '%s' already exists" % name)
        
        self.__ensure_servman_connection_profile(server)
        
        self._create_schema(name, engine)

        self.__run_servman(name, server, _type, log_file_path, extensions_text, packages)

    def __run_servman(self, name, server, _type, log_file_path=None, extensions_text='', packages=''):

        def _get_server_type(engine):
            
            m = {'postgresql':'CASTStorageService', 
                 'oracle':'Oracle' # @todo
                }
            return m[engine.dialect.name]
        
        engine = server.engine
        
        # connection is handled through server type, connection string and login/password only
        # no need for profile
        # it works after a certain version @todo find which one
        # @todo : check if that is the reason why I do not have cms connection profile...
        
        # generate temporary file
        xml_file_pattern = """<?xml version="1.0" encoding="iso-8859-1" ?>
<CAST-AutomaticInstall>
<ServerInstall ProfileSystem="%s" ServerType="%s" UserSystem="%s" SystemPassword="%s" ServerName="%s" >
  <InstallDatabase DbName="%s" >
    %s
    %s
  </InstallDatabase>
</ServerInstall>
</CAST-AutomaticInstall>
        """        
        
        xml_file_content = xml_file_pattern % (self.__get_profile_name(engine),
                                               _get_server_type(engine), 
                                               engine.url.username,
                                               engine.url.password,
                                               self.__get_profile_name(engine), 
                                               name,
                                               packages,
                                               extensions_text)
        
        # create temp file and execute servman
        temp_dir = tempfile.mkdtemp()
        path = os.path.join(temp_dir, "config_%s.xml" % _type)
        with open(path, 'w') as xml_config:
            xml_config.write(xml_file_content)
        
        try:
            servman_exe = os.path.join(self.__path, 'servman.exe')
            if not log_file_path:
                # generate a temp one
                log_file_path = os.path.join(temp_dir, "log_%s.castlog" % _type)
            rcode = subprocess.call([servman_exe, "-INSTALL_CONFIG_FILE(%s)" % path, "-LOG(%s)" % log_file_path])        
            
            if rcode != 0:
                errors = ''
                # error 
                # scan log for errors
                with open(log_file_path, mode='r') as log:
                    for line in log:
                        
                        if 'Error\a' in line:
                            errors += line.replace('\a', '\t') + '\n'
                
                raise RuntimeError("failed to install '%s' schema :\n%s" %(name, errors))
        finally:
            # remove temp
            shutil.rmtree(temp_dir, ignore_errors=True)
        # @todo perform sanity checks at the end for example, sys package versions ...

 
    def manage_extensions(self, 
                          name, 
                          server,
                          _type,
                          extension_list, 
                          log_file_path=None,
                          dependency_strategy=DependencyStrategy.minimal, 
                          all_users_dir=False):
        """
        So called manage extension.
        Add, upgrade, downgrade extensions.

        :param server: the server containgthe schema
        :parma name: name of the schema (xxx_local, xxx_mngt, xxx_central)
        :param extension_list: a list of extension id or extension id + version to install
        
        @todo: 
        - check compatibility of version between the caip and the schema !!!
        
        """
        if self.__version < '8.0.0':
            raise RuntimeError('Unsupported. Need at least CAIP 8.0.0')
         
        self.__run_servman(name, 
                           server, 
                           _type, 
                           log_file_path, 
                           self.__get_extension_text(extension_list, dependency_strategy, all_users_dir))        
        
    
    def __get_extension_text(self,
                             extension_list, 
                             dependency_strategy=DependencyStrategy.minimal, 
                             all_users_dir=False):
        
        
        extension_text = ''
        
        for extension in extension_list:
            
            if type(extension) is tuple:
                
                extension_text += '<Plugin id="%s" version="%s"/>\n' % (extension[0], extension[1])
            
            else:
                extension_text += '<Plugin id="%s"/>\n' % extension
                
        if not all_users_dir:
            
            extension_text += '<SkipLookupLegacyUADefaultLocation/>\n' 
            
        if dependency_strategy == self.DependencyStrategy.minimal:
        
            extension_text += '<InstallDependencies strategy="TakeMinimal"/>\n'

        elif dependency_strategy == self.DependencyStrategy.latest:
        
            extension_text += '<InstallDependencies strategy="TakeLatest"/>\n'
            
        return extension_text        
        
    def remove_schema(self, name, server):
        """
        Remove a knowledge base
        
        :param server: cast.application.server.Server
        """
        server.engine.execute(DropSchema(name, cascade=True))

    def configure_platform_preference(self, server, mngt_name, key=None, delivery_path=None, deploy_path=None, log_path=None, lisa_path=None, ltsa_path=None):
        """
        Set the licence key, delivery and deploy folder
        
        :param server: cast.application.server.Server
        :param mngt_name: name of the managment base
        :param key: str licence key
        :param delivery_path: str 
        :param deploy_path: str
        :param log_path: str path of the log (8.3.0 and above)
        :param lisa_path: str path of the temp (8.3.0 and above)
        :param ltsa_path: str path of the temp (8.3.0 and above)
        :raise RuntimeError: in case licence key is incorrect or CAIP version do not correspond to schema
        
        @todo chekc if CAIP version+build is correct regarding server+schema 
        --> no need because generates error ?
        
        """       
        castms_exe = os.path.join(self.__path, 'CAST-MS-CLI.exe')
        
        params = [castms_exe,
                  "ConfigurePlatformPreferences",
                  '-connectionProfile',
                  '%s' % CASTAIP.__get_cms_connection_profile_name(server, mngt_name) ]
        
        if key:
            params.append('-licenseKey')
            params.append('%s' % key)
        
        if delivery_path:
            params.append('-sourceDeliveryFolder')
            params.append('%s' % delivery_path)
        
        if deploy_path:
            params.append('-sourceDeploymentFolder')
            params.append('%s' % deploy_path)

        # options new to 8.3.0         
        if self.get_version() >= '8.3.0':
            
            if log_path:
                params.append('-logRootPath')
                params.append('%s' % log_path)
                params.append('-jobLogRootPath')
                params.append('%s' % log_path)
                
            if lisa_path:
                params.append('-workingPath')
                params.append('%s' % lisa_path)
                params.append('-storageWorkingPath')
                params.append('%s' % lisa_path)
            if ltsa_path:
                params.append('-temporaryPath')
                params.append('%s' % ltsa_path)
                params.append('-temporaryWorkingPath')
                params.append('%s' % ltsa_path)
        
        
        p = subprocess.Popen(params, 
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        _, err = p.communicate()   
        rcode = p.returncode
        
        if rcode != 0:
            raise RuntimeError(err)

    def update_dmt_plugins(self, combined_or_managment_schema, log_path=None):
        """
        Ensure that the delivery folder contains the DMT plugins from the extensions.
        
        @param combined_or_managment_schema: combined install or managment base
        @type combined_or_managment_schema: cast.application.ManagmentBase or cast.application.Combined

        .. versionadded:: 1.6.17
        """
        mngt = self._get_mngt(combined_or_managment_schema)
        # @type mngt:cast.application.ManagmentBase
        
        # special connection parameter for that command
        parameters = ['-allowInMemoryMigration', 
                      '-connectionString', 'LIBPQ:%s:%s'%(mngt.engine.url.host, mngt.engine.url.port),
                      '-connectionSchema',mngt.name,
                      '-connectionUser', mngt.engine.url.username,
                      '-connectionPassword', mngt.engine.url.password
                      ]
        
        self._execute_castms_command(mngt, 'UpdateDMTPlugins', parameters, log_path=log_path)    
        

    def create_application(self, combined_or_managment_schema, name, log_path=None):
        """
        Create a new application in DMT.

        @param combined_or_managment_schema: combined install or managment base
        @type combined_or_managment_schema: cast.application.ManagmentBase or cast.application.Combined

        @param name: name of the application to add
        
        @return: the added application
        @rtype: cast.application.DMTApplication

        .. versionadded:: 1.6.17
        """
        logger = logging.getLogger('cast.application')
        logger.info('Creating application %s on schema %s', name, str(combined_or_managment_schema))

        mngt = self._get_mngt(combined_or_managment_schema)
        delivery_path = mngt.get_delivery_path()
        deploy_path = mngt.get_deploy_path()
        
        result = DMTApplication(name)
        result.mngt = mngt
        result.delivery_path = delivery_path
        result.guid = str(uuid.uuid4())
        
        parameters = ['-appli', name,
                      '-appliGuid', result.guid,
                      '-sourceDeliveryFolder', delivery_path,
                      '-sourceDeploymentFolder', deploy_path
                      ]
        
        self._execute_castms_command(mngt, 'CreateEmptyApplication', parameters)    
        
        logger.info('Application %s created on schema %s', name, str(combined_or_managment_schema))
        
        return result
    
    def create_version(self, dmt_application, name, log_path=None):
        """
        Create a new version for a DMT application.
        
        @param dmt_application: the application on which we add a version
        @type dmt_application:cast.application.DMTApplication
        @param name: the name of the version
        
        @return: the added version
        @rtype: cast.application.DMTVersion

        .. versionadded:: 1.6.17
        """
        now = datetime.now()
        
        parameters = ['CreateVersionForServer',
                      '-application', dmt_application.name,
                      '-name', name,
                      '-releaseDate', now.strftime("%Y%m%d"),
                      '-storagePath', dmt_application.delivery_path
                      ]
        
        self._execute_dmt_command(parameters, log_path)
        
        return dmt_application.get_version(name)
    
    def create_source_package(self, dmt_version, name, folder_path):
        """
        Create a package for source files in a DMT version.
        
        @param dmt_version: The version on which adding the package
        @type dmt_version:cast.application.DMTVersion
        @param name: name of the package to add
        @param folder_path: path of the source folder
        
        @rtype: cast.application.DMTPackage
        
        @see https://doc.castsoftware.com/display/DOC83/Automating+source+code+delivery

        .. versionadded:: 1.6.17
        """
        
        parameters = ['CreatePackageForServer',
                      '-application', dmt_version.application.name,
                      '-versionName', dmt_version.name,
                      '-storagePath', dmt_version.delivery_path,
                      '-packageType', 'delivery.SourceFilesPackage',
                      '-extractorType', 'dmtdevfolderextractor.SourceFolderExtractor',
                      '-packageName', name,
                      '-folderPath', folder_path
                      ]
        
        self._execute_dmt_command(parameters)
        return dmt_version.get_package(name)

    def create_maven_http_package(self, dmt_version, name, repository_url='https://repo1.maven.org/maven2'):
        """
        Create a package for maven in a DMT version.
        
        Require installation of com.castsoftware.JEE-MavenHttp.
        
        @param dmt_version: The version on which adding the package
        @type dmt_version:cast.application.DMTVersion
        @param name: name of the package to add
        @param repository_url: url of the maven repository

        @rtype: cast.application.DMTPackage

        .. versionadded:: 1.6.17
        """
        
        parameters = ['CreatePackageForServer',
                      '-application', dmt_version.application.name,
                      '-versionName', dmt_version.name,
                      '-storagePath', dmt_version.delivery_path,
                      '-packageType', 'dmtdevjeemavenresourcesextractor.MavenResourceFilesPackage',
                      '-extractorType', 'dmtjeemavenhttpresourcesextractor.MavenHttpResourceExtractor',
                      '-packageName', name,
                      '-connectionURL', repository_url
                      ]
        
        self._execute_dmt_command(parameters)
        return dmt_version.get_package(name)
    
    def create_nuget_package(self, dmt_version, name, repository_url='https://api.nuget.org/v3/index.json'):
        """
        Create a package for nuget in a DMT version.
        
        Require installation of com.castsoftware.dmtdotnetnugetresourcesextractor.
        
        @param dmt_version: The version on which adding the package
        @type dmt_version:cast.application.DMTVersion
        @param name: name of the package to add
        @param repository_url: url of the nuget repository

        @rtype: cast.application.DMTPackage

        .. versionadded:: 1.6.17
        """
        
        parameters = ['CreatePackageForServer',
                      '-application', dmt_version.application.name,
                      '-versionName', dmt_version.name,
                      '-storagePath', dmt_version.delivery_path,
                      '-packageType', 'dmtdevmicrosofttechno.NetResourceFilesPackage',
                      '-extractorType', 'dmtdotnetnugetresourcesextractor.NugetExtractor',
                      '-packageName', name,
                      '-connectionURL', repository_url
                      ]
        
        self._execute_dmt_command(parameters)
        return dmt_version.get_package(name)
    
    def generate_version(self, dmt_version):
        """
        Launch extraction and discovery on a DMT version.
        
        @type dmt_version:cast.application.DMTVersion

        .. versionadded:: 1.6.17
        """
        
        parameters = ['Generate',
                      '-application', dmt_version.application.name,
                      '-version', dmt_version.name,
                      '-storagePath', dmt_version.delivery_path,
                      ]
        
        self._execute_dmt_command(parameters)

    def close_version(self, dmt_version, log_path=None):
        """
        After generate_version

        @param dmt_version: The version to close
        @type dmt_version:cast.application.DMTVersion

        .. versionadded:: 1.6.17
        """
        parameters = ['CloseVersion',
                      '-application', dmt_version.application.name,
                      '-version', dmt_version.name,
                      '-storagePath', dmt_version.delivery_path,
                      '-oneApplicationMode', dmt_version.application.guid
                      ]
        
        self._execute_dmt_command(parameters, log_path)

    def manage_application(self, dmt_application, log_path=None):
        """
        Manage the application in CASTMS.

        @param dmt_application: The application to manage
        @type dmt_application:cast.application.DMTApplication

        .. versionadded:: 1.6.17
        """
        mngt = dmt_application.mngt
        
        parameters = ['-appli', dmt_application.name]
        
        self._execute_castms_command(mngt, 'ManageAICPApplication', parameters)    

    def accept_delivery(self, dmt_version):
        """
        Accept a version in CASTMS.
        @type dmt_version:cast.application.DMTVersion

        .. versionadded:: 1.6.17
        """
        mngt = dmt_version.application.mngt

        parameters = ['-appli', dmt_version.application.name,
                      '-version', dmt_version.name,
                      ]
        
        self._execute_castms_command(mngt, 'AcceptDelivery', parameters)    

    def set_as_current_version(self, dmt_version):
        """
        Accept a version.  
        @type dmt_version:cast.application.DMTVersion

        .. versionadded:: 1.6.17
        """
        logger = logging.getLogger('cast.application')
        logger.info('Setting version %s as current version for application %s...', 
                    dmt_version.name,
                    dmt_version.application.name
                    )
        
        mngt = dmt_version.application.mngt

        parameters = ['-appli', dmt_version.application.name,
                      '-version', dmt_version.name,
                      ]
        
        self._execute_castms_command(mngt, 'SetAsCurrentVersion', parameters)
          
        logger.info('Version %s set as current version for application %s', 
                    dmt_version.name,
                    dmt_version.application.name
                    )
    
    def add_sql_dependency(self, dmt_application):
        """
        Add dependencies from following technologies to any SQL analysis unit
        'MAINFRAME', 'CPP', 'DOTNET', 'JEE'

        @param dmt_application: The application
        @type dmt_application:cast.application.DMTApplication

        .. versionadded:: 1.6.17
        """
        logger = logging.getLogger('cast.application')
        logger.info('Adding SQL dependencies for application %s...', str(dmt_application.name))
        
        mngt = dmt_application.mngt

        temp_dir = tempfile.mkdtemp()
        path = os.path.join(temp_dir, "AddDependenciesToSQLAnalyzer.groovy")
        with open(path, 'w') as script:
            script.write(add_dependency_script)

        parameters = ['-file', path,
                      '-param0', dmt_application.name]
        try:
            self._execute_castms_command(mngt, 'ExecuteScript', parameters)        
            logger.info('Dependencies added for application %s', str(dmt_application.name))
        finally:
            # remove temp folder
            shutil.rmtree(temp_dir, ignore_errors=True)
            
    def run_analysis(self, dmt_application, amt_memory_profile=False):
        """
        Run analysis.  
        @param dmt_application: The application on which running analysis
        @type dmt_application:cast.application.DMTApplication

        .. versionadded:: 1.6.17
        """
        logger = logging.getLogger('cast.application')
        logger.info('Running analysis for application %s...', str(dmt_application.name))
        
        mngt = dmt_application.mngt

        parameters = ['-appli', dmt_application.name]
        
        if amt_memory_profile:
            parameters += ['-activateAmtMemoryProfile', 'true']
        
        self._execute_castms_command(mngt, 'RunAnalysis', parameters)        
        logger.info('Analysis done for application %s', str(dmt_application.name))

    def prepare_snapshot(self, dmt_application):
        """
        Snapshot preparation. 
        @type dmt_application:cast.application.DMTApplication

        .. versionadded:: 1.6.17
        """
        logger = logging.getLogger('cast.application')
        logger.info('Prepare snapshot for application %s...', str(dmt_application.name))
        
        mngt = dmt_application.mngt

        parameters = ['-appli', dmt_application.name]
        
        self._execute_castms_command(mngt, 'PrepareSnapshot', parameters)        
        logger.info('Preparation done for application %s', str(dmt_application.name))

    def generate_snapshot(self, dmt_application, snapshot_name, version_name=None, capture_date=None):
        """
        Generate snapshot
        
        @param dmt_application: The application on which generating a snapshot
        @type dmt_application:cast.application.DMTApplication
        @param snapshot_name: Name of the snapshot. It must be unique for a given Application in a given Dashboard Service.
        @param version_name: Name of the version that will appear in the dashboard. (unrelated to the version in DMT/CASTMS).
                             Default is snapshot_name
        @param capture_date: string, '20231226', default is today.

        .. versionadded:: 1.6.17
        """
        logger = logging.getLogger('cast.application')
        logger.info('Generating snapshot for application %s...', str(dmt_application.name))
        
        mngt = dmt_application.mngt

        parameters = ['-appli', dmt_application.name,
                      '-snapshot', snapshot_name]
        
        if not version_name:
            version_name = snapshot_name
        
        if not capture_date:
            today = date.today()
            capture_date = today.strftime('%Y%m%d')

        if capture_date:
            parameters += ['-captureDate', capture_date]

        if version_name:
            parameters += ['-version', version_name]

        self._execute_castms_command(mngt, 'GenerateSnapshot', parameters)        
        logger.info('Snapshot done for application %s', str(dmt_application.name))
    
    def automate_delivery(self, dmt_version, name, log_path=None):
        """
        Clones a dmt_version, generate, close, accept, set as current version  
        @type dmt_version:cast.application.DMTVersion

        .. versionadded:: 1.6.17
        """
        mngt = dmt_version.application.mngt

        parameters = ['-appli', dmt_version.application.name,
                      '-version', name,
                      '-fromVersion', dmt_version.name
                      ]
        
        self._execute_castms_command(mngt, 'AutomateDelivery', parameters)
    
    def upload_source_in_local(self, dmt_application):
        """
        Upload the source code in local. 
        @type dmt_application:cast.application.DMTApplication

        .. versionadded:: 1.6.18
        """
        logger = logging.getLogger('cast.application')
        logger.info('Uploading source in local for application %s...', str(dmt_application.name))
        
        mngt = dmt_application.mngt

        parameters = ['-appli', dmt_application.name]
        
        self._execute_castms_command(mngt, 'UploadSourcesInLocal', parameters)        
        logger.info('Source uploaded done for application %s', str(dmt_application.name))
    
    def _get_mngt(self, combined_or_managment_schema):
        try:
            return combined_or_managment_schema.get_managment()
        except:
            return combined_or_managment_schema
    
    def _execute_dmt_command(self, parameters, log_path=None):
        
        temp_dir = tempfile.mkdtemp()
        if not log_path:
            log_path = os.path.join(temp_dir, "log.log")
 
        dmt_exe = os.path.join(self.__path, 'DeliveryManagerTool', 'DeliveryManagerTool-CLI.exe')
        
        params = [dmt_exe] + parameters + ['-logFilePath', '%s' % log_path]
        
        logger = logging.getLogger('cast.application')
        logger.info('Executing command %s', ' '.join(params))

        p = subprocess.Popen(params, 
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        _, err = p.communicate()   
        rcode = p.returncode
        
        shutil.rmtree(temp_dir, ignore_errors=True)
        if rcode != 0:
            raise RuntimeError(err)
        
    
    def _execute_castms_command(self, mngt, command, parameters, log_path=None):
        """
        In order to have real options/command
        CAST-MS-CLI.exe -help true
        """
        server = Server.get_server(mngt.engine)
        castms_exe = os.path.join(self.__path, 'CAST-MS-CLI.exe')
        
        params = [castms_exe,
                  command,
                  '-connectionProfile',
                  '%s' % CASTAIP.__get_cms_connection_profile_name(server, mngt.name),
                  ]
        params += parameters
        
        if log_path:
            params += ['-logFilePath', log_path]

        logger = logging.getLogger('cast.application')
        logger.info('Executing command %s', ' '.join(params))
        
        # removing PYTHONPATH/PYTHONHOME 
        # see https://cast-products.atlassian.net/browse/AIPCORE-4992
        local_environment = dict(os.environ)
        try:
            local_environment.pop('PYTHONPATH')
        except KeyError:
            pass
        try:
            local_environment.pop('PYTHONHOME')
        except KeyError:
            pass

        p = subprocess.Popen(params, 
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             env=local_environment)
        _, err = p.communicate()   
        rcode = p.returncode
        
        if rcode != 0:
            raise RuntimeError(err)
        
        
    def _execute_groovy_script(self, server, mngt_name, script_content, log_path=None):
        """
        """
         
        temp_dir = tempfile.mkdtemp()
        path = os.path.join(temp_dir, "script.groovy")
        with open(path, 'w') as script:
            script.write(script_content)
         
        if not log_path:
            log_path = os.path.join(temp_dir, "log.log")
 
        dmt_exe = os.path.join(self.__path, 'DeliveryManagerTool', 'DeliveryManagerTool-CLI.exe')
         
        params = [dmt_exe,
                  "ExecuteScript",
                  '-connectionProfile',
                  '%s' % CASTAIP.__get_cms_connection_profile_name(server, mngt_name),
                  '-file',
                  '%s' % path,
                  '-logFilePath',
                  '%s' % log_path,
                 ]
         
        p = subprocess.Popen(params, 
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        _, err = p.communicate()   
        rcode = p.returncode
         
        shutil.rmtree(temp_dir, ignore_errors=True)
        if rcode != 0:
            raise RuntimeError(err)
        

        
    def _create_schema(self, name, engine):
        """
        Create a database schema.
        """
        engine.execute(CreateSchema(name))
                        
    def _ensure_cms_connection(self, server, mngt_name):
        """
        Create an entry (if necessary) in the cast-ms.connectionProfiles.pmx file.
        """
        engine = server.engine

        if engine.dialect.name != "postgresql":
            raise RuntimeError("Not implemented")
        
        file_path = os.path.join(self.__user_folder, 'cast-ms.connectionProfiles.pmx')

        if not os.path.exists(file_path):
            # create one if not exists (folder can be missing too)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(filename, "w") as f:
                f.write("""
<?xml version='1.0' encoding='utf-8'?>
<document version="1.1">
 <lot label="Connection profiles" requires="connectionprofiles:2.1;pmcgeneral:3.1;system:1.0" symbol="connectionProfiles">
  <connectionprofiles.ConnectionProfiles>
   <connectionProfiles>
  </connectionprofiles.ConnectionProfiles>
 </lot>
</document>""")
        
        tree = eTree.parse(file_path)
        root = tree.getroot()
        lot = next(iter(root))
        profiles1 = next(iter(lot))
        profiles2 = next(iter(profiles1))
        
        
        _type = 'connectionprofiles.ConnectionProfilePostgres'
        _p = 'CRYPTED2:' + set_message(engine.url.password)
        
        for connection in profiles2:
            try:
                if connection.tag == _type and connection.attrib['password'] == _p and \
                   connection.attrib['user'] == engine.url.username and connection.attrib['schema'] == mngt_name and \
                   connection.attrib['host'] == engine.url.host and connection.attrib['port'] == str(engine.url.port):
                    
                    # already existing : nothing to do
                    return
            except KeyError:
                # it may happen sometimes that a line is incomplete
                # skip
                pass
                
        # add it
        _uuid = 'uuid:'+ str(uuid.uuid4())
        profiles2.append(eTree.Element(_type, 
                                       {'entry':_uuid,
                                        'host':engine.url.host,
                                        'schema':mngt_name,
                                        'port':str(engine.url.port),
                                        'user':engine.url.username,
                                        'name':CASTAIP.__get_cms_connection_profile_name(server, mngt_name),
                                        'password':_p}))
            
        # write back
        tree.write(file_path, encoding='utf-8', xml_declaration=True)
    
    @staticmethod
    def __get_cms_connection_profile_name(server, mngt_name):
        
        return mngt_name + ' on CastStorageService _ ' + server.engine.url.host + ':' + str(server.engine.url.port)
    
    def __ensure_servman_connection_profile(self, server):
        """
        Ensure that we have a servman connection profile to engine.

        @deprecated but still usefull 
        @see : https://confluence.castsoftware.com/display/TG/Server+Manager+-+Information+-+Connection+Profile+Path+and+file
        """
        engine = server.engine
        
        dialect = engine.dialect.name
        
        if dialect != "postgresql":
            raise RuntimeError("Not implemented")
        # too bad guys...
        
        appdata = self.get_all_users_path()
        
        if not os.path.exists(appdata):
            os.makedirs(appdata)

        profile_name = self.__get_profile_name(engine)
        
        servman_profile_path = os.path.join(appdata, "CWSIProfileConnection.INI")
        available = False
        
        with open(servman_profile_path, 'r') as servman_profile:
            # search [profile_name]
            for line in servman_profile.readlines():
                if ('[' + profile_name + ']') in line:
                    available = True
        
        if not available:
            servman_profile_write = open(servman_profile_path, 'a')
            servman_profile_write.write("""[%s]
1=s%s
3=s%s
2=s%s:%s
54=i1
41=i22
39=b0
55=sLIBPQ:%s:%s
13=i4
8=i303
9=i303
10=b1
38=s%s
""" % (profile_name, profile_name, engine.url.username, engine.url.host, engine.url.port, engine.url.host, engine.url.port, Logger().set_message(engine.url.password)))
    
    def __read_cms_preferences(self):
        """
        cast-ms.preferences.pmx
        """
        try:
            tree = eTree.parse(os.path.join(self.__user_folder, 'cast-ms.preferences.pmx'))
            root = tree.getroot()
            
            lot = next(iter(root))
            
            for preference in lot:
                
                if preference.tag == 'preferences.Preferences':
                    
                    try:
                        self.__lisa_path = preference.attrib['workingPath']
                    except:
                        pass
    
                    try:
                        self.__ltsa_path = preference.attrib['temporaryPath']
                    except:
                        pass
    
                    try:
                        self.__log_root_path = preference.attrib['logRootPath']
                    except:
                        pass
    
                else:
                    try:
                        self.__mail_host = preference.attrib['host']
                    except:
                        pass
            
                    try:
                        self.__mail_port = preference.attrib['port']
                    except:
                        pass
            
                    try:
                        self.__mail_from = preference.attrib['from']
                    except:
                        pass
                    
                    for credential in preference:
                        for credential_preference in credential:
                            
                            try:
                                self.__mail_user = credential_preference.attrib['user']
                            except:
                                pass
    
                            try:
                                self.__mail_password = get_message(credential_preference.attrib['password'][9:])
                            except:
                                pass        
        except FileNotFoundError:
            # when user did not ever ran CMS
            pass
        
    def __read_cwbin(self):
        """
        Extract version from cw.bin
        """
        with open(os.path.join(self.__path, 'cw.bin'), "rb") as cwbin:
            
            versionString = ''
            fileBytes = cwbin.read()
            index = 18
            while True:
                
                current = chr(fileBytes[index]-100)
                if str.isdigit(current) or current == '.':
                    versionString += current;
                else:
                    break
                index += 1
            
            self.__version = StrictVersion(versionString)
            
    def __read_ini(self):
        """
        Read CastGlobalSettings.ini to get some variables
        """
        
        values = {'CAST_CURRENT_USER_WORK_PATH':'%APPDATA%\CAST\CAST\$CAST_MAJOR_VERSION$.$CAST_MINOR_VERSION$\\',
                  'CAST_ALL_USERS_PATH':r'%ProgramData%\CAST\CAST\$CAST_MAJOR_VERSION$.$CAST_MINOR_VERSION$\\',
                  'CAST_CURRENT_USER_TEMP_PATH':r'%TEMP%\CAST\CAST\$CAST_MAJOR_VERSION$.$CAST_MINOR_VERSION$',
                  'CAST_PROGRAM_FILES_COMMON_PATH':r'%CommonProgramFiles%\CAST\CAST\$CAST_MAJOR_VERSION$.$CAST_MINOR_VERSION$',
                  'CAST_PROGRAM_FILES_COMMON_UNVERSIONED_PATH':r'%CommonProgramFiles%\CAST\CAST',
                  'CAST_PLUGINS_ROOT_PATH':r'%ProgramData%\CAST\CAST\Extensions'
                  }
        
        with open(os.path.join(self.__path, 'CastGlobalSettings.ini')) as settings:
            
            for line in settings:
                
                if not line.startswith('CAST_'):
                    continue
                value = line[line.find('=')+1:].strip()

                if line.startswith('CAST_CURRENT_USER_WORK_PATH'):
                    values['CAST_CURRENT_USER_WORK_PATH'] = value           

                if line.startswith('CAST_ALL_USERS_PATH'):
                    values['CAST_ALL_USERS_PATH'] = value           

                if line.startswith('CAST_CURRENT_USER_TEMP_PATH'):
                    values['CAST_CURRENT_USER_TEMP_PATH'] = value           

                if line.startswith('CAST_PROGRAM_FILES_COMMON_PATH'):
                    values['CAST_PROGRAM_FILES_COMMON_PATH'] = value           

                if line.startswith('CAST_PROGRAM_FILES_COMMON_UNVERSIONED_PATH'):
                    values['CAST_PROGRAM_FILES_COMMON_UNVERSIONED_PATH'] = value           

                if line.startswith('CAST_PLUGINS_ROOT_PATH'):
                    values['CAST_PLUGINS_ROOT_PATH'] = value           


        
        def expand(text):
        
            text = text.replace('$CAST_MAJOR_VERSION$', str(self.__version.version[0]))
            text = text.replace('$CAST_MINOR_VERSION$', str(self.__version.version[1]))
            text = os.path.expandvars(text)
            return text
            
        self.__user_folder = expand(values['CAST_CURRENT_USER_WORK_PATH'])
        self.__all_users_path = expand(values['CAST_ALL_USERS_PATH'])

        self.__current_user_temp_path = expand(values['CAST_CURRENT_USER_TEMP_PATH'])
        self.__common_path = expand(values['CAST_PROGRAM_FILES_COMMON_PATH'])
        self.__common_unversionned_path = expand(values['CAST_PROGRAM_FILES_COMMON_UNVERSIONED_PATH'])
        self.__plugin_root_path = expand(values['CAST_PLUGINS_ROOT_PATH'])

    @staticmethod
    def __get_profile_name(engine):
    
        return "%s:%s" % (engine.url.host, engine.url.port)
        
    def __repr__(self):
        
        return 'CAIP(%s, %s)' % (self.__path, self.__version)
        
        
def read_enlighten_connection_profiles(path):
    """
    Read a CWProfileConnection.INI to extract the connection informations
    
    returns a list of tuple : engine, schema name
    :param path: path of the file to read
    
    For now: postgresql only 
    """
    config = configparser.ConfigParser()
    config.read(path)
    
    result = []
    try:
        for section in config.sections():
    
            connection_string = config.get(section, '55')[1:]
            if not connection_string.startswith('LIBPQ'):
                continue
            
            server_port = connection_string.split(',')[0].split(':')[1:]
            
            if len(server_port) == 2:
                server, port = server_port
            elif len(server_port) == 1:
                server = server_port[0]
                port = 2280 # not sure here 
            
            user = config.get(section, '3')[1:]
            cp = config.get(section, '38')[1:]
            password = Logger().get_message(cp)
            schema = config.get(section, '27')[1:]
            result.append((create_postgres_engine(host=server, port=int(port), user=user, password=password), schema))
    except:
        pass
    return result


def get_enlighten_connection_profile(path, kb):
    """
    Read a CWProfileConnection.INI and find the connection name.
    
    returns str
    :param path: path of the file to read
    :param kb: KnowledgeBase
    
    For now: postgresql only 
    """
    url = kb.engine.url
    
    config = configparser.ConfigParser()
    config.read(path)
    
    try:
        for section in config.sections():
    
            connection_string = config.get(section, '55')[1:]
            if not connection_string.startswith('LIBPQ'):
                continue
            
            server_port = connection_string.split(',')[0].split(':')[1:]
            
            if len(server_port) == 2:
                server, port = server_port
            elif len(server_port) == 1:
                server = server_port[0]
                port = 2280 # not sure here 
            
            user = config.get(section, '3')[1:]
            cp = config.get(section, '38')[1:]
            password = Logger().get_message(cp)
            schema = config.get(section, '27')[1:]
            
            if (server, int(port), user, schema) == (url.host, url.port, url.username, kb.name):
                return section
    except:
        pass
    return None


def read_servman_connection_profiles(path):
    """
    Read a CWSIProfileConnection.INI to extract the connection informations
    
    returns a list of engine
    :param path: path of the file to read
    
    For now: postgresql only
    """
    config = configparser.ConfigParser()
    config.read(path)
    
    result = []
    
    for section in config.sections():

        connection_string = config.get(section, '55')[1:]
        if not connection_string.startswith('LIBPQ'):
            continue
        
        server, port = connection_string.split(',')[0].split(':')[1:]
        
        user = config.get(section, '3')[1:]
        cp = config.get(section, '38')[1:]
        password = Logger().get_message(cp)
#         print(server, port, user, password)
        result.append(create_postgres_engine(host=server, port=int(port), user=user, password=password))

    return result


def generate_set_id(application, set_name):

    kb = application.kb
    kb._ensure_additional_tables()
    
    # get the id
    subset_id = None
    query = select([kb.pmc_subsets.c.subset_id]).where(kb.pmc_subsets.c.subset_name == set_name)
    for o in kb._execute_sqlalchemyquery2(query):
        subset_id = o[0]
        
    if not subset_id:
        # create a new one
        query = select([func.max(kb.pmc_subsets.c.subset_id)])
        result = kb.engine.execute(query)
        max_id = result.fetchone()[0]
        if max_id:
            subset_id = max_id + 1
        else:
            subset_id = 1
        ins = kb.pmc_subsets.insert().values(subset_name = set_name, subset_id=subset_id)
        result = kb.engine.execute(ins)
        
    else:
                  
        # clear the set
        d = kb.pmc_subset_objects.delete().where(kb.pmc_subset_objects.c.subset_id==subset_id)
        kb.engine.execute(d)
    
    
    return subset_id


def _get_in_project(project_list_or_application):
    """
    Return an 'inable' for idpro in (...)
        
    """
    
    if type(project_list_or_application) is list:
        return project_list_or_application
    
    application = project_list_or_application
    # @type application: cast.application.Application
    kb = application.kb
    # @type kb: cast.application.KnowledgeBase
    
    UsrProRoot = reflect_table('UsrProRoot', kb.metadata, kb.engine)
    query_usr_pro_root = select([UsrProRoot.c.idroot]).where(UsrProRoot.c.idusrpro == application.id)
    
    ProDep = reflect_table('ProDep', kb.metadata, kb.engine)
    query1 = select([ProDep.c.idpro], distinct=True).where(ProDep.c.idpromain.in_(query_usr_pro_root))
    # select distinct(IdPro) from ProDep where IdProMain in (select IdRoot from UsrProRoot where IdUsrPro = %s)
    
    ProRoot = reflect_table('ProRoot', kb.metadata, kb.engine)
    query2 = select([ProRoot.c.idpro], distinct=True).where(ProRoot.c.idroot.in_(query_usr_pro_root))
    # select distinct(IdPro) from ProRoot where IdRoot in(select IdRoot from UsrProRoot where IdUsrPro = %s)
    
    return query1.union(query2)
    
    
def get_ssl_connection_arguments(host, port):
    
    result = {}
    
    path = os.environ.get("CASTCONNECTIONEXTRAPARAMETERS")
    
    if not path:
        return result
    
    searched_section = '%s:%s' % (host.lower(), port)
    
    config = configparser.ConfigParser()
    config.read(path)
    
    for section in config.sections():

        if section.lower() != searched_section.lower():
            continue
        
        ssl_enabled = config.get(section, 'ssl')
        
        if ssl_enabled == 'false':
            return result
        
        result['ssl'] = {'cert_reqs':ssl.CERT_REQUIRED}
        
        try:
            result['ssl']['ca_cert'] = config.get(section, 'ssLrootcert')
        except KeyError:
            pass
        
        try:
            result['ssl']['certfile'] = config.get(section, 'sslcert')
        except KeyError:
            pass

        try:
            result['ssl']['keyfile'] = config.get(section, 'sslkey')
        except KeyError:
            pass

        try:
            result['ssl']['ssl-mode'] = config.get(section, 'sslmode')
        except KeyError:
            pass
        
        break
    
    return result

def _get_guid_from_dmt_index(folder_path, name):
    
    file_path = os.path.join(folder_path, 'index.xml')
    tree = eTree.parse(file_path)
    root = tree.getroot()
    
    for entry in root:
        if entry.tag == 'entry' and entry.attrib['key'].endswith('_name') and entry.text == name:
            uuid = entry.attrib['key'].split('_name')[0]
            return uuid


# taken from http://jnk-centos-git/tools/maintenance/-/blob/master/Tools/GROOVY/AddDependenciesToSQLAnalyzer/src/AddDependenciesToSQLAnalyzer.groovy    
add_dependency_script = """/**
 * CAST Maintenance : add dependencies from a set of technologies to all SQL Analyzer analysis units
 * JEE, DotNet, CPP, Mainframe 
 * @author SFR
 * Auguqr 2019
 * 
 * Version 1.1
 */

def APPLICATION_NAME = null;
def SOURCE_TECHNOLOGIES = null;
def CAST_VERSION = checkVersion();

if (null == CAST_VERSION)
{
    APPLICATION_NAME = param0;
    SOURCE_TECHNOLOGIES = param1.split(',');
}
else
{
    APPLICATION_NAME = CAST_getGroovyValue("APPLICATION_NAME", "applicationName", "param0");
    SOURCE_TECHNOLOGIES = CAST_getGroovyValue("SOURCE_TECHNOLOGIES", "sourceTechnologies", "param1"); 
}

String [] DEFAULT_SOURCE_TECHNOS = [ 'MAINFRAME', 'CPP', 'DOTNET', 'JEE' ];

ArrayList<String> eligibleTechnos = null;

// Checks parameters...
if (APPLICATION_NAME == null)
{
    println "Parameter not set to the application name, process aborted";

    return;
}

// Check application...
def application = cms.pmcportfolio.Application.entities.find( { it.name == APPLICATION_NAME; } );

if (application == null)
{
    println "application " + APPLICATION_NAME + " not found, process aborted";

    return;
}

Object targetTechhology = null;

try
{
    targetTechnology = findApplicationTechno(application, "UA");
    
    if (null == targetTechnology)
        throw new Exception ("No universal analyzer")
}    
catch(Exception ex)
{
    println("The application entered as first parameter does not contain the Universal Analyzer Technology");
    return;
}

// Check presence of technologies in application
List<Object> targets = findSQLAnalyzerAnalysisUnits(application);

if (targets.isEmpty())
{
    println("The application entered as first parameter does not contain any SQL Analyzer Analysis Unit");
    return;
}

if (SOURCE_TECHNOLOGIES == null)
{
    println "Source Technologies not set, defaulting to [CPP, DOTNET, J2EE, MAINFRAME]";
    eligibleTechnos = Arrays.asList(DEFAULT_SOURCE_TECHNOS);
}
else
{
    eligibleTechnos = Arrays.asList(SOURCE_TECHNOLOGIES);
}

List<Object> sources = new ArrayList<Object>();

for (Object technology : eligibleTechnos)
{
    try
    {
        sourceTechnology = findApplicationTechno(application, technology);
        if (null != sourceTechnology)
        {
          println(technology + " found in the application");
          sources.add(sourceTechnology);
        }
        else
            throw new Exception(technology+" not found");
    }
    catch(Exception ex)
    {
        println(technology + " not found in the application");
    }
}

if (sources.isEmpty())
{
    println("No eligible source technology found in the application, process aborting");
    return;
}

for (Object src : sources)
{
    for (Object au : targets)
    {
        def dependency = application.dependencies.find( {it != null && it.source == src && it.target == au} );     
        
        if (null == dependency)
        {
            dependency = application.do_dependencies_add(cms.techno.StandardDependency);
            dependency.source = src;
            dependency.target = au
            println("Added a dependency from techonology " + src.name + " to Analysis Unit " + au.name);
        }
    }
}

def findSQLAnalyzerAnalysisUnits(application){
    // Find SQL Analyzer analysis units
    List<Object> SQLAnalysisUnits = new ArrayList<Object>();
    application.codeResources.each{
        def packageResource = it
        it.analysisUnits.each(){
            if(it.meta_type == cms.universalanalysis.UAAnalysisUnit){
                def analysisUnit = it
                // println("Inspecting Analysis unit : " + analysisUnit.name);
                def language = analysisUnit.languages.find({it != null && it.name ==  "SQL"; } )
                if (null != language){
                    println("Found a SQL Analysis Unit : " + analysisUnit.name);
                    SQLAnalysisUnits.add(analysisUnit);
                }
            }
        }
    }
    return SQLAnalysisUnits;
}


def findApplicationTechno(application, techno) {
        def technoMap = [
            "ABAP": cms.sapanalysis.SAPAppTechnology,
            "ZOS": cms.dbtwoserver.DBZOSAppTechnology,
            "UDB": cms.dbtwoserver.DBUDBAppTechnology,
            "ORACLE": cms.oracleserveranalysis.OracleAppTechnology,
            "MS SQL": cms.sqlserveranalysis.SqlServerAppTechnology,
            "SYBASE": cms.sqlserveranalysis.SybaseAppTechnology,
            "ASP": cms.aspanalysis.ASPAppTechnology,
            "BO": cms.boanalysis.BOAppTechnology,
            "CPP": cms.cppanalysis.CPPAppTechnology,
            "DOTNET": cms.dotnetanalysis.NetAppTechnology,
            "FORMS": cms.forms.FORMSAppTechnology,
            "J2EE": cms.j2eeanalysis.J2EEAppTechnology,
            "JEE": cms.j2eeanalysis.J2EEAppTechnology,
            "MAINFRAME": cms.mainframeanalysis.MainframeAppTechnology,
            "PB": cms.pbanalysis.PBAppTechnology,
            "UA": cms.universalanalysis.UAAppTechnology,
            "VB": cms.vbanalysis.VBAppTechnology
        ]
        if (technoMap[techno] == null) {
            throw new Exception('Unknown Application Technology : ' + techno)
        }
        return application.technologies.find({
            return it.meta_type == technoMap[techno]
        });
}

def checkVersion()
{
    Binding binding = getBinding();
    if (binding.hasVariable('cliVersion'))
    {
        println ("Using CAST-AIP version " + cliVersion);
        return cliVersion;
    }
    else
    {
        return null;
    }
}"""


def get_expiration_date(license_key):
    """
    Given a license key return the expiration date 
    """
    text = license_key.split(':')[2]
    if text == 'Unlimited':
        return date.max # infinity
    year = int(text[:4])
    month = int(text[4:6])
    day = int(text[6:])
    return date(year, month, day)
    

def patch_kb(kb):
    """
    Will be executed on kb 
    - at construction in case of
      - recent CAIP core api
      - interactive code
    - during api upgrade in case of previous CAIP core api
    """    
    
