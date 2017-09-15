#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 14:39:43 2017

@author: foolwolf0068
"""

def ProjectEular6(n=100):
    a=[x*x for x in range(1,n+1)]
    b=list(range(1,n+1))
    return (sum(b)*sum(b)-sum(a))

# 
c=ProjectEular6(10)
print(c)