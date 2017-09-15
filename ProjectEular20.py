#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 16:15:40 2017

@author: foolwolf0068
"""

def ProjectEular20(n):
    sum=0
    for x in str(n):
        sum+=int(x)
    return sum

def factnum(n):
    if n <0:
        print('Please check your enter...')
        return 0
    if n==0 or n==1:
        return 1
    else:
        return n*factnum(n-1)
    
print(ProjectEular20(factnum(100)))