#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 17:26
# @Author  : Bear
# @Site    : 
# @File    : api_url.py
# @Software: PyCharm

# 将所有的API进行统一封装
# api = 'http://m-alpha.lmbang.com' # lmb的host
# api = 'http://open.lmbang.com'     # preg的host（线上）
api = 'http://open.alpha.lmbang.com'   # preg的host（alpha）

# 账号、密码登陆URL
login_url = api + '/user-login/index'

# 发帖URL
post_url = api + '/topic/add/index'

# 综合搜索URL
search_url = api + '/find-search/all'
