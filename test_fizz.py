import unittest
import pytest
import fizz
import coverage


class TestCase(unittest.TestCase):
    #pass cases
    def test_pass_1(self):
        test = fizz.fizz() #test[0] should equal 1 as fizz returns the array sequence
        self.assertEqual(test[0], 1)
    def test_pass_2(self):
        test = fizz.fizz() #test[2] should be Fizz as 3 is divisible by 3
        self.assertEqual(test[2], "Fizz")
    def test_pass_3(self):
        test = fizz.fizz() #test[4] should be Buzz as 5 is divisible by 3
        self.assertEqual(test[4], "Buzz")



if __name__ == '__main__':
    unittest.main()