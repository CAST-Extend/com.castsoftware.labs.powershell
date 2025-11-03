'''
Created on 5 nov. 2020

@author: MMR
'''
import csv

############################################################################################    

def parse_hostopcjobs_file(filepath, log):
    list_opcjobscall = []
    with open(filepath, 'r') as csvfile:
        # pass the file object to reader() to get the reader object
        csv_reader = csv.reader(csvfile)
        # Iterate over each row in the csv using reader object
        # Hardcoded delimiter
        _delimiter = ';'
        nbRecord = 0
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            nbRecord +=1
            # skip the header line ? no because no header
            if nbRecord > 0: 
                opc_job_line = parse_host_csv_line(row, log)
                if opc_job_line != None:
                    list_opcjobscall.append(opc_job_line)  
    return list_opcjobscall

def parse_host_csv_line(row, log):
    opc_job_line = None
    try:
        if row == None or len(row) == 0 or row[0] == None or row[0].startswith("#"): 
            return None
         
        row_splitted = row[0].split(";")
        opc_job_line = HostOPCJobsCsvLine()
        opc_job_line.opc_type = 'opcjob_to_cblprogram'
        try:
            opc_job_line.using = row_splitted[1]
        except:
            None
        opc_job_line.opc_job_name = row_splitted[2]
        try:
            opc_job_line.step_number = row_splitted[4]
        except:
            None
        # cobol program
        cblpgname = row_splitted[5].split("PGM = ")[1]
        opc_job_line.cobol_prog_name = cblpgname 
    except:
        log.warning("Error parsing OPC host file line %s " + str(row[0]))
    return opc_job_line

class HostOPCJobsCsvLine:
    def __init__(self):
        self.opc_type = None
        self.opc_job_name = None
        self.cobol_prog_name = None
        self.using= None
        self.step_number = None


############################################################################################
class LocalJobsCsvLine:
    def __init__(self):
        self.opc_type = None
        self.opc_job_name = None
        self.csharp_prog_name = None


def parse_localopcjobs_file(filepath, log):
    list_opcjobscall = []
    with open(filepath, 'r') as csvfile:
        # pass the file object to reader() to get the reader object
        csv_reader = csv.reader(csvfile)
        # Iterate over each row in the csv using reader object
        # Hardcoded delimiter
        _delimiter = ';'
        nbRecord = 0
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            nbRecord +=1
            # skip the header line ? no because no header
            if nbRecord > 0: 
                opc_job_line = parse_local_csv_line(row, log)
                if opc_job_line != None:
                    list_opcjobscall.append(opc_job_line)  
    return list_opcjobscall


def parse_local_csv_line(row, log):    
    opc_job_line = None
    try:
        if row == None or len(row) == 0 or row[0] == None or row[0].startswith("#"): 
            return None
        
         
        row_splitted = row[0].split(";")
                
        opc_job_line = LocalJobsCsvLine()
        opc_job_line.opc_type = 'opcjob_to_exe'
      
        for job_name in row_splitted[0].split("\\"):
            None
        job_name = job_name.split(".")[0]
        opc_job_line.opc_job_name = job_name
        target = row_splitted[1]
        if target.endswith(".exe"):
            opc_job_line.csharp_prog_name = target
    except:
        log.warning("Error parsing OPC local file line %s " + str(row[0]))
    return opc_job_line