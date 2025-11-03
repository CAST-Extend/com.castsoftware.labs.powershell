import cast_upgrade_1_6_23 # @UnusedImport
import unittest
import tempfile
from cast.analysers.test import UATestAnalysis
from cast.application.test import run
from cast.application import create_engine

class TestIntegration(unittest.TestCase):

    def test_basic(self):
        myengine = create_engine("postgresql+pg8000://operator:CastAIP@localhost:2284/postgres")
        run(kb_name='powershell_sample2_local', application_name='EI_TEST_2020_C01', engine=myengine)
        
        
if __name__ == "__main__":
    unittest.main()