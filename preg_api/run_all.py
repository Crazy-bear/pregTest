#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 18:31
# @Author  : Bear
# @Site    : 
# @File    : run_all.py
# @Software: PyCharm
# 1.集中运行所有的测试用例，
# 2.自动生成HTML报告，
# 3.自动发送邮件
import os
import sys
import unittest
# 将获取当前路径，并插入os.path中，以免脱离IDE后，引包出现“找不到包”的错误
preg_api_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, preg_api_path)
print(preg_api_path)
from preg_api.common.logger import *
from preg_api.conf.HTMLTestRunnerNew import HTMLTestRunner
from preg_api.common.send_email import *
import time


sys.path.append('./test_case')
sys.path.append('./test_case_h5')


def creat_test_suit():
    # 定义一个测试套件
    testunit = unittest.TestSuite()
    test_dir = './test_case_h5'     # 运行时修改为指定测试目录
    print(test_dir)
    # TestLoader类中提供的方法discover（）
    # discover（start_dir, pattern ='test *.py', top_level_dir = None ）
    # start_dir：要测试的模块名或测试用例目录；
    # pattern='test*.py'：表示用例文件名的匹配原则，下面的例子中匹配文件名为以“test”开头的“.py”文件，星号“*”表示任意多个字符；
    # top_level_dir=None：测试模块的顶层目录，如果没有顶层目录，默认为None；
    discover = unittest.defaultTestLoader.discover(
        test_dir,
        pattern='test_*.py',)

    for testsuit in discover:
        for test_case in testsuit:
            testunit.addTest(test_case)
            print('case', test_case)
        print(testsuit)
    return testunit


alltestnames = creat_test_suit()

if __name__ == '__main__':
    # 按照格式获取当前时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    # 定义报告存放的路径
    # file = './report/'+now+'_preg_result.html'
    file = './report/'+now+'_h5_result.html'
    fp = open(file, 'wb')

    # 生成HTML测试报告
    runner = HTMLTestRunner(stream=fp,
                            tester="hjx",
                            # title=u"孕期伴侣接口测试报告",
                            title=u"h5接口测试报告",
                            description=u"用例执行情况:")
    runner.run(alltestnames)
    fp.close()

    # 打印日志
    log = Log()
    log.info("所有用例运行完成")

    # 发送测试邮件
    # content = "接口自动化报告"
    # subject = "接口自动化报告"
    # from_addr = ''    # 发送邮箱地址
    # to_addr = ['']  # 列表形式填写收件人，发送给单个人也以列表形势传送
    # host = "smtp.exmail.qq.com"
    # pwd = "123456"    # 由于是第三方登陆，所以此处的密码是授权码,运行时需要修改为授权码
    # file_name = file
    # SendMail(content, subject, from_addr, to_addr, host, pwd, file_name).send_mail()

