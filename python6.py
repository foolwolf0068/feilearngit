#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 11:05:22 2017

@author: foolwolf0068
"""

def fib(n):
    if n<0:
        print('Please check your input!!!')
        return False
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
# test
print(fib(10))