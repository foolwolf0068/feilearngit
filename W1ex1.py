#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:12:03 2017
中国大学MOOC课程
《Python 语言程序设计》
第三周
@author: foolwolf0068
"""
# month.py
months = 'JanFebMarAprMayJunJulAugSepOctNovDec'
n = input("请输入月份(1-12):")
pos = (int(n)-1)*3
monthAbbrev = months[pos:pos+3]
print("%d月份的简写是%s." % (int(n),monthAbbrev))

# weekday

days = 'MonTusWedThuFriSatSun'
days2 = '一二三四五六日'
n = input("请输入星期数(1-7):")
pos = (int(n) - 1)
pos1 = pos*3
dayAbbrev = days[pos1 : pos1 + 3]
daychi = days2[pos]
print("星期'%s'的简写是'%s'."%(daychi, dayAbbrev))
