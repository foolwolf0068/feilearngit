#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 13:14:46 2017

@author: foolwolf0068
"""

import time
for x in range(1,19):
    print(x)
    #time.sleep(1)
    
L=list(range(11,20))
print(L)
for i in range(11,20):
    print(i)
    if i%2==0:
        L.remove(i)
        
print(L)