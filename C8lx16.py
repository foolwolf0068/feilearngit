#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 18:18:36 2017

@author: foolwolf0068
"""
# 8.16
def ISBN13(s):
    return s+calTenthnumber(s)
    
def calTenthnumber(s):
    num1=len(s)
    if num1 == 12:
        sum1=0
        for i in s:
            sum1+=int(i)        
        for i in range(2,13,2):
            sum1+=2*int(s[i-1])
        a1=10-sum1%10
        if a1 == 10:
            return "0"
        else:
            return str(a1)
    else:
        print("Check your enter String...")
        return "F"
def main():
    s=input("Enter the 1st 12 digits of an ISBN-13 as a string:\n")
    print("The ISBN-13 number is",ISBN13(s))
main()            
        