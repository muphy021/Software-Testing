# -*- encoding: utf-8 -*-

from py_automation.case_3.common_func.send_email import *
from py_automation.case_3.common_func.find_report_file import *
from py_automation.case_2.test_mathfunc import TestMathFunc

import os
import unittest
import time
from py_report.htmltestrunner3 import *


if __name__=='__main__':
    print ('=====AutoTest Start======')

    current_path = os.path.dirname(__file__)

    test_case_dir = os.path.join(current_path, "test_case")
    test_report_dir = os.path.join(current_path, "report")
    # discover = unittest.defaultTestLoader.discover(test_case_dir, pattern="test_*.py")
    suite = unittest.TestSuite()
    tests = [TestMathFunc("test_multi"), TestMathFunc("test_log_ex")]
    suite.addTests(tests)

    now = time.strftime('%Y-%m-%d_%H:%M:%S')
    ready_report_path = os.path.join(test_report_dir, now)
    os.mkdir(ready_report_path)

    report_name = os.path.join(test_report_dir, now, "result.html")
    report_file = open(report_name, 'ab+')


    # exe report
    runner = HTMLTestRunner(stream=report_file, title=u"测试报告", description=u"用例执行情况")
    runner.run(suite)

    report_file.close()

    # find test report
    get_report = os.path.join(find_file(test_report_dir), "result.html")
    # print(get_report)
    # send report mail
    send_email(get_report)

    print("=====AutoTest Over======")