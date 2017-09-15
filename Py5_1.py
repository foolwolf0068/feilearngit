#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 15:18:07 2017

@author: foolwolf0068
"""

for i in range(10):
    print("feige")
print(i)

for i in range(1,5):
    j=0
    while j<i:
        print(j,end="")
        j+=1
        
i=0
while i<5:
    for j in range(i,1,-1):
        print(j,end="")
    print("****")
    i+=1
    
i=5
while i>=1:
    num=1
    for j in range(1,i+1):
        print(num,end="xxx")
        num*=2
    print()
    i-=1
i=1
while i<=5:
    num=1
    for j in range(1,i+1):
        print(num,end="G")
        num+=2
    print()
    i+=1
    
# 5-10
import random
numoftr=int(1e6)
numofh=0
for i in range(numoftr):
    x=random.random()*2-1
    y=random.random()*2-1
    if x*x+y*y<=1:
        numofh+=1
pi=4*numofh/numoftr
print("PI is",pi)

# 5-13
Num_of_primes=100
Num_of_primes_perline=10
count=0
number=2
print("The first 50 prime numbers are")
while count<Num_of_primes:
    isPrime=True
    
    divisor=2
    while divisor<=number/2:
        if number % divisor==0:
            isPrime=False
            break
        divisor+=1
    
    if isPrime:
        count+=1
        print(format(number,"5d"),end="")
        if count%Num_of_primes_perline==0:
            print()
    number+=1