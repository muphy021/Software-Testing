# coding:utf-8
__author__ = 'Helen'
'''
description:执行测试
'''
import unittest,time, HTMLTestRunner
from py_automation.py_appium.config.globalparameter import test_case_path,report_name
from py_automation.py_appium.src.common import send_email


# 构建测试集,包含src/test_case目录下的所有以test开头的.py文件
suite = unittest.defaultTestLoader.discover(start_dir=test_case_path,pattern='test*.py')

# 执行测试
if __name__=="__main__":
    report = report_name+"Report.html"
    fb = open(report,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fb,
        title=u'88APP自动化测试报告',
        description=u'项目描述：生产环境'
    )
    runner.run(suite)
    fb.close()
    # 发送邮件
    time.sleep(10)  # 设置睡眠时间，等待测试报告生成完毕（这里被坑了＝＝）
    email = send_email.send_email()
    email.sendReport()