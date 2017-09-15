#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 21:02:41 2017

@author: foolwolf0068
"""

def reverse(s):
    str1=""
    for i in s:
        str1=i+str1
    return str1

#print(reverse("102"))

def main():
    s=input("Enter a string:")
    print(s,"reverses to",reverse(s))
main()