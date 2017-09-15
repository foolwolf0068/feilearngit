#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 23:01:06 2017

@author: foolwolf0068
"""
# 8.4
def count(s,ch):
    count0=0
    for i in s:
        if i == ch:
            count0+=1
    return count0

def main():
    s="feige"#input('Enter a string:')
    ch='e'#input('Enter a letter:')
    print(ch,"happens in",s,count(s,ch),"times.")
main()


# 8.6
def countLetters(s):
    count0=0
    for i in s:
        if ("a"<=i<="z" or "A"<=i<="Z"):
            count0+=1
    return count0

def main1():
    s= input("Enter a string: ")
    print(s,"has",countLetters(s),'letters.')
main1()