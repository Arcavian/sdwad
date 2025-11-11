import unittest
import sys
from mini_dafny import*
class TestPack(unittest.TestCase):

    def test_asgn_4(self):
        import asgn_4
        actual = verify(asgn_4.code,verbose = False)
        self.assertEqual(actual, sat)
    

    def test_slow_copy(self):
        import slow_copy_0
        actual = verify(slow_copy_0.code,verbose = False)
        self.assertEqual(actual, unsat)
        
        import slow_copy_1
        actual = verify(slow_copy_1.code,verbose = False)
        self.assertEqual(actual, sat)

        import slow_copy_2
        actual = verify(slow_copy_1.code,verbose = False)
        self.assertEqual(actual, sat)
    
    def test_loop_to_0(self):
        import loop_to_0
        actual = verify(loop_to_0.code,verbose = False)
        self.assertEqual(actual, unsat)

        import loop_to_1
        actual = verify(loop_to_1.code,verbose = False)
        self.assertEqual(actual, sat)

    def test_max3_0(self):
        import max3_0
        actual = verify(max3_0.code,verbose = False)
        self.assertEqual(actual, unsat)

        import max3_1
        actual = verify(max3_1.code,verbose = False)
        self.assertEqual(actual, sat)

        import max3_2
        actual = verify(max3_2.code,verbose = False)
        self.assertEqual(actual, unsat)

        import max3_3
        actual = verify(max3_3.code,verbose = False)
        self.assertEqual(actual, sat)

    def test_slow_square_0(self):
        import slow_square_0
        actual = verify(slow_square_0.code,verbose = False)
        self.assertEqual(actual, unsat)

        import slow_square_1
        actual = verify(slow_square_1.code,verbose = False)
        self.assertEqual(actual, sat)

if __name__ == '__main__':
    unittest.main()