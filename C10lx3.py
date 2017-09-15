# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 15:18:30 2017

@author: Administrator
"""

# 10.3
def createList():
    str1=input("Enter integers between 1 and 100: ")
    items=str1.split()
    lst=[eval(x) for x in items]
    return lst

def countNumbers(lst):
    counts=100*[0]
    for i in range(len(lst)):
       counts[lst[i]-1] +=1
    return counts

def displayCount(counts):
    for i in range(len(counts)):
        if counts[i] != 0:
            if counts[i] > 1:
                print(i+1,"occurs",counts[i],"times")
            else:
                print(i+1,"occurs",counts[i],"time")
            
def main():
    lst=createList()
    counts=countNumbers(lst)
   # print(counts)
    displayCount(counts)
    
main()


        