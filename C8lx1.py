#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 20:11:52 2017

@author: foolwolf0068
"""

s=input("Enter your SSN like 'ddd-dd-dddd': ")
if s[:2].isdigit() and s[4:5].isdigit() and s[7:10].isdigit()\
    and s[3]=='-' and s[6]=='-' and len(s)==11:
    print(s,"is a Valid SSN")
else:
    print(s,"is not a Valid SSN")
    