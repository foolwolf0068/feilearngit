#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 13:37:54 2017
笨办法学 Python
@author: foolwolf0068
"""
# ex5
my_name = 'Fei ge'
my_age = 30 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes ='Blue'
my_teeth = 'white'
my_hair = 'black'

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes,my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)
# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." %(my_age, my_height, my_weight, my_age + my_height + my_weight))
print("Feige %r." %my_name)