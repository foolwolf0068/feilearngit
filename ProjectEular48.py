#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 17:32:25 2017

@author: foolwolf0068
"""

def SelfPower(n=10):
    return sum([x**x for x in range(1,n+1)])

print(SelfPower(1000)%(10**10))