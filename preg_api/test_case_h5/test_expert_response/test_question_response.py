#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 11:28
# @Author  : Bear
# @Site    : 
# @File    : test_question_response.py
# @Software: PyCharm


# 问题回复question_response
import unittest
import requests
from preg_api.common.login import *


class QuestionResponse(unittest.TestCase):
    '''问题回复'''
    def setUp(self):
        pass

    def test_question_response_text(self):
        '''文本回复'''
        pass    # text（文字），media（语音）

    def test_question_response_media(self):
        '''语音回复'''
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
