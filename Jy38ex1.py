#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 20:18:11 2017

@author: foolwolf0068
"""

class Parent:
    def hello(self):
        print("father...")

class child(Parent):
    pass

class child1(Parent):
    def hello(self):
        print("child...")
p=Parent()

p.hello()

c=child()
c.hello()

c1=child1()
c1.hello()    