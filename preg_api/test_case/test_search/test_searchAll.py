#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 20:06
# @Author  : Bear
# @Site    : 
# @File    : test_searchAll.py
# @Software: PyCharm
import requests
import unittest
from pprint import pprint
import os
import sys
from preg_api.common.api_url import *
from preg_api.common.md5_encryption import *
from preg_api.common.login import *
# 将获取当前路径，并插入os.path中，以免脱离IDE后，引包出现“找不到包”的错误
preg_api_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, preg_api_path)


# 定义SearchAllCase类测试综合搜索
class SearchAllCase(unittest.TestCase):
    '''综合搜索'''
    def setUp(self):
        self.t_skey = login('13510278144', '123456')
        # pprint(self.t_skey)

    def test_all_search(self):
        '''综合搜索：会员'''
        querystring = {"client_flag": "preg",
                       "kw": "会员",
                       "mvc": "1"}
        headers = {'Cookie': 't_skey' + '=' + self.t_skey}
        r = requests.request("GET", search_url, headers=headers, params=querystring)
        # pprint(r.json())
        status_code = r.status_code
        ret = r.json()['ret']
        msg = r.json()['msg']
        data = r.json()['data']['list']
        try:
            self.assertEqual(200, status_code)
            self.assertEqual('0', ret)
            self.assertIn('会员', data)
        except AssertionError:
            raise AssertionError(msg, "搜索数据中不包括‘会员’内容")

    def test_posts_search(self):
        '''帖子搜索：会员'''
        pass

    def test_course_search(self):
        '''课程搜索：会员'''
        pass

    def test_qa_search(self):
        '''问答搜索：会员'''
        pass

    def test_wiki_search(self):
        '''百科搜索：会员'''
        pass

    def test_video_search(self):
        '''视频搜索：会员'''
        pass

    def test_lm_search(self):
        '''辣妈搜索：会员'''
        pass

    def test_bang_search_(self):
        '''帮搜索：会员'''
        pass

    def test_chat_search_(self):
        '''群聊搜索：会员'''
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
