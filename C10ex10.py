# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 17:01:51 2017

@author: Administrator
"""

def binarySearch(lst,key):
    low=0
    high= len(lst) -1    
    while high>=low :  
        mid=(low+high)//2
        if key < lst[mid] :
            high=mid-1
        elif key==lst[mid] :
            return mid
        else:
            low=mid+1
    return -low-1
def celsius(f):# F to C
    return (f-32)*5/9

def main():
    lst=[2,4,7,10,11,45,50,59,60,66,69,70]
    print(binarySearch(lst,70))
    print(binarySearch(lst,50))
    print(binarySearch(lst,66))
    print(binarySearch(lst,40))
    print(celsius(86))
main()