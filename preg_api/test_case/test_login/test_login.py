# encoding:utf8
import requests
import unittest
from pprint import pprint
import os
import sys
from preg_api.common.api_url import *
from preg_api.common.md5_encryption import *

# 将获取当前路径，并插入os.path中，以免脱离IDE后，引包出现“找不到包”的错误
preg_api_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, preg_api_path)


# 定义LoginCase类测试登录接口
class LoginCase(unittest.TestCase):
    '''账号、密码登陆测试'''
    def setUp(self):
        pass

    def test_login_success(self):
        '''正常登陆测试'''
        account = 13510278144
        password = md5_encryption('123456')
        querystring = {"account": account,
                       "password": password
                       }
        response = requests.post(login_url, params=querystring)
        # pprint(response.json())
        status_code = response.status_code
        ret = response.json()['ret']
        msg = response.json()['msg']
        bindphone = response.json()['data']['bindphone']
        try:
            self.assertEqual(200, status_code)
            self.assertEqual('0', ret)
            self.assertEqual('登录成功', msg)
            self.assertEqual('13510278144', bindphone)
        except AssertionError:
            # raise AssertionError('登录失败' + msg)
            raise AssertionError(msg)

    def test_login_account_null(self):
        '''账号：为空'''
        account =''
        password = md5_encryption('123456')
        querystring = {"account": account,
                       "password": password
                       }
        response = requests.post(login_url, params=querystring)
        # pprint(response.json())
        status_code = response.status_code
        ret = response.json()['ret']
        msg = response.json()['msg']
        try:
            self.assertEqual(200, status_code)
            self.assertEqual('111102', ret)
            self.assertEqual('用户名或密码不能为空', msg)
        except AssertionError:
            # raise AssertionError('登录失败' + msg)
            raise AssertionError(msg)

    def test_login_account_error(self):
        '''账号：错误账号'''
        account ='13540'
        password = md5_encryption('123456')
        querystring = {"account": account,
                       "password": password
                       }
        response = requests.post(login_url, params=querystring)
        # pprint(response.json())
        status_code = response.status_code
        ret = response.json()['ret']
        msg = response.json()['msg']
        try:
            self.assertEqual(200, status_code)
            self.assertEqual('111105', ret)
            self.assertEqual('输入正确的邮箱或手机号', msg)
        except AssertionError:
            # raise AssertionError('登录失败' + msg)
            raise AssertionError(msg)

    def test_login_password_null(self):
        '''密码：为空'''
        account = '13510278144'
        password = ''   # 密码为空时，不需要用md5加密，否则还是会传密码
        querystring = {"account": account,
                       "password": password
                       }
        response = requests.post(login_url, params=querystring)
        # pprint(response.json())
        status_code = response.status_code
        ret = response.json()['ret']
        msg = response.json()['msg']
        try:
            self.assertEqual(200, status_code)
            self.assertEqual('111102', ret)
            self.assertEqual('用户名或密码不能为空', msg)
        except AssertionError:
            # raise AssertionError('登录失败' + msg)
            raise AssertionError(msg)

    def test_login_password_error(self):
        '''密码：错误'''
        account = '13510278144'
        password = md5_encryption('2222')
        querystring = {"account": account,
                       "password": password
                       }
        response = requests.post(login_url, params=querystring)
        # pprint(response.json())
        status_code = response.status_code
        ret = response.json()['ret']
        msg = response.json()['msg']
        try:
            self.assertEqual(200, status_code)
            self.assertEqual('111104', ret)
            self.assertEqual('用户名或密码错误，请重新输入', msg)
        except AssertionError:
            # raise AssertionError('登录失败' + msg)
            raise AssertionError(msg)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
