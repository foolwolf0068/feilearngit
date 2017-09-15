# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 20:07:23 2017

@author: Administrator
"""
def findSmall(lst):
    vmin=lst[0]
    for i in lst:
        if vmin>i:
            vmin=i
    return vmin
    
def indexOfSmallestElement(lst):
    lst1=[]
    smallValue=findSmall(lst)
    for i in range(len(lst)):
        if smallValue >= lst[i]:
            smallValue = lst[i]
            lst1.append(i)
    return smallValue,lst1

def main():
    lst=[-1,-2,2,-2,3,-2]
    lst1=indexOfSmallestElement(lst)
    print("The smallest number in",lst,"is",lst1[0],
          "and the index is",lst1[1:])
    
main()