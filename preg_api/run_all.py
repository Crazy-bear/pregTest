#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 18:31
# @Author  : Bear
# @Site    : 
# @File    : run_all.py
# @Software: PyCharm

from HTMLTestRunnerNew import HTMLTestRunner
import sys
import unittest
import time
sys.path.append('./test_case')


def creat_test_suit():
    # 定义一个测试套件
    testunit = unittest.TestSuite()
    test_dir = './test_case'     # 运行时修改为指定测试目录
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
    file = './report/'+now+'_preg_result.html'
    fp = open(file, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            tester="hjx",
                            title=u"孕期伴侣接口测试报告",
                            description=u"用例执行情况:")
    runner.run(alltestnames)
    fp.close()
