#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 16:56:06 2017
笨办法学 PYthon
@author: foolwolf0068
"""
# ex6
x = "There are %d types of people." % 10 # %d = 10
binary = 'binary'
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)

print("I said: %r." % x)
print("I also said: '%s'." % y)

hilarious = False
joke_evalution = "Isn't that joke so funny?! %r"

print(joke_evalution % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
