#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 19:06:56 2017

@author: foolwolf0068
"""

def isPalindrome(s):
    low=0
    high=len(s)-1
    while low<high:
        if s[low]!=s[high]:
            return False
        low+=1
        high-=1
    return True
def main():
    s=input("Enter a string: ")
    if isPalindrome(s):
        print(s,"is a palindrome.")
    else:
        print(s,"is not a palindrome.")

main()
