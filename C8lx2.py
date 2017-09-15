#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 20:25:43 2017

@author: foolwolf0068
"""

def find(s1,s2):
    if len(s1)<len(s2):
        s1,s2=s2,s1
    if s2 in s1:
        print(s2,"is",s1,"'s substring.")
    else:
        print(s2,"is not",s1,"'s substring.")   

def main():
    s1=input("Enter the 1st string: ")
    s2=input("Enter the 2nd string: ")
    find(s1,s2)

main()