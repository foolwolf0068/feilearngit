#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 16:13:48 2017
小甲鱼视频
@author: foolwolf0068
"""


class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    def __get__(self, instance, owner):
        return self.fget(instance)
    
    def __set__(self, instance, value):
        self.fset(instance, value)
        
    def __delete__(self, instance):
        self.fdel(self, instance)
        
class C:
    def __init__(self):
        self._x = None
    def getX(self):
        return self._x
    def setX(self, value):
        self._x = value
    def delX(self):
        del self._x
    x = MyProperty(getX, setX, delX)
    
    

def main():
    c = C()
    c.x = 'fege'
    print(c.x)
    print(c._x)
    del c.x
 #   c._x
    
    
    
  
        

if __name__ == "__main__":
    main()
