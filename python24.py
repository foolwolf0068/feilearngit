#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 17:00:36 2017

@author: foolwolf0068
"""
def fenshu(n=20):
    if n<1:
        print('Please check your input!!!')
        return False
    a,b=1,2
    L=[]
    for i in range(n):
        L.append(b/a)
        a,b=b,a+b
    return L

print(sum(fenshu(20)))
