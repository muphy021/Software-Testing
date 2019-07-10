# -*- coding: UTF-8 -*-

import unittest
from py_automation.case_2.test_mathfunc import TestMathFunc
from py_report.htmltestrunner3 import HTMLTestRunner
import time
import os



if __name__ == '__main__':
    suite = unittest.TestSuite()

    # 使用这种方法可以对测试用例排序
    tests = [TestMathFunc("test_multi"), TestMathFunc("test_log_ex")]
    suite.addTests(tests)

    # 使用TestLoader的方法传入TestCase
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

    # 在同目录下生成txt格式的测试报告
    # with open('UnittestTextReport.txt', 'a') as f:
    # runner = unittest.TextTestRunner(stream=f, verbosity=2)
    # runner.run(suite)
    now = time.strftime('%Y-%m-%d %H%M%S')
    filename = open(os.getcwd() + '/testResult_report' + now + '.html', 'wb')

    runner = HTMLTestRunner(stream=filename, title="单元测试报告", description="验证测试html报告")
    runner.run(suite)
    unittest.main()

