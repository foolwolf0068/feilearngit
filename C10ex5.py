# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 15:43:11 2017

@author: Administrator
"""

# 10-11
def selectSort(lst):
    for i in range(len(lst)-1):
        currentMin = lst[i]
        currentMinIndex=i
        
        for j in range(i+1,len(lst)):
            if currentMin >lst[j]:
                currentMin=lst[j]
                currentMinIndex=j
        if currentMinIndex != i:
            lst[currentMinIndex]=lst[i]
            lst[i]=currentMin
    return lst

def insertSort(lst):
    for i in range(1,len(lst)):        
        currentElement=lst[i]
        k=i-1
        while k>=0 and lst[k]>currentElement:
            lst[k+1]=lst[k]
            k-=1
        lst[k+1]=currentElement
    return lst

def main():
    import random
    lst=[1,9,4.5,10.6,5.7,-4.5]
    print(selectSort(lst))
    random.shuffle(lst)
    print(lst)
    # lst=[1,9,4.5,10.6,5.7,-4.5]
    print(insertSort(lst))
main()

