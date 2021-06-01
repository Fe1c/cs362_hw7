import unittest
import pytest
import leap
import coverage


class TestCase(unittest.TestCase):
    #pass cases
    def test_pass_1(self):
        #test to see if a year diviible by four is considered a leap year for first version
        self.assertEqual(leap.leap(2012), "true")
    def test_pass_2(self):
        #test to see if a year divible by 4 and 100
        self.assertEqual(leap.leap(2000), "false")

if __name__ == '__main__':
    unittest.main()