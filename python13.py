#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 14:18:50 2017

@author: foolwolf0068
"""

def shuixh():
    L1=[]
    for x in range(100,1000):
        L=str(x)        
        a=int(L[0])**3+int(L[1])**3+int(L[2])**3
        if a==x:
            L1.append(x)
    return L1
#test
print(shuixh())