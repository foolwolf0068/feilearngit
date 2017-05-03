#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 13:29:17 2017

@author: foolwolf0068
"""
# 11

def tuzi(n):
    if n<=0:
        print('Please check your input!!!')
        return False
    if n==1 or n==2:
        return 1
    else:
        return tuzi(n-1)+tuzi(n-2)
    
print(tuzi(2))
# 12
def findprime(a=101,b=201):
    if a==1:
        a=2
    import math
    L=list(range(a,b))
    for x in range(a,b):
        x1=x
        k=int(math.sqrt(x))        
        for i in range(2,k+1):
            if x%i==0:
                L.remove(x1)
                break                
    #print(L)
    return L,len(L)
print(findprime(101,201))