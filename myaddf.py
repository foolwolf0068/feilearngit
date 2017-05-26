#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 09:49:30 2017

@author: foolwolf0068
"""

def add_function(a,b):
    """
    The function is to add two number.
    """
    print(a+b)
    return a+b
if __name__=='__main__':
    add_function(2,3)
from functools import reduce
f=reduce(add_function,list(range(10)))
print(f)