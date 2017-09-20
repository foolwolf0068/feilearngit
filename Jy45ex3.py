#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 16:13:48 2017
小甲鱼视频
@author: foolwolf0068
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    
        
    def __setattr__(self, name, value):
        if name == "square":
            self.width = value
            self.height = value
        else:
            # method 1
            super().__setattr__(name,value) # recommandition

            # method 2
            #self.__dict__[name] = value
            # method 3
            #self.name = value  this method is wrong!!!
        
    def getArea(self):
        return self.width * self.height
    

def main():
    r1 = Rectangle(4,5)
    print(r1.getArea())
    r1.square = 10
    print(r1.width)
    print(r1.height)
    print(r1.getArea())
    print(r1.__dict__)
    
  
        

if __name__ == "__main__":
    main()
