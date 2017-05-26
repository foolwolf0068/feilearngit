#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 20:58:40 2017

@author: foolwolf0068
enumerate 函数的应用
"""
import string
s=string.ascii_lowercase
e=enumerate(s)
print(s)
print(list(e))

def xread_line(line):
    return((idx,int(val)) for idx,val in enumerate(line) if val!='0')

print(xread_line('0001110101'))
print(list(xread_line('0001110101')))