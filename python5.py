#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 10:59:50 2017

@author: foolwolf0068
"""

def sort3num():
    L=[]
    for i in range(3):
        x=float(input('请输入第 %d 个数字'%(i+1)))
        L.append(x)
    L.sort()
    return L

print(sort3num())