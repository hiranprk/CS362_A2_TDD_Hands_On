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
        input = 'aldjfld'
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test2(self):
        """ Boundary case: 8 characters """
        input = 'adleiwpd'
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test3(self):
        """ Boundary case: 20 characters """
        input = 'asdfghjklqwertyuiopz'
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test4(self):
        """ Boundary case: 21 characters """
        input = 'asdfghjklqwertyuiopza'
        expected = False
        self.assertEqual(check_pwd(input), expected)

    """ Rule 2: Must contain at least one lowercase letter (standard English alphabet) """
    def test5(self):
        """ Boundary case: 8 characters, all uppercase letter """
        input = 'ASDFGHJK'
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test6(self):
        """ Boundary case: 8 characters, 1 lowercase letter """
        input = 'aSDFGHJK'
        expected = False
        self.assertEqual(check_pwd(input), expected)

    """ Rule 3: Must contain at least one uppercase letter (standard English alphabet) """
    def test7(self):
        """1 uppercase letter"""
        input = 'Asdfghjk'
        expected = False
        self.assertEqual(check_pwd(input), expected)

    """ Rule 4: Must contain at least one digit """
    def test8(self):
        """1 digit, 1 upper, 1 lower"""
        input = '1Asdfghj'
        expected = True
        self.assertEqual(check_pwd(input), expected)


if __name__ == '__main__':
    unittest.main()
