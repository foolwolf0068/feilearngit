#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 23:31:31 2017

@author: foolwolf0068
"""
# 8.7
def getNumber(s):
    for i in s:
        if i.isalpha():
            print(letterToNum(i),end="")
        else:
            print(i,end="")   
    
def letterToNum(ch):
    ch=ch.lower()
    if ch in ['a','b','c']:
        return '2'
    elif ch in ['d','e','f']:
        return '3'
    elif ch in ['g','h','i']:
        return '4'
    elif ch in ['j','k','l']:
        return '5'
    elif ch in ['m','n','o']:
        return '6'
    elif ch in ['p','q','r','s']:
        return '7'
    elif ch in ['t','u','v']:
        return '8'
    elif ch in ['w','x','y','z']:
        return '9'
def main():
    s=input("Enter a string:")
    getNumber(s)
    
main()
    