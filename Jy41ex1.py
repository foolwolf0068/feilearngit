#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 16:55:09 2017
小甲鱼视频
@author: foolwolf0068
"""

class Rectangle:
    def __init__(self,x,y): # 不能对 init 做返回
        self.x = x
        self.y = y
        
    def getPeri(self):
        return 2 * (self.x + self.y)
    
    def getArea(self):
        return self.x * self.y
    
rect = Rectangle(3,4)
print(rect.getArea())
print(rect.getPeri())


class Capstr(str):
    def __new__(cls,string):
        string = string.upper()
        return str.__new__(cls,string)
    
a = Capstr("I love feige.com")
print(a)

class C:
    def __init__(self):
        print("this is __init__")
        
    def __del__(self):
        print("this is __del__")
        
c1 = C()
c2 = c1
c3 = c2
del c3
del c2
del c1
