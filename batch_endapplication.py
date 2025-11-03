from cast.application import ApplicationLevelExtension, create_link
import cast_upgrade_1_6_23  # @UnusedImport
import logging 
import traceback
from opcjobs import parse_host_csv_line, parse_hostopcjobs_file,\
    parse_localopcjobs_file

"""
class DevboosterExtensionApplication
    
"""
    
class EIBatchExtensionApplication(ApplicationLevelExtension):

    ###################################################################################################        

    
    def __init__(self):
        # setting the value for unit testing, will be overwitten by standard analysis
        self.default_deploy_folder = 'C:/Users/mmr/workspace/com.castsoftware.uc.ei.batch/tests/test_cases'
        
        self.nb_file_hostopcjobs = 0
        self.nb_file_localopcjobs = 0
        self.cobolprogs = {}        
        self.cobolunknownprogs = {}
        self.opcjobs = {}
            
    ###################################################################################################        
  
    def end_application(self, application):
        logging.info("*********************************************************************************") 
        logging.info("EIBatchExtensionApplication : running code at the end of an application")

        ############################################################################################

        # List of OPC Jobs
        logging.debug("OPC jobs list in local : ")
        for opcjob in application.objects().has_type('OPCJob'): 
            self.opcjobs[opcjob.get_name()] = opcjob
            logging.info(opcjob.get_name()) 

        # List of cobol programs (all of them)
        logging.debug("Cobol programs list in local : ")
        for cobolpgm in application.objects().has_type('CAST_COBOL_SavedProgram').load_property('metric.CodeLinesCount'): 
            self.cobolprogs[cobolpgm.get_name()] = cobolpgm
            logging.info(cobolpgm.get_name()) 
        
        logging.debug("Cobol unknown programs list in local : ")
        for cobolpgm in application.objects().has_type('CAST_COBOL_ProgramPrototype'): 
            self.cobolunknownprogs[cobolpgm.get_name()] = cobolpgm
            logging.info(cobolpgm.get_name())
        
        ############################################################################################
        # parsing files when required
        files = application.get_files()
        # files = application.get_files(['CAST_COBOL_SavedProgram', 'CAST_DotNet_DotNet', 'CAST_Web_File', 'C_FILE'])
        logging.info("parsing opc file files : '.hostopcjobs', '.localopcjobs' ")

        for file in files:
            # logging.debug("parsing file > " + o.get_path())
            # check if file is analyzed source code, or if it generated (Unknown)
            if not file.get_path():
                continue

            # for logging only
            if file.get_path().lower().endswith('.hostopcjobs') or file.get_path().lower().endswith('.localopcjobs'):
                logging.debug("file found: >" + str(file.get_path()))
            
            if file.get_path().lower().endswith('.hostopcjobs'):
                self.nb_file_hostopcjobs += 1
                list_opcjobs = parse_hostopcjobs_file(file.get_path(), logging)
                for opcjob_to_link in list_opcjobs:
                    self.create_link_to_cbl_prog(file, self.opcjobs[opcjob_to_link.opc_job_name], opcjob_to_link.cobol_prog_name)#, self.opcjobs[opcjob_to_link.opc_job_name].position)
            """if file.get_path().lower().endswith('.localopcjobs'):
                self.nb_file_localopcjobs += 1
                list_opcjobs = parse_localopcjobs_file(file.get_path(), logging)
                for opcjob_to_link in list_opcjobs:
                    None
            """
        self.end_app_log()
 
    ###################################################################################################        

    def create_link_to_cbl_prog(self, cfile, o_caller_opcjob, called_cblprog, bookmark=None):
        if not not o_caller_opcjob and not not called_cblprog:
            try:
                logging.info("\t  Trying to create link between OPC job " + o_caller_opcjob.get_fullname() + " and cobol program " + called_cblprog)
                oCblPgm = self.cobolprogs[called_cblprog]
                create_link('callLink', o_caller_opcjob, oCblPgm, bookmark)
                logging.info("\t  Link created between OPC job " + o_caller_opcjob.get_fullname() + " and cobol program " + oCblPgm.get_name())                
            except KeyError:
                try:
                    oCblPgm = self.cobolunknownprogs[called_cblprog]
                    create_link('callLink', o_caller_opcjob, oCblPgm, bookmark)
                    logging.info("\t  link created between OPC job " + o_caller_opcjob.get_fullname() + " and unknown cobol program " + oCblPgm.get_name())
                except KeyError:
                    logging.info('\t\tCouldn''t find cobol program %s' % (called_cblprog))                                

    ###################################################################################################        
 
    def end_app_log(self):
        # Final reporting
        logging.info("###################################################################################")
        logging.info("Number of .hostopcjobs files scanned : " + str(self.nb_file_hostopcjobs))
        logging.info("Number of .localopcjobs files scanned : " + str(self.nb_file_localopcjobs))
        logging.info("###################################################################################")
        
