#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 15:39:37 2017

@author: foolwolf0068
"""

f=open('readme.txt')
content=f.read()
print(content)
f.close()
from random import randint
#print(randint(1,100))
L=[]
for i in range(40):
    L.append(randint(0,100))
print(L)
av1=sum(L)/40
print(av1)
L1=[]
count=0
for i in range(40):
    if L[i]<av1:
        L1.append(L[i])
        count+=1
print(L1,count)       
L.sort(reverse=True)
print('-'*30)
print(L)