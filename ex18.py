#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 23:53:11 2017
笨办法 学Python
@author: foolwolf0068
"""
# ex18
# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" %(arg1, arg2))
    
# ok, that *args is actuallu pointless, we can just do this
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" %(arg1, arg2))
    
# this just takes one argument
def print_one(arg1):
    print("arg1: %r" % arg1)
    
# this one takes no arguments
def print_none():
    print("I got nothing.")
    
print_two('Fei','Yan')
print_two_again('Qiao', "li")
print_one("First!")
print_none()