#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 10:46:59 2017

@author: foolwolf0068
"""

def comsquare():
    import math
    n=-100
    L=[]
    while True:
        if int(math.sqrt(n+100))-math.sqrt(n+100)==0:
            if int(math.sqrt(n+268))-math.sqrt(n+268)==0:
                L.append(n)
        if n>100000:
            return L
        n+=1

print(comsquare())