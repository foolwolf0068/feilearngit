#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 22:50:56 2017
笨办法学 Python
@author: foolwolf0068

How to run this program?
 python ex17.py test.txt copied.txt
 
 cat copied.txt # print the content of copied.txt on screen
"""
# ex17
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" %(from_file, to_file))

# we could do these two on one line too, how?
input1 = open(from_file)
indata = input1.read()

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue,CTRL-C to abort.")
input()

output = open(to_file,'w')
output.write(indata)

print("Alright, all done.")
output.close()
input1.close()