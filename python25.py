#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 17:10:47 2017

@author: foolwolf0068
"""

def fact(n=5):
    if n<0:
        print('Please check your input!!!')
        return False
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
#print(fact())
print(sum(map(fact,range(1,20))))

# 26 
print('5! = %d .'% fact())