#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 16:35:56 2017

@author: foolwolf0068
"""
# Chapter 5 practice
# 5.1
numofneg=0
numofpos=0
numoftotal=0
sum0=0
while True:
    number=eval(input("Enter an interger, the input ends if it is 0:"))
    numoftotal+=1
    sum0+=number
    if number>0:
        numofpos+=1
    elif number<0:
        numofneg+=1
    else:
        break
if sum0!=0 and numoftotal!=1:
    print("The number of positives is",numofpos)
    print("The number of negatives is",numofneg)
    print("The total is",numoftotal)
    print("The average is",sum0/numoftotal)
else:
    print("You didn\'t enter any number")

# 5.3
print(format(" 公斤","4s"),format(" 磅","6s"))
for i in range(1,200,2):
    print(format(i,"4d"),format(2.2*i,"6.2f"))
   
# 5.4
print(format(" 英里","4s"),format(" 公里","6s"))
for i in range(1,11):
    print(format(i,"4d"),format(1.609*i,"6.3f"))    

# 5.7
import math
print(format(" 英里","4s"),format(" Sin","6s"),format(" Cos","6s"))
for i in range(0,361,10):
    print(format(i,"4d"),format(math.sin(i/180*math.pi),"6.4f"),format(math.cos(i/180*math.pi),"6.4f"))

# 5.8
print(format("Number","5s"),format("Square Root","6s"))
for i in range(0,21,2):
    print(format(i,"5d"),format(math.sqrt(i),"6.4f"))      

# 5.9
sum1=0
fe1=10000
for i in range(1,11):
    fe1*=1.05
    sum1+=fe1
print("After 10 years, the fee will be",fe1)
print("The total fee is",sum1)

# 5.12&13
count=0
for i in range(100,1001):
    if (i%5==0 or i%6==0):
        print(i,end=' ')
        count+=1
        if count==10:
            count=0
            print()
print()
print("Divided by 5 or 6 but not 30")
count=0
for i in range(100,1001):
    if (i%5==0 or i%6==0)and(i%30!=0):
        print(i,end=' ')
        count+=1
        if count==10:
            count=0
            print()
print("5.13 end")  
      
# 5.14
n=1
while True:
    if n*n>12000:
        print("The smallest root number is",n)
        break
    n+=1
                
# 5.15
n=100
while True:
    if n*n*n<12000:
        print("The largest root number is",n)
        break
    n-=1

