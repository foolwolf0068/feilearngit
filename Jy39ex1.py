#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 14:59:13 2017

@author: foolwolf0068
"""

class Turtle:
    def __init__(self,x):
        self.x = x

class Fish:
    def __init__(self,y):
        self.y = y

class Pool:
    def __init__(self,x,y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)
    
    def printnum(self):
        print("In the pool,there are",self.turtle.x,"turtles and",self.fish.y,"fishes.")

pool = Pool(2,10)
pool.printnum()

class C:
    count = 0
    

a = C()
b = C()
c = C()
c.count += 10
C.count += 100
print("a.count=",a.count)
print("b.count=",b.count)
print("c.count=",c.count)
print("C.count=",C.count)