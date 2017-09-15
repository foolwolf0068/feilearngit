# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 16:46:58 2017

@author: Administrator
"""
# bubble sort
def bubbleSort(lst):
    n=len(lst)
    for i in range(n):
        for j in range(n-1,i,-1):
            if lst[j-1]>lst[j]:
                lst[j],lst[j-1]=lst[j-1],lst[j]
        print("After the ",i+1,"time: ")
        for j in range(n):
            print(lst[j],end=" ")
        print()
    return lst
# advanced bubble sort
def bubbleSortNew(lst):
    n=len(lst)
    flag=0
    for i in range(n):
        for j in range(n-1,i,-1):
            if lst[j-1]>lst[j]:
                lst[j],lst[j-1]=lst[j-1],lst[j]
                flag=1
        print("After the ",i+1,"time: ")
        for j in range(n):
            print(lst[j],end=" ")
        print()
        if flag==0:
            break
        else:
            flag=0
    return lst        
def main():
    lst=[69,65,90,37,92,6]
    newlst=bubbleSort(lst)
    print(newlst)
    
    lst1=[69,65,90,37,92,6]
    newlst1=bubbleSortNew(lst)
    print(newlst1)
main()