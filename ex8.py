#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 17:26:10 2017
笨办法学 Python
@author: foolwolf0068
"""
# ex 8
formatter = '%r %r %r %r'

print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", 'three', 'Four'))
print(formatter % (True, False, True, False))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
        "I had this thing.",
        "That you could type up right",
        "But it didn't sing",
        "So I said goodnight."))

