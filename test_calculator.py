import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(10,15),25)
        self.assertEqual(add(232,56),288)
        self.assertEqual(add(1,2),3)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(15,10),5)
        self.assertEqual(sub(5,3),2)
        self.assertEqual(sub(100,50),50)
    

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(5,5),25)
        self.assertEqual(mul(7,6),42)
        self.assertEqual(mul(1,987),987)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(10,5),2)
        self.assertEqual(div(5,2.5),2)
        self.assertEqual(div(100,20),5)
    

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code
        with self.assertRaises(ZeroDivisionError):
            div(0,10)

    def test_logarithm(self): # 3 assertions
    #     fill in code
        self.assertEqual(log(10,100),2)
        self.assertEqual(log(3,9),2)
        self.assertEqual(log(2,8),3)

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
        with self.assertRaises(ValueError):
            log(-5,8)

    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
        with self.assertRaises(ValueError):
            logarithm(0,5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(5,12),13)
        self.assertEqual(hypotenuse(0,0),0)
        

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################
        with self.assertRaises(ValueError):
            square_root(-5)

# Do not touch this
if __name__ == "__main__":
    unittest.main()