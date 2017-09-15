# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 20:52:08 2017

@author: Administrator
"""
#10.9
from math import sqrt
def mean(x):
    n=len(x)
    sum=0
    for i in x:
        sum += i
    return sum/n

def deviation(x):
    a=mean(x)
    n=len(x)
    sum=0
    for i in x:
        sum+=(i-a)**2
    return sqrt(sum/(n-1))

def inputList():
    str1=input("Enter numbers: ")
    items=str1.split()
    lst=[eval(x) for x in items]
    return lst

def main():
    x=inputList()
    print("The mean is:",mean(x))
    print("The standard deviation is:",deviation(x))
    
main()
    