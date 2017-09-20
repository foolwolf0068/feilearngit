#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 16:13:48 2017
小甲鱼视频
@author: foolwolf0068
"""

class MyDescriptor:
       
    def __get__(self, instance, owner):
        print("Getting...", self,instance, owner)
        
    def __set__(self,instance,value):
        print("Setting...", self,instance, value)
        
    def __delete__(self,instance):
        print("deleting...", self, instance)

class Test:
    x = MyDescriptor()
    
class Mproperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    def __get__(self, instance, owner):
        return self.fget(instance)
    
    def __set__(self, instance, value):
        self.fset(instance, value)
        
    def __del__(self, instance):
        self.fdel(self, instance)
        
        
    

def main():
    test = Test()
    test.x
    test
    Test
    test.x = "X-feige"
    del test.x
    
  
        

if __name__ == "__main__":
    main()
