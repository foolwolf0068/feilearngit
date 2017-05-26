#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 18:06:40 2017

@author: foolwolf0068
Tencent education video
"""

score=90
scores=[80,90.2,'a','feige',90,90]
print(scores)
print(type(scores))
z=90.2
print(id(scores[1]))
print(id(z))
print(z in scores)
name=[1,2,3]
name1=[88,22]
print(name+name1)
print(name*2)
import platform
print(platform.uname())
print(divmod(5,2))