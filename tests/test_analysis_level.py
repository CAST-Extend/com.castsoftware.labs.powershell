'''
Created on 9 avr. 2015

@author: JAR
'''
import unittest
import cast.analysers.test

class Test(unittest.TestCase):
    def testRegisterPlugin(self):
        
        # instanciate a UA analyzer for 'PowerShell' language defined by <category name="PowerShell" rid="4">
        # see http://cast-projects.github.io/Extension-SDK/doc/code_reference.html?highlight=uatestanalysis#cast.analysers.test.UATestAnalysis
        analysis = cast.analysers.test.UATestAnalysis('PowerShell')
        
        #add_selection for folder, absolute reference
        #analysis.add_selection('C:\CAST_Clients\ACMS\Development\DEV_14.2.1\CswDev\JOBS')
        
        #add_selection for folder under "tests" Eclipse folder, relative reference
        analysis.add_selection('test_cases')
        analysis.set_verbose(True)
        print("Analysis running")
        analysis.run()
        print("Analysis statistics")
        analysis.print_statistics()        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
