#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 14:26:40 2017

@author: foolwolf0068
"""
a='feige is the 1 best'
n=0
n1=0
n2=0
n3=0
for x in a:
    if x.isalpha():
        n+=1
    elif x.isspace():
        n1+=1
    elif x.isdigit():
        n2+=1
    else:
        n3+=1
            
print(n,n1,n2,n3)
