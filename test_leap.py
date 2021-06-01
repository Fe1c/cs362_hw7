import unittest
import pytest
import leap
import coverage


class TestCase(unittest.TestCase):
    #pass cases
    def test_pass_1(self):
        #test to see if a year diviible by four is considered a leap year for first version
        self.assertEqual(leap.leap(2012), "true")


if __name__ == '__main__':
    unittest.main()