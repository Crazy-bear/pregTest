#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 20:20
# @Author  : Bear
# @Site    : 
# @File    : login.py
# @Software: PyCharm
import requests
from preg_api.common.api_url import *
from preg_api.common.md5_encryption import *
from pprint import pprint
# 封装login方法，提供调用


# 定义login方法
def login(account, password):
    login_pwd = md5_encryption(password)
    login_pars = {"account": account,
                  "password": login_pwd
                  }
    r = requests.post(login_url, params=login_pars)
    # pprint(r.json())
    status_code = r.status_code
    ret = r.json()['ret']
    msg = r.json()['msg']
    try:
        assert 200 == status_code
        assert '0' == ret
        assert '登录成功' == msg
    except AssertionError:
        # raise AssertionError('登录失败' + msg)
        raise AssertionError(msg)
    return r.cookies['t_skey']  # 获取t_skey是为了免登录，处于“登陆”状态


# if __name__ == '__main__':
#     login = login(13510278144, '123456')
#     pprint(login)
