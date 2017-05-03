#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 10:10:43 2017

@author: foolwolf0068
"""

def lirun():
    profit=float(input('请输入利润(单位：元）'))
    print('您输入的利润为：%d 元'%(profit))
    nbase=[1000000,600000,400000,200000,100000,0]
    rate=[0.01,0.015,0.03,0.05,0.075,0.1]
    sum1=0
    print('---------------------')
    for i in range(0,6):
        if profit >nbase[i]:
            sum1+=(profit-nbase[i])*rate[i]
            print((profit-nbase[i])*rate[i])
            profit=nbase[i]
    print('---------------------')
    return sum1
#print('--------------')
print(lirun())