#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 21:20:24 2017
笨办法学 PYthon
@author: foolwolf0068
"""

from sys import argv

script, filename = argv

txt = open(filename)

print("Here is your file %r:"% filename)
print(txt.read())
txt.close()
print("Type the filename again:")

file_again = input("--> ")
txt_again = open(file_again)
print(txt_again.read())
txt_again.close()
