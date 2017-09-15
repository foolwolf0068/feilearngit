#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 15:39:05 2017

@author: foolwolf0068
"""

def ProjectEular16(n):
    if n<0:
        print('Please check your enter...')
        return
    L=[]
    str1=str(n)
    for s in str1:
        L.append(int(s))        
    #Lnew=int(L)
    return sum(L)

print(ProjectEular16(2**1000))