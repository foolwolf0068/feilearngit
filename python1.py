#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 10:02:44 2017

@author: foolwolf0068
"""

def diffnumber(n=5):
    if n<1 or n>9:
        print('Please check your input!!!')
        return False
    L=[]
    for i in range(1,n):
        for j in range(1,n):
            for k in range(1,n):
                if i!=j and j!=k and i!=k:
                    L.append(i*100+j*10+k)
                    print(i*100+j*10+k)
    return L
diffnumber()