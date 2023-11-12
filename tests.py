# CS362
# A2: TDD Hands On
# by Kongkom Hiranpradit ONID ID: hiranprk
# 12 November 2023

import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    """ Rule 1: Must be between 8 and 20 characters (inclusive) """
    def test1(self):
        """ Boundary case: 7 characters """
        input = 'aldjfldi'
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test2(self):
        """ Boundary case: 8 characters """
        input = 'adleiwpd'
        expected = True
        self.assertEqual(check_pwd(input), expected)


if __name__ == '__main__':
    unittest.main()
