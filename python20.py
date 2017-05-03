#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 14:55:25 2017

@author: foolwolf0068
"""

def bounce(h0=100,tim=10):
    if h0<0 or tim<1:
        print('Please check your input!!!')
        return False
    H=[]
    S=[]
    h=h0
    for i in range(1,tim+1):
        h*=0.5
        H.append(h0)
        if i==1:
            s0=h0+h
            #S.append(s0)
        else:
            s0*=0.5
        S.append(s0)
    return h,sum(S)-h
print(bounce(100,10))            
        
    
        