# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 13:58:50 2017

@author: Administrator
求π的近似值
"""
# method 1 概率法
from random import random
def calPi1(n):
    n=1000#eval(input("Enter the number of points:"))
    count=0
    for i in range(n):
        x = random()
        y = random()
        if (x*x+y*y)<=1:
            count += 1
    return 4*count/n
# Method 2 割圆法
def calPi2(n):
    k=3.0
    y2=1.0
    s=6
    i=0
    while i <=n:
        s *= 2
        y2 = 2-(4-y2)**0.5
        i += 1
        k *=2
    return k*y2**0.5
# method 3 公式法
def calPi3():
    pi=2.0
    temp=2.0
    numerator=1
    denominator=3
    while temp > 1e-16:
        temp *=(numerator/denominator)
        pi += temp
        numerator += 1
        denominator += 2
    return pi
        
def main():
    print("Method 1 pi=",calPi1(10000000))        
    print("Method 2 pi=",calPi2(13))
    print("Method 3 pi=",calPi3())
main()