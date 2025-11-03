import cast.analysers.ua
from cast.analysers import CustomObject, Bookmark, log, create_link
import os
import re
from opcjobs import parse_hostopcjobs_file, parse_localopcjobs_file 

class BatchSrcFile(cast.analysers.ua.Extension):
    
    dict_opc_jobs = {}
    nb_opc_job = 0
    nb_opc_job_for_host = 0
    nb_opc_job_for_local = 0  
    nb_opc_job_for_local_call_to_dotnetpgm = 0
    
    def create_opc_jobs(self, file, env, list_items):
        for opc_job_line in list_items:
            #log.info("call from opc job %s to cobol program %s for step %s" % (opc_job_line.opc_job_name, opc_job_line.cobol_prog_name, opc_job_line.step_number))
            if not opc_job_line.opc_job_name in self.dict_opc_jobs:
                # creating the OPC job object
                log.info("Creating OPCJob %s" % str(opc_job_line.opc_job_name ))
                custobj = cast.analysers.CustomObject()
                custobj.set_type("OPCJob")
                custobj.set_name(opc_job_line.opc_job_name)
                custobj.set_fullname(opc_job_line.opc_job_name)
                custobj.set_parent(file)
                custobj.save()
                self.dict_opc_jobs[opc_job_line.opc_job_name] = custobj
                self.nb_opc_job += 1
                if env == 'host': self.nb_opc_job_for_host += 1
                elif env == 'local': self.nb_opc_job_for_local += 1
            
            try:
                if opc_job_line.csharp_prog_name != None:
                    # create the
                    log.info("Creating OPCJob call to program for .Net %s" % str(opc_job_line.csharp_prog_name))
                    objcall_to_prog = cast.analysers.CustomObject()
                    objcall_to_prog.set_type("OPCDotNetCall")
                    objcall_to_prog.set_name(opc_job_line.csharp_prog_name)
                    objcall_to_prog.set_fullname(opc_job_line.csharp_prog_name)
                    objcall_to_prog.set_parent(custobj)
                    objcall_to_prog.save()
                    objcall_to_prog.save_property('CAST_CallToProgram.programName', opc_job_line.csharp_prog_name)
                    create_link('callLink',custobj, objcall_to_prog)#,callBookmark)
                    self.nb_opc_job_for_local_call_to_dotnetpgm += 1
    
            except AttributeError:
                # for host there is not csharp program name
                None
        
    def start_file(self, file):             # Extension point : each file
        filepath=file.get_path()
        file_name, file_extension = os.path.splitext(filepath)
        
        typesToSaveDico = {'.opc': 'OPCDotNetCall','.ps1': 'PowerShellDotNetCall','.bat': 'WindowsBATDotNetCall','.cmd': 'WindowsCMDDotNetCall' }
        
        fileextensions = ('.bat', '.cmd', '.ps1', '.opc', '.hostopcjobs', '.localopcjobs')       # this could be dynamic : fetch from UA job options....
        if not filepath.endswith(fileextensions):   # UA is supposed to filter only *.bat , this check is in double ?
            return

        if filepath.endswith('.hostopcjobs'):
            self.create_opc_jobs(file, 'host', parse_hostopcjobs_file(filepath, log))
                
        elif filepath.endswith('.localopcjobs'):
            self.create_opc_jobs(file, 'local', parse_localopcjobs_file(filepath, log))
        
        elif file_extension in typesToSaveDico:
            batch_art = CustomObject()
            batch_art.set_name(os.path.basename(filepath))
            batch_art.set_fullname(filepath)
            batch_art.set_type('BatchProgram')              # same type for all 3 kinds of extension .
            batch_art.set_parent(file)
            batch_art.save()
            log.info("Saved BatchProgram custom object for " + str(filepath))
        
            # parsing line by line
            lineNb = 0
            with open(file.get_path(), 'r') as f:
                fullExeCallList = []            # reset list of .exe for that file
                for line in f:
                    lineNb +=1
                    
                    # OLD WAY - unreliable : detect calling command : CALL / spawn / call / call prod_exec exec=
                    #if line[:20].lower() == "call prod_exec exec=":
                        #callProgramBookmark = Bookmark(file,lineNb,1,lineNb,-1)
                        #log.info("About to create Call to program at " + str(lineNb) + " for " + line)
                        #batch_art.save_violation('Batch_Properties.numberOfCACLScommand', callProgramBookmark)
    
                    
                    # Assumption is made that the executable is callable with fullname (including '.exe')
                    # Using this characteristics to detect calls (instead of keyword spawn / call / call prod_exec / ....)
                    # matchCall = re.match("^[ \t]*CALL[ \t]+([^(]+)\(", line)
                    # limitation : does not skip the commented out commands (REM, ';', ...)
                    foundExeCallList = re.findall(r'[\w_\.]+\.exe', line)
                    if foundExeCallList:
                        log.info("!!!FOUND matchExeCall at line " + str(lineNb) + " for " + line)
                        calledExecutable = foundExeCallList[0]       # assuming there is only one match on one line, taking the first in the list
                        colStart = line.find(calledExecutable) + 1
                        colEnd = colStart + len(calledExecutable)
                        
                        log.debug("!!!FOUND calledExecutable : " + calledExecutable)
                        # DONE : maintain a list of "Call to program" objects and check for existence to avoid RuntimeError: Duplicate guid 
                        if calledExecutable not in fullExeCallList:
                            fullExeCallList.append(calledExecutable)
                            # DONE : create "Call to program" object
                            call_to_prog = CustomObject()
                            call_to_prog.set_name(calledExecutable)
                            call_to_prog.set_fullname(calledExecutable)
                            # get the type of shell/opc , in order to save with the right object type (1 type defined per type of shell/opc)
                            shellType = os.path.splitext(filepath)[1]
                            # TODO (optional) : control the shellType to ensure it is known and avoid a key error in dico
                            call_to_prog.set_type(typesToSaveDico[shellType])
                            call_to_prog.set_parent(batch_art)
                            call_to_prog.save()
                            log.info("Saved call_to_prog custom object with type  " + typesToSaveDico[shellType])
                            
                            # DONE: save_property('CAST_CallToProgram.programName', programeName) that will be used by WBS to match with server object
                            call_to_prog.save_property('CAST_CallToProgram.programName', calledExecutable)
                        
                            # DONE: create_link from current Batch file to calledExecutable
                            callBookmark = Bookmark(file,lineNb,colStart,lineNb,colEnd)
                            create_link('callLink',batch_art,call_to_prog,callBookmark)
                        
    
            log.info("NB LINES (my counter) of " + os.path.basename(filepath) + " = " + str(lineNb))
            batch_art.save_position(Bookmark(file,1,1,lineNb,-1))       # useful for F11 Code Viewer : Object D:\..my.bat (Batch Program) has no code 
    
    ##########################################################################################################################
  
    def end_analysis(self):
        self.log_end_analysis()
  
    ##########################################################################################################################
        
    def log_end_analysis(self):
        log.info("=======================================================================================")
        log.info('BatchSrcFile end_analysis UA')        
        log.info("=======================================================================================")
        log.info("Total number of OPC job created : %s" % str(self.nb_opc_job))
        log.info("Number of OPC job for host created : %s" % str(self.nb_opc_job_for_host))
        log.info("Number of OPC job for local created : %s" % str(self.nb_opc_job_for_local))
        log.info("Number of OPC job for local call to program created %s:" % str(self.nb_opc_job_for_local_call_to_dotnetpgm))
        log.info("*******************************************************************************************")       
    