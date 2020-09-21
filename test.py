import unittest 
import os

import nbimporter
import Code.PandemicPrediction as pp

class TestAgent(unittest.TestCase): 

    def setUp(self):        
        print("Initialised unit test")
    
    def test_nodal_precession(self):
        pp1 = pp.Pandemic(0.01, 0.6, range(20, 30, 1))
        self.assertEqual([0.01, 0.6],[pp1.beta, pp1.delta])

if __name__ == '__main__':
    main = TestAgent()

    # This executes the unit test/(itself)
    import sys
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAgent)
    unittest.TextTestRunner(verbosity=4,stream=sys.stderr).run(suite)
