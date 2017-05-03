#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 15:23:40 2017

@author: foolwolf0068
"""

def eattao(n=10):
    x10=1
    for i in range(n,1,-1):
        x9=(x10+1)*2
        x10=x9
    return x10
print(eattao(n=1))