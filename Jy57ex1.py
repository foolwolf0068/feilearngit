#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 04:09:37 2017
小甲鱼视频 正则表达式
@author: foolwolf0068
"""

import re
re.search(r'feige','i love feige de feige')
# 匹配 IP 地址
pattern = r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])'


print(re.search(pattern,'255.255.123.1'))

p1 = r'\d{3}\s*\-\s*\d{3,8}'
print(re.search(p1,'010  -   123478'))

# check password

p2 = r'[a-zA-Z\_][0-9a-zA-Z\_]{0,19}'

print(re.match(p2,'aA010_123478'))
# check mailbox

p3 = r'([a-z]+)(\.)?([a-z]*)(\@)([a-z]+)(\.)([a-z])+'
print(re.match(p3,'someone@gmail.com'))
if re.match(p3,'someo.ne@gmail.com'):
    print(re.match(p3,'someo.ne@gmail.com'))