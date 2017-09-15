#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 17:11:26 2017

@author: foolwolf0068
"""

def ProjectEular30(n):
    sum=0
    for x in str(n):
        sum+=int(x)**len(str(n))
    return sum
# method 1
sum1=0
for i in range(10000,100000):
    if i==ProjectEular30(i):
        sum1+=i
print(sum1) 
# method 2
print([x for x in range(1,100000) if x==ProjectEular30(x)])
print(sum([x for x in range(10000,100000) if x==ProjectEular30(x)]))
