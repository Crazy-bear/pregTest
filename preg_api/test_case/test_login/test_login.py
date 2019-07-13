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
        # bindphone = response.json()['data']['bindphone']
        try:
            self.assertEqual(200, status_code)
            self.assertEqual('0', ret)
            self.assertEqual('登录成功', msg)
            # self.assertEqual('13510278144', bindphone)
        except AssertionError:
            raise AssertionError('登录失败')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
