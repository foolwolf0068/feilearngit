#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 23:00:42 2017

@author: foolwolf0068
"""
# method 1
def ProjectEular1(n=1):
    L=[]
    while True:
        if n%3==0 or n%5==0:
            L.append(n)        
        sum0=sum(L)
        if n>=1000:
            return sum(L)-1000
        n+=1
print(ProjectEular1(1))

#method 2
L1=[]
for i in range(1,1000):
    if i%3==0 or i%5==0:
        L1.append(i)
print(sum(L1))

#method 3
L2=list(range(0,1000))
print(sum(L2[3:1000:3])+sum(L2[5:1000:5])-sum(L2[15:1000:15]))

#method 4
print(sum([x for x in range(1000) if x % 3== 0 or x % 5== 0]))