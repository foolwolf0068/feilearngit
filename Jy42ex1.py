#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 17:48:28 2017
小甲鱼视频
@author: foolwolf0068
"""

class New_int(int):
    def __add__(self,other):
        return int.__sub__(self,other)
    def __sub__(self,other):
        return int.__add__(self,other)
    
a = New_int(3)
b = New_int(5)

print(a + b)
print(a - b)

"""
这段代码的魔法方法是不能用的
class Try_int(int):
    def __add__(self,other):
        return self + other #无线递归
    def __sub__(self,other):
        return self - other
a = Try_int(3)
b = Try_int(5)
print(a + b)    
"""
class Try_int(int):
    def __add__(self,other):
        return int(self) + int(other)
    def __sub__(self,other):
        return int(self) - int(other)
a = Try_int(3)
b = Try_int(5)
print(a + b)   