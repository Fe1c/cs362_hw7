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
        test = fizz.fizz() #test[0] should equal 1 as fizz returns the array sequence
        self.assertEqual(test[2], "Fizz")



if __name__ == '__main__':
    unittest.main()