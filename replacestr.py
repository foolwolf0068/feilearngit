#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 14:31:21 2017

@author: foolwolf0068
"""

str1="Do you love Canglaoshi? Canglaoshi is a good teacher."
str2=str1.split(' ')
print(str2)
flag=1
for x,string in enumerate(str2):
    if 'Canglaoshi' in string:
        if flag==1:
            str2[x]='PHP?'
            flag+=1
        else:
            str2[x]='PHP'
        
print(str2)
print(' '.join(str2))
# while else
count =0
while count<5:
    print(count,'is less than 5')
    count+=1
else:
    print(count,'is not less than 5')
#for else
from math import sqrt
for n in range(99,1,-1):
    root=sqrt(n)
    if root==int(root):
        print(n)
        #continue
        #break
else:
    print('Nothing')
f=open('readme.txt')
for line in f:
    print(line.strip())
f1=open('readme.txt','a+')
f1.write('This a good file!\n')
for line in f1:
    print(line.strip())
import os
print(os.stat('readme.txt'))
f1.close()