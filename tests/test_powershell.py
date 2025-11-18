'''
Created on 9 avr. 2015

@author: JAR
'''
import unittest
import cast.analysers.test
from cast.application.test import TestKnowledgeBase
from powershell_endapplication import PowerShellApplicationLevel
import logging

class Test(unittest.TestCase):
    def test_analyzer_level(self):
        # instanciate a UA analyzer for 'PowerShell' language defined by <category name="PowerShell" rid="4">

        analysis_level = cast.analysers.test.UATestAnalysis('PowerShell')
        analysis_level.add_selection('test_cases')
        analysis_level.set_verbose(True)
        print("Analysis running")
        analysis_level.run()
        print("Analysis statistics")
        analysis_level.print_statistics()

    def test_app_level(self):

        test_kb = TestKnowledgeBase()
        project = test_kb.add_project('ProjectA', 'PowerShellProject')
        project.add_object('exemple2', 'exemple2', 'PowerShellProgram')

        extension = PowerShellApplicationLevel()
        application = test_kb.run(extension.end_application, logging.DEBUG) #Lance end_app

if __name__ == "__main__":
    unittest.main()
