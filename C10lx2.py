# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 14:57:21 2017

@author: Administrator
"""
# 10.2
def lsrRever(lst):
    NewList = []
    for i in range(len(lst)-1,-1,-1):
        NewList.append(lst[i])
    return NewList

def main():
    lst=list(range(8))
    print(lst)
    print(lsrRever(lst))
    
main()