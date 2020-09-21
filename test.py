import unittest 
import os

import nbimporter
import Code.PandemicPrediction as pp

class TestAgent(unittest.TestCase): 

    def setUp(self):        
        print("Initialised unit test")

if __name__ == '__main__':
    main = TestAgent()

    # This executes the unit test/(itself)
    import sys
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAgent)
    unittest.TextTestRunner(verbosity=4,stream=sys.stderr).run(suite)
