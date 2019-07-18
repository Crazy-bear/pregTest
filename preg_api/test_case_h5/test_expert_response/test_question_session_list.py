#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 11:27
# @Author  : Bear
# @Site    : 
# @File    : test_question_session_list.py
# @Software: PyCharm


# 问题会话列表question_session_list
import os
import sys
import requests
import unittest
from preg_api.common.login import *


class QuestionSessionList(unittest.TestCase):
    '''问题会话列表'''
    def setUp(self) -> None:
        self.t_skey = login('evan10@qq.com', '123456')
        # pprint(self.t_skey)

    def test_question_session_list(self):
        '''问题会话列表'''
        querystring = {"id": "345"}
        headers = {"Cookie": 't_skey' + '=' + self.t_skey}
        r = requests.request("POST", h5_question_session_list_url, headers=headers, params=querystring)
        # pprint(r.json())
        status_code = r.status_code
        ret = r.json()['ret']
        msg = r.json()['msg']
        data = r.json()['data']['problem']['id']
        # pprint(data)
        try:
            self.assertEqual(200, status_code)
            self.assertEqual('0', ret)
            self.assertIn('ok', msg)
            self.assertEqual('345', data)
        except AssertionError:
            raise AssertionError('参数错误：' + msg)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
