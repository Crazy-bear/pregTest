#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 10:56
# @Author  : Bear
# @Site    : 
# @File    : test_expert_login.py
# @Software: PyCharm

import requests
import os
import sys
import unittest
from pprint import pprint
from preg_api.common.md5_encryption import *
from preg_api.common.api_url import *
# 将获取当前路径，并插入os.path中，以免脱离IDE后，引包出现“找不到包”的错误
preg_api_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, preg_api_path)
# 专家登陆


class ExpertLogin(unittest.TestCase):
    '''专家登陆'''
    def setUp(self):
        pass

    def test_expert_login(self):
        '''成功登陆'''
        email = 'evan10@qq.com'
        # pwd = md5_encryption('123456')
        pwd = '123456'  # 后台接口没有做md5加密
        querystring = {"email": email, "password": pwd, "client_flag": "H5"}
        r = requests.request("GET", h5_expert_login_url, params=querystring)
        # pprint(r.json())
        status_code = r.status_code
        ret = r.json()['ret']
        msg = r.json()['msg']
        try:
            self.assertEqual(200, status_code)
            self.assertEqual('0', ret)
            self.assertEqual('登陆成功', msg)
        except AssertionError:
            raise AssertionError('登陆失败:' + msg)

    def test_expert_login_account_null(self):
        '''账号：为空'''
        pass

    def test_expert_login_account_error(self):
        '''账号：错误'''
        pass

    def test_expert_login_password_null(self):
        '''密码：为空'''
        pass

    def test_expert_login_password_error(self):
        '''密码：错误'''
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
