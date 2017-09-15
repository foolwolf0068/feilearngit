#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 14:18:57 2017

@author: foolwolf0068
Chapter 7
例子
"""
from Circle import Circle
c1=Circle(5)
print(c1.radius)
print(c1.gePerimeter())

# check point 7.9
class A(object):
    def __init__(self,i):
        self.i=i
        
def main():
    a=A(2)
    print(a.i)

main()

# 7.10
class B(object):
    def B1(self):
        self.radius=3
        
class C(object):
    def __init__(self):
        self.radius=3
    def setRadius(radius):
        self.radius=radius