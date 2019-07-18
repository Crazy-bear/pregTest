#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 11:29
# @Author  : Bear
# @Site    : 
# @File    : test_update_question.py
# @Software: PyCharm


# 更新问题
import unittest
import requests
from preg_api.common.login import *


class UpdateQuestion(unittest.TestCase):
    '''更新问题'''
    def setUp(self):
        pass

    def test_update_question_back(self):
        '''退回（待分配）'''
        pass    # 1=退回（待分配），3=举报（待审核），4=待补充

    def test_update_question_report(self):
        '''举报（待审核）'''
        pass

    def test_update_question_to_be_added(self):
        '''待补充'''
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
