# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 18:40:23 2017

@author: Administrator
"""
# 10.6

def isPrime(n):
    if n<0:
        print("The number must be postive!!!")
        return False
    if n==1:
        return False
    for i in range(2,int(n/2)+1):
        if n%i==0 :
            return False
    return True

def creatPrimeList(n):
    lst=[]
    for i in range(1,n+1):
        if isPrime(i):
            lst.append(i)
    return lst

def main():
    count=0
    n=1
    lst=[]
    while count<50:
        if isPrime(n):
            lst.append(n)
            count+=1
        n+=1
    print(lst)

main()
    
        