#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 14:43:52 2017

@author: foolwolf0068
"""

def leijia(a,n):
    x=str(a)
    sum1=0
    L=[]
    for i in range(1,n+1):
        L.append(x*i)
    for j in range(len(L)):
        sum1+=int(L[j])
        
    return sum1
print(leijia(4,4))