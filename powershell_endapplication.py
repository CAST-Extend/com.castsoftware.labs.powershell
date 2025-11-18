from cast.application import ApplicationLevelExtension, create_link
import logging
import os

class PowerShellApplicationLevel(ApplicationLevelExtension):
    """
    Post-processing for PowerShell analysis.
    Creates logical links between PowerShell objects
    (e.g., function calls across scripts or modules).
    """

    def __init__(self):
        # stats for logging
        self.nb_scripts = 0
        self.nb_links = 0
        self.functions = {}
        self.callsites = {}

    def end_application(self, application):
        logging.info("***************************************************************")
        logging.info("PowerShellApplicationLevel: post-processing application objects")
        print("application : %s" %application)
        # collect all PowerShell script files
        scripts = list(application.objects().has_type('PowerShellProgram'))
        self.nb_scripts = len(scripts)
        for s in scripts:
            logging.debug("Script found: {0}".format(s.get_name()))

        # collect all functions defined
        for func in application.objects().has_type('PowerShellFunction'):
            self.functions[func.get_fullname()] = func
            logging.debug("Function found: {0}".format(func.get_fullname()))

        # collect all call sites (functions calling others)
        for call in application.objects().has_type('PowerShellCall'):
            self.callsites[call.get_fullname()] = call
            logging.debug("Call site found: {0}".format(call.get_fullname()))

        # create logical links between call sites and target functions
        for caller_name, caller_obj in self.callsites.items():
            target_name = caller_name.split('.')[-1]
            if target_name in self.functions:
                self.create_call_link(caller_obj, self.functions[target_name])

        # collect calls from intermediate file
        calls_file = self.get_intermediate_file('com.castsoftware.labs.powershell.txt')
        logging.info("calls_file : %s" %calls_file)

        for line in calls_file:
            if line.startswith("CALL;"):
                try:
                    _, target_name, caller_name = line.strip().split(';', 2)
                except ValueError:
                    continue

        self.log_summary()

    def create_call_link(self, caller, callee):
        """Create a CAST link between two PowerShell objects."""
        try:
            create_link('callLink', caller, callee)
            logging.info("Link created: {0} -> {1}".format(
                caller.get_fullname(), callee.get_fullname()))
            self.nb_links += 1
        except Exception as e:
            logging.warning("Failed to create link {0} -> {1}: {2}".format(
                caller, callee, e))

    def log_summary(self):
        logging.info("***************************************************************")
        logging.info("Scripts analyzed: {0}".format(self.nb_scripts))
        logging.info("Links created: {0}".format(self.nb_links))
        logging.info("***************************************************************")
