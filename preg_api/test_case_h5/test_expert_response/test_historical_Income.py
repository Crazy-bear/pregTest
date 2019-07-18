#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 11:24
# @Author  : Bear
# @Site    : 
# @File    : test_historical_Income.py
# @Software: PyCharm


# 历史收入
import unittest
import requests
from preg_api.common.login import *


class HistoricalIncome(unittest.TestCase):
    '''历史收入'''
    def setUp(self) -> None:
        self.t_skey = login('evan10@qq.com', '123456')
        # pprint(self.t_skey)

    def test_historical_income(self):
        '''默认当前月份之前的历史收入'''
        querystring = {"month": ""}
        headers = {'Cookie': 't_skey' + '=' + self.t_skey}
        r = requests.request('POST', h5_historical_income_url, headers=headers, params=querystring)
        # pprint(r.json())
        status_code = r.status_code
        ret = r.json()['ret']
        msg = r.json()['msg']
        try:
            self.assertEqual(200, status_code)
            self.assertEqual('0', ret)
            self.assertIn('ok', msg)
        except AssertionError:
            raise AssertionError('获取历史数据失败：' + msg)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
