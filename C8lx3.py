#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 20:36:05 2017

@author: foolwolf0068
"""

def isValid(s):
    if isLetterNum(s) and isLetterCount(s):
        return True
    else:
        return False

def isLetterNum(s):
    if len(s)>=8:
        for i in s:
            if ("a"<=i<="z" )or ("A"<=i<="Z") or ("0"<=i<="9"):
                return True
            else:
                return False
    else:
        return False

def isLetterCount(s):
    count0=0
    for i in s:
        if ("0"<=i<="9"):
            count0+=1
    if count0>=2:
        return True
    else:
        return False
def main():
    s=input("Enter your password:")
    if isValid(s):
        print(s,"is a valid password!")
    else:
        print(s,"is not a valid password!")
main()    