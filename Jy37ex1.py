#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 20:05:13 2017

@author: foolwolf0068
"""

class Ball:
    def __init__(self,name):
        self.name = name
    def kick(self):
        print("my name is",self.name,",god,you kid me?")
        
b= Ball('toudu')
b.kick()
c= Ball('toucu')
c.kick()

class person:
    name = "feige"
    
d=person()
print(d.name)
        