# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 19:28:03 2017

@author: Administrator
"""

from random import randint
def creatList(n):
    lst=[]
    for i in range(n):
        lst.append(randint(0,9))
        
    return lst

def countNumbers(lst):
    counts=10*[0]
    for i in range(len(lst)):
       counts[lst[i]] +=1
    return counts

def main():
    lst=creatList(10)
    print(lst)
    lst1= countNumbers(lst)
    print(lst1)
    
main()