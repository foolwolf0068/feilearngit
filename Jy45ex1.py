#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 16:13:48 2017
小甲鱼视频
@author: foolwolf0068
"""

class C:
    def __init__(self,size = 10):
        self.size = size
    
    def getSize(self):
        return self.size
    
    def setSize(self,value):
        self.size = value
        
    def delSize(self):
        del self.size
    x=property(getSize,setSize,delSize)


c = C()
print(c.x)

def Fibs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        c = Fibs(n-1) + Fibs(n-2)
        return (int(c/2) if (c % 2) == 0 else c)

def newfib(n):
    return [Fibs(x) for x in range(1,n+1)]

print(newfib(12))
        
