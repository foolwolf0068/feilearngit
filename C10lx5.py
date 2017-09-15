# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 17:53:24 2017

@author: Administrator
"""

def inputList():
    str1=input("Enter ten numbers: ")
    items=str1.split()
    lst=[eval(x) for x in items]
    return lst

def distinctList(lst):
    lst1=[]
    for i in lst:
        if i not in lst1:
            lst1.append(i)
    return lst1

def main():
    lst=inputList()
    lst1=distinctList(lst)
    print("The distinct numbers are:",lst1)
    
main()