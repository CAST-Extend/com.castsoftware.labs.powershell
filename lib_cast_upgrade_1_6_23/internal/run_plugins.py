"""
Main entry point for application level plugins.

"""
import argparse
import sys
import logging
import traceback
from cast.application.internal.find_plugins import find_cast_plugins, call_application_level_extensions, get_plugins, analysis_has_warnings
from cast.application import KnowledgeBase, create_postgres_engine, create_oracle_engine, create_sqlserver_engine
from cast.application.internal import set_current_application, is_debug_log, set_report_path, set_current_event, _create_xml_report_file
from cast.application.managment import ManagmentBase
from cast.application.server import Server
import warnings
from sqlalchemy import exc as sa_exc


def parse_arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument('--log', help="output log file path", required=True)
    parser.add_argument('--application', help="application name")
    parser.add_argument('--castdirectory', help="CAIP installation directory")
    parser.add_argument('--event', help="event to trigger")
    parser.add_argument('--temporary', help="temporary folder for application")
    parser.add_argument('--intermediate', help="intermediate folder for application")

    parser.add_argument('--user', help="knowledge base connection user", default=None)
    parser.add_argument('--password', help="knowledge base connection password", default=None)
    parser.add_argument('--trusted', help="Use trusted connection for sqlserver", dest='trusted', action='store_true')
    parser.set_defaults(trusted=False)

    parser.add_argument('--database', help="knowledge base database type", choices=['postgresql', 'oracle', 'sqlserver'], default='postgresql')
    
    parser.add_argument('--host', help="knowledge base host")
    parser.add_argument('--port', help="knowledge base port", default=None, type=int)
    parser.add_argument('--instance', help="knowledge instance port", default=None)
    
    parser.add_argument('--sid', help="knowledge base sid (oracle)", default=None)
    parser.add_argument('--service', help="knowledge instance service", default=None)

    parser.add_argument('--kb-database-name', help='knowledge base database name (postgresql)', dest='kb_database_name', default='postgres')

    parser.add_argument('--schema', help="knowledge base name")

    parser.add_argument('--report-path', help="Path to generate the report to", dest='report_path', default=None)

    # mngt
    parser.add_argument('--mngt-user', help="mngt base connection user", dest='mngt_user', default=None)
    parser.add_argument('--mngt-password', help="mngt base connection password", dest='mngt_password', default=None)
    parser.add_argument('--mngt-trusted', help="Use trusted connection for sqlserver", dest='mngt_trusted', action='store_true')
    parser.set_defaults(mngt_trusted=False)

    parser.add_argument('--mngt-database', help="mngt base database type", dest='mngt_database', choices=['postgresql', 'oracle', 'sqlserver'], default='postgresql')
    
    parser.add_argument('--mngt-host', help="mngt base host", dest='mngt_host')
    parser.add_argument('--mngt-port', help="mngt base port", dest='mngt_port', default=None, type=int)
    parser.add_argument('--mngt-instance', help="mngt instance port", dest='mngt_instance', default=None)
    
    parser.add_argument('--mngt-sid', help="mngt base sid (oracle)", dest='mngt_sid', default=None)
    parser.add_argument('--mngt-service', help="mngt instance service", dest='mngt_service', default=None)

    parser.add_argument('--mngt-database-name', help='mngt base database name (postgresql)', dest='mngt_database_name', default='postgres')

    parser.add_argument('--mngt-schema', help="mngt base name", dest='mngt_schema')
    


    return parser.parse_args()


def main():
    
    try:
        args = parse_arguments()
        # get rid of annoying warning
        warnings.simplefilter("ignore", category=sa_exc.SAWarning)
        
        file = open(args.log, 'w')
        file.write('Timestamp\a\tLevel\a\tTopic\a\tBody\a\tWho\a\tError Number\a\tRuntime File\a\tLine\a\tModule\a\tSource Line\a\tSource Column\a\tRuntime Context\a\tSource\n')
        file.close()
        
        # get the log level...
        level = logging.INFO
        if is_debug_log():
            level = logging.DEBUG
        
        
        FORMAT = ' %(asctime)-15s \a\t%(levelname)s\a\tMODULMSG ; Body\a\t%(message)s'
        logging.basicConfig(filename=args.log,
                            filemode='a+',
                            format=FORMAT,
                            level=level)
        
        set_report_path(args.report_path)
        
        logging.info("Running Extensions at application level  ...")
        
        logging.info("Connecting to knowledge base ...")

        kb_engine = None
        
        if args.database == 'postgresql':
            kb_engine = create_postgres_engine(args.user, args.password, args.host, args.port, args.kb_database_name)
        elif args.database == 'oracle':
            kb_engine = create_oracle_engine(args.user, args.password, args.host, args.port, args.sid, args.service)
        elif args.database == 'sqlserver':
            kb_engine = create_sqlserver_engine(args.user, args.password, args.host, None, args.port, args.instance, args.trusted)
        
        mngt_engine = None
        if args.mngt_schema:
            if args.database == 'postgresql':
                mngt_engine = create_postgres_engine(args.mngt_user, args.mngt_password, args.mngt_host, args.mngt_port, args.mngt_database_name)
            elif args.database == 'oracle':
                mngt_engine = create_oracle_engine(args.mngt_user, args.mngt_password, args.mngt_host, args.mngt_port, args.mngt_sid, args.mngt_service)
            elif args.database == 'sqlserver':
                mngt_engine = create_sqlserver_engine(args.mngt_user, args.mngt_password, args.mngt_host, None, args.mngt_port, args.mngt_instance, args.mngt_trusted)
        
        mngt = None
        
        try:
            schema_server = Server(kb_engine)
            kb = schema_server.get_schema(args.schema)
            if mngt_engine:
                mngt = ManagmentBase(args.mngt_schema, mngt_engine)

        except:
            # if we cannot connect...
            logging.error("The following error occurred : %s",
                          traceback.format_exc())
            sys.exit(1)

        application = kb.get_application(args.application)
        
        if not application:
            raise RuntimeError('Application %s does not exist. Existing applications are : %s' % (args.application, kb.get_applications()))

        # connect application to it's managment base
        setattr(application, 'managment', mngt)
            
        set_current_application(application)
        
        logging.info("Connecting to knowledge base Done")

        # currently run event (for authorizing or not some operations)
        set_current_event(args.event)
        
        find_cast_plugins(args.castdirectory, kb)
        plugins = get_plugins()

        # set lisa/ltsa
        for plugin in plugins:
            plugin.set_temporary(args.temporary)
            plugin.set_intermediate(args.intermediate)


        if args.event == 'end_application' and plugins and isinstance(kb, KnowledgeBase):
            # no need to run csv for other events
            logging.info("Updating cast system views ...")
            kb.update_cast_system_views()
            logging.info("Updating cast system views Done")
        
        if args.event == 'end_application' and isinstance(kb, KnowledgeBase):
            logging.debug("Marking extension jobs as unused ...")
            application._mark_plugin_jobs_as_unused()
            logging.debug("Marking extension jobs as unused Done")
        
        if plugins:
            call_application_level_extensions(args.event, application)

        if args.event == 'end_application' and isinstance(kb, KnowledgeBase):
            logging.debug("Deleting unused job extension ...")
            application._delete_unused_jobs()
            logging.debug("Deleting unused job extension done")
        
        # publish reports
        _create_xml_report_file()
        
        logging.info("Running Extensions at application level Done")
    
    except:
        logging.error("The following error occurred : %s",
                      traceback.format_exc())
        sys.exit(2)
    
    if analysis_has_warnings():
        sys.exit(2)
    else:
        sys.exit(0)
    

main()
