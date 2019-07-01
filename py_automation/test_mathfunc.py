# -*- coding: utf-8 -*-

import unittest
from py_automation.mathfunc import *


class TestMathFunc(unittest.TestCase):

    def setUp(self):
        # print("do something befor test.prepare environment")
        pass

    def tearDown(self):
        # print("do something after test.Clean up")
        pass

    def test_add(self):
        # print("测试加法")
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    @unittest.skip("i don't want to run this case")
    def test_minus(self):
        # print("测试减法")
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        # print("测试乘法")
        self.assertEqual(6, multi(2, 3))

    def test_divide(self):
        # print("测试除法")
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))

'''
if __name__ == '__main__':
    unittest.main()
'''

