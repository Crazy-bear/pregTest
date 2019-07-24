#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 19:36
# @Author  : Bear
# @Site    : 
# @File    : test_post.py
# @Software: PyCharm
import unittest
import json
from requests import request
from preg_api.common.api_url import *
from preg_api.common.login import *


# 发帖
class Post(unittest.TestCase):
    '''发帖'''
    def setUp(self):
        self.t_skey = login('13510278144', '123456')
        # pprint(self.t_skey)

    def test_post_ordinary(self):
        '''普通帖'''
        d = [{"type": "text",
             "info": {"content": "testtest自动化测试testtest自动化测试testtest自动化测试"}
              }
             ]

        querystring = {"type": "0",
                       "active_type": "",
                       "source_from": "",
                       "title": "testtest555",
                       "record_id": "",
                       "bid": "8184",
                       "content": json.dumps(d),
                       "ext": ""}
        headers = {'Cookie': 't_skey' + '=' + self.t_skey}
        r = requests.request("GET", post_url, headers=headers, params=querystring)
        # pprint(r.json())
        status_code = r.status_code
        ret = r.json()['ret']
        msg = r.json()['msg']
        title = r.json()['data']['topic_info']['title']
        try:
            self.assertEqual(200, status_code)
            self.assertEqual('0', ret)
            self.assertEqual('发帖成功', msg)
            self.assertIn('test', title)
        except AssertionError:
            raise AssertionError('发帖失败')

    def test_post_taobao(self):
        '''淘宝帖'''
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
