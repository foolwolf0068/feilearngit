#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:42:32 2017

@author: foolwolf0068
"""

"""
study __getattr__ and __setattr__

"""
class Rectangle(object):
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
if __name__=="__main__":
    r=Rectangle()
    r.width=3
    r.length=4
    print(r.getSize())
    r.setSize((30,40))
    print(r.width,r.length)
while 1:
    print("this is a division program.")
    c = input("input 'c' continue, otherwise logout:")
    if c == 'c':
        a = input("first number:")
        b = input("second number:")
        try:
            print(float(a)/float(b))
            print("*************************")
        except ZeroDivisionError:
            print("The second number can't be zero!")
            print("*************************")
    else:
        break    
