# -*- coding: utf-8 -*-

import unittest
from py_automation.case_2.mathfunc import *
from learnPython.py_log.log_demo import *

class TestMathFunc(unittest.TestCase):
    def setUp(self):
        print("每条case之前执行")
        # pass

    def tearDown(self):
        print("每条case之后执行")
        # pass

    def test_add(self):
        """测试加法功能"""
        print("测试加法")
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(1, 2))

    # @unittest.skip("i don't want to run this case")
    def test_minus(self):
        """测试减法功能"""
        print("测试减法")
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        """测试乘法功能"""
        print("测试乘法")
        self.assertEqual(6, multi(2, 3))

    def test_divide(self):
        """测试除法功能"""
        print("测试除法")
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))

    def test_log_ex(self):
        """Test python's log function"""
        print("Test python's log")
        log_ex()

'''
if __name__ == '__main__':
    unittest.main()
'''

