#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 11:12:51 2017

@author: foolwolf0068
"""
def pnine():
    print('------------乘法口诀表----------------')
    for i in range(1,10):
        for j in range(1,i+1):
            print('%d x %d = %2d '%(j,i,j*i),end=' ')
        print('')
            
pnine()

import time
for x in range(1,19):
    print(x)
    time.sleep(1)
 