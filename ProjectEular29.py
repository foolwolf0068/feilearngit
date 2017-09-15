#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 16:49:07 2017

@author: foolwolf0068
"""
def DisPower(m=2,n=5):
    L=set([a**b for a in range(m,n+1) for b in range(m,n+1)])
    #LNew=set(L)
    return len(L)

print(DisPower(2,100))