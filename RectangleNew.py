#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:54:39 2017

@author: foolwolf0068
"""

class Rectangle1(object):
    """
    the width and length of Rectangle
    """
    def __init__(self):
        self.width=0
        self.length=0
    def setSize(self,size):
        self.width,self.length=size
    def getSize(self):
        return self.width,self.length
    #add one sentence
    size=property(getSize,setSize)
    
if __name__=="__main__":
    r1=Rectangle1()
    r1.width=3
    r1.length=4
    print(r1.getSize())
    r1.Size=30, 40
    print(r1.width,r1.length)
    