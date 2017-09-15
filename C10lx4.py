# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 17:34:11 2017

@author: Administrator
"""

# 10.4
def inputList():
    str1=input("Enter the scores: ")
    items=str1.split()
    lst=[eval(x) for x in items]
    return lst

def scoreRate(lst):
    aver1=sum(lst)/len(lst)
    uppercount=0
    lowercount=0
    for i in lst:
        if i >=aver1:
            uppercount+=1
        else:
            lowercount+=1
    print("There are ",uppercount,"above the average and ",lowercount,"below the average.")

def main():
    lst1=inputList()
    scoreRate(lst1)
    
main()        
