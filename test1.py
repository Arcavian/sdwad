import unittest
import sys
from mini_dafny import *
class TestPack(unittest.TestCase):
    def test_asgn_0(self):
        import asgn_0
        actual = verify(asgn_0.asgn,verbose = False)
        self.assertEqual(actual, unsat)
    
    def test_asgn_1(self):
        import asgn_1
        actual = verify(asgn_1.asgn,verbose = False)
        self.assertEqual(actual, sat)

    def test_asgn_2(self):
        import asgn_2
        actual = verify(asgn_2.asgn,verbose = False)
        self.assertEqual(actual, sat)

    def test_asgn_3(self):
        import asgn_3
        actual = verify(asgn_3.asgn,verbose = False)
        self.assertEqual(actual, unsat)
        
    def test_skip_0(self):
        import skip_0
        actual = verify(skip_0.skip,verbose = False)
        self.assertEqual(actual, sat)
    
    def test_skip_1(self):
        import skip_1
        actual = verify(skip_1.skip,verbose = False)
        self.assertEqual(actual, sat)

    def test_swap_0(self):
        import swap_0
        actual = verify(swap_0.swap,verbose = False)
        self.assertEqual(actual, unsat)
    
    def test_swap_1(self):
        import swap_1
        actual = verify(swap_1.swap,verbose = False)
        self.assertEqual(actual, sat)

    def test_if_0(self):
        import if_0
        actual = verify(if_0.if_0,verbose = False)
        self.assertEqual(actual, unsat)
    
    def test_if_1(self):
        import if_1
        actual = verify(if_1.if_1,verbose = False)
        self.assertEqual(actual, sat)
    
    def test_if_0(self):
        import if_2
        actual = verify(if_2.if_2,verbose = False)
        self.assertEqual(actual, unsat)
if __name__ == '__main__':
    unittest.main()