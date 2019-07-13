#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 17:57
# @Author  : Bear
# @Site    : 
# @File    : md5_encryption.py
# @Software: PyCharm

from hashlib import md5


# 利用md5加密，将传入的密码进行加密
def md5_encryption(string_):
    if isinstance(string_, str):
        m = md5()
        m.update(b'%s' % (string_.encode('utf8')))
        encodeStr = m.hexdigest()
        return encodeStr
    else:
        raise TypeError('必须传入字符串类型')
