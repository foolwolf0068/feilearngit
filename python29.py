#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 17:38:11 2017

@author: foolwolf0068
"""

def numreprint(n):
    
    x=str(n)
    #print(x)
    nx=len(x)
    L=[]
    for i in range(nx):
        #print(x[nx-i-1])
        L.append(x[nx-i-1])
    return nx,L
print(numreprint(26379))
