#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 18:00:35 2017

@author: foolwolf0068
"""
# 8.15
def ISBN10(s):
    return s+calTenthnumber(s)
    
def calTenthnumber(s):
    num1=len(s)
    if num1 == 9:
        sum1=0
        for i in range(1,10):
            sum1+=i*int(s[i-1])
        a1=sum1%11
        if a1 == 10:
            return "X"
        else:
            return str(a1)
    else:
        print("Check your enter String...")
        return "F"
def main():
    s=input("Enter the 1st 9 digits of an ISBN-10 as a string:\n")
    print("The ISBN-10 number is",ISBN10(s))
main()            
        