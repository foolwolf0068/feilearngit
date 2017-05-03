#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 11:10:41 2017

@author: foolwolf0068
"""

def copynumarry():
    a=[1,2,3,4,5]
    b=a[:] # or b=copy.copy(a)
    return b

print(copynumarry())