#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 17:17:58 2017

@author: foolwolf0068
"""

def strprint(n=5):
    if n<0:
        print('Please check your input!!!')
        return False
    L=[]
    for i in range(5):
        str1=input('Please input the %dth string: '% (i+1))
        L.append(str1)
    L.reverse()
    return L

print(strprint())