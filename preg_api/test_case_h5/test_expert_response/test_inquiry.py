#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 10:58
# @Author  : Bear
# @Site    : 
# @File    : test_inquiry.py
# @Software: PyCharm


# 问诊列表页inquiry
import os
import sys
import requests
import unittest
from preg_api.common.login import *


class Inquiry(unittest.TestCase):
    '''问诊列表'''
    def setUp(self) -> None:
        self.t_skey = login('evan10@qq.com', '123456')
        # pprint(self.t_skey)

    def test_inquiry_to_be_resolved(self):
        '''待解决'''
        querystring = {"status": "2"}   # 2=待解决，9=已回复，7=已解决 ，6=已关闭
        headers = {'Cookie': 't_skey' + '=' + self.t_skey}
        r = requests.request('GET', h5_inquiry_url, headers=headers, params=querystring)
        # pprint(r.json())
        status_code = r.status_code
        ret = r.json()['ret']
        msg = r.json()['msg']
        try:
            self.assertEqual(200, status_code)
            self.assertEqual('0', ret)
            self.assertIn('ok', msg)
        except AssertionError:
            raise AssertionError('参数错误：' + msg)

    def test_inquiry_replied(self):
        '''已回复'''

    def test_inquiry_resolved(self):
        '''已解决'''

    def test_inquiry_closed(self):
        '''已关闭'''

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
