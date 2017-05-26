#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 00:02:28 2017

@author: foolwolf0068
"""

def Fibnum(n=3):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return Fibnum(n-1)+Fibnum(n-2)
n=1
L=[]
while Fibnum(n)<=4000000:
    if Fibnum(n)%2==0:
        L.append(Fibnum(n))
    n+=1
print(L)
print(sum(L))
    
    