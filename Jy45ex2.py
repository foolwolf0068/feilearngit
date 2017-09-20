#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 16:13:48 2017
小甲鱼视频
@author: foolwolf0068
"""

class C:
    def __getattribute__(self, name):
        print("getattribute")
        return super().__getattribute__(name)
    def __getattr__(self, name):
        print("getattr")
        
    def __setattr__(self, name,value):
        print("setattr")
        return super().__setattr__(name,value)
    def __delattr__(self, name):
        print("delattr")
        return super().__delattr__(name)
    

def main():
    c = C()
    c.x
    c.x = 1
    del c.x
  
        

if __name__ == "__main__":
    main()
