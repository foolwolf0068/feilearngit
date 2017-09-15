# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:30:36 2017

@author: Administrator
"""
def insertionSort(lst):
    for i in range(1,len(lst)):
        key=lst[i]
        j=i-1
        while j>=0 and lst[j]<key:
            lst[j+1]=lst[j]
            j=j-1
        lst[j+1]=key
    return lst
              
    
def main():
    lst=[31,41,59,26,41,58]
    
    print(insertionSort(lst))
    
main()
            