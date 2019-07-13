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
    testunit = unittest.TestSuite()
    test_dir = './test_case'     # 运行时修改为指定测试目录
    print(test_dir)
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
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    file = './report/'+now+'_preg_result.html'
    fp = open(file, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            tester="hjx",
                            title=u"孕期伴侣接口测试报告",
                            description=u"用例执行情况:")
    runner.run(alltestnames)
    fp.close()
