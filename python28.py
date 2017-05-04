#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 17:33:00 2017

@author: foolwolf0068
"""

def suishu(n=5):
    if n<1:
        print('Please check your input!!!')
        return False
    if n==1:
        return 10
    else:
        return (2+suishu(n-1))
print(suishu())