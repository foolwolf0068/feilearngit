#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 10:10:16 2017

@author: foolwolf0068
"""
for n in range(10000,100001,10000):
    iterm=1
    e1=1
    for i in range(1,n+1):
        iterm/=i
        e1+=iterm
    print("n=",n,"e=",e1)
    
