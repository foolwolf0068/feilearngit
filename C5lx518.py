#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 04:06:40 2017

@author: foolwolf0068
"""
#编程题 5.22
# 5.22
def smallFactor(a=2,b=1000):
    #from C6lx2 import isPrime
    if a>b:
        b,a=a,b
    count=0
    for i in range(a,b+1):
        if isPrime(i):
            print(i,end=" ")
            count+=1        
            if count%8==0:
                print()
def isPrime(n):
    if n <0:
        print("n must be a positive number...")
        return 0
    if n==1:
        return False
    if n==2:
        return True
    n0=2
    while n0<=n/2+1:
        if n%n0==0:
            return False
        else:
            n0+=1
    return True

smallFactor(2,1000)
    
