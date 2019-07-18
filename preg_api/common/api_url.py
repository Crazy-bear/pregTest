#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 17:26
# @Author  : Bear
# @Site    : 
# @File    : api_url.py
# @Software: PyCharm

# 将所有的API进行统一封装

'''H5接口'''
api_h5 = 'https://m-alpha.lmbang.com'  # lmb的host

'''preg接口'''
# api_preg = 'http://open.lmbang.com'     # preg的host（线上）
api_preg = 'http://open.alpha.lmbang.com'   # preg的host（alpha）

'''专家问答接口'''
# 专家登陆
h5_expert_login_url = api_h5 + '/diagnose-expert/login'

# 问诊列表页
h5_inquiry_url = api_h5 + '/diagnose-expert/myConsultation'

# 问题会话列表
h5_question_session_list_url = api_h5 + '/diagnose-expert/getProblemList'

# 问题回复
h5_question_response_url = api_h5 + '/diagnose-expert/replay'

# 我的收入
h5_income_url = api_h5 + '/diagnose-expert/listIncome'

# 历史收入
h5_historical_income_url = api_h5 + '/diagnose-expert/listIncome'

# 更新问题
h5_update_question_url = api_h5 + '/diagnose-expert/updateQuestion'


'''preg接口'''
# 账号、密码登陆URL
login_url = api_preg + '/user-login/index'

# 发帖URL
post_url = api_preg + '/topic/add/index'

# 综合搜索URL
search_url = api_preg + '/find-search/all'
