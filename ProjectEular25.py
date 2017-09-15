#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 16:27:25 2017

@author: foolwolf0068
"""

def factnum(n):
    if n <0:
        print('Please check your enter...')
        return 0
    if n==1 or n==2:
        return 1
    else:
        return factnum(n-1)+factnum(n-2)
    
def Facnum(a=3):
    n=1    
    while True:
       if len(str(factnum(n)))>=a:
           return n
       else:
           n+=1

print(Facnum(5),factnum(17))