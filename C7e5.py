#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 10:21:05 2017

@author: foolwolf0068

"""

from Circle import Circle
def main():
    myCircle=Circle()
    n=5
    printArea(myCircle,n)
    print("\nRadius is",myCircle.radius)
    print("n is",n)
    
def printArea(c,times):
    print("Radius \t\tArea")
    while times>=1:
        print(c.radius,"\t\t",c.getArea())
        c.radius+=1
        times-=1
        
main()
# check point 7.11
class Count(object):
    def __init__(self,count=0):
        self.count=count
def main():
    c=Count()
    times=0
    for i in range(100):
        increment(c,times)
    print("count is",c.count)
    print("times is",times)
def increment(c,times):
    c.count+=1
    times+=1
main()
# check point 7.12
class Count1(object):
    def __init__(self,count=0):
        self.count=count
def main():
    c=Count1()
    n=1
    m(c,n)
    print("count is",c.count)
    print("n is",n)
def m(c,n):
    c=Count1(5)
    n=3
main()