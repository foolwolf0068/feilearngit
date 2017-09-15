# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 16:32:25 2017

@author: Administrator
"""
"""
# 
lst=[]
print("Enter ten numbers: ")
for i in range(10):
    lst.append(input())
"""
# 10.9
def linearsearch(lst,key):
    for i in range(len(lst)):
        if key == lst[i]:
            return i
    return -1

def main():
    lst=[1,4,4,2,5,-3,6,2]
    print(linearsearch(lst,4))
    print(linearsearch(lst,-4))
    print(linearsearch(lst,6))
main()
def binarySearch(lst,key):
    low=0
    high= len(lst) -1
    mid=(low+high)//2
    while high>=low :     
        if key < lst[mid] :
            high=mid-1
        elif key==lst[mid] :
            return mid
        else:
            low=mid+1
    return -low-1

def main():
    lst=[2,4,7,10,11,45,50,59,60,66,69,70]
    print(binarySearch(lst,2))
    
main()