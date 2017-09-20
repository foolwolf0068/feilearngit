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
    


def main():
    rect = Rectangle(3,4)
    print(rect.getArea())
    print(rect.getPeri())

if __name__ == "__main__":
    main()
