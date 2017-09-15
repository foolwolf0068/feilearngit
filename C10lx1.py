# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 13:50:04 2017

@author: Administrator
"""
# 10.1
def scoreRating(best,n):
    if n >= best - 10:
        return "A"
    elif n >= best - 20:
        return "B"
    elif n >= best - 30:
        return "C"
    elif n >= best - 40:
        return "D"
    else:
        return "F"
    
def listRead(lst):
    best=max(lst)
    lstNew=[]
    for i in range(len(lst)):
       lstNew.append(scoreRating(best,lst[i]))
    return lstNew

def main():
    str1=input("Enter scores: ")
    items=str1.split()
    lst=[eval(x) for x in items]
    lst1=listRead(lst)
    for i in range(len(lst1)):
        print("Student ",i+1," score is ",lst[i],"and grade is ",lst1[i])
        
main()