# -*- encoding: utf-8 -*-

import logging

'''
https://www.cnblogs.com/yyds/p/6901864.html


日志的作用可以简单总结为以下3点：
(1) 程序调试
(2) 了解软件程序运行情况，是否正常
(3) 软件程序运行故障分析与问题定位

如果应用的日志信息足够详细和丰富，还可以用来做用户行为分析，如：分析用户的操作行为、类型洗好、地域分布以及其它更多的信息，由此可以实现改进业务、提高商业利益。

不同的应用程序所定义的日志等级可能会有所差别，分的详细点的会包含以下几个等级：
    DEBUG
    INFO
    NOTICE
    WARNING
    ERROR
    CRITICAL
    ALERT
    EMERGENCY

一条日志信息对应的是一个事件的发生，而一个事件通常需要包括以下几个内容：
(1) 事件发生时间
(2) 事件发生位置
(3) 事件的严重程度--日志级别
(4) 事件内容

日志等级是从上到下依次升高的，即：DEBUG (最详细的日志信息) < INFO（关键点信息） < WARNING（不期望的事件，但是程序正常运行） < ERROR（部分功能不正常） < CRITICAL（程序不能继续运行），
而日志的信息量是依次减少的；



'''
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
# filename='test_py_logging.log',
logging.basicConfig( level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT) # 'module' object has no attribute 'basicConfig'因为起的文件名是logging



logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")