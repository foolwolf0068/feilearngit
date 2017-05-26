#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 19:41:38 2017

@author: foolwolf0068
"""
# 注释
"""
请计算：
19+2*4-8/2
"""
#请计算：19+2*4-8/2
a=19+2*4-8/2
print(a)
b='feige'
print(b+str(a))
print(b+repr(a))
docs="c:\\news"
print(docs)
docs=r"c:\news"
print(docs)
docs1='c:\news'
print(docs1)
docs2=r'c:\news'
print(docs2)
lan='study python'
print(lan.index('t'))
print(lan.count('t'))
c=lan[:]
#c=lan.copy()
print(id(c))
print(id(lan))
print(c)
#lan[2]='f'
print(c,lan)
print('f'.join(c))
name='飞哥'
print(type(name))
print(name.encode())
print(name.encode().decode())
for i in range(5):
    print(i,end='')