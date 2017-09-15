#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 14:46:46 2017

@author: foolwolf0068
"""
#import math

def ProjectEular14(a=1000000):
    L=[]
    for n in range(1,a+1):
        count=1   
        while  True:
            if n%2==0:
                n/=2
                count+=1
                if n<=1:
                    break
            else:
                n=3*n+1
                count+=1
            #count+=1
        L.append(count)
    return L

#Test
amax=max(ProjectEular14(1000000))
for i,j in enumerate(L):           
    if j==amax:
        print(i+1,j)