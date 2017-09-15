#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 20:06:42 2017
笨办法学PYthon
@author: foolwolf0068
"""
# ex13
'''
how to run this script?
It likes those:
run it in terminal 
python ex13.py 1st 2nd 3rd
python ex13.py apple cheese bread
python ex13.py fei ge. qiaoer

'''
from sys import argv

script, first, second, third = argv

print('The script is called:', script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
"""
'''This script needs to check again!'''
Fei1, Fei2, Fei3 = input("Please input at least 3 variables:")
print("Your first variable is:", Fei1)
print("Your second variable is:", Fei2)
print("Your third variable is:", Fei3)
""""