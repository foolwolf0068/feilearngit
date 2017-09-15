#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 00:38:02 2017

@author: foolwolf0068
"""

# python 语言程序设计
print(format('F'*7,'<10s'),format('U','<5s'),format('NN','<5s'))

# 1.6
sum0=sum(list(range(1,10)))
print(sum0)
# 1.7
def leijic(n=3):
    if (n<=1):
        return 1
    else:
        return leijic(n-1)+(-1)**(n-1)/(2*n-1)
import math   
print(4*leijic(6),4*leijic(100),math.pi)
n=8
while n<900:
    err=abs(4*leijic(n)-math.pi)
    if err<0.05:
        print(n,4*leijic(n))
        break
    n+=1

num=3120324986
time0=3600*365
for i in range(1,6):
    num=num+time0*i//7+time0*i//45-time0*i//13
    print('The '+str(i)+'th year is '+str(num)+'!')