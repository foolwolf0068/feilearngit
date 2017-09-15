#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 01:01:25 2017

@author: foolwolf0068
"""

def carry(bit,pos):
    carrary=0
    for i in range(pos+1):        
        bit[i] += carrary
        if bit[i] <= 9:
            carrary = 0
        elif bit[i] > 9 and i<pos:
            carrary = bit[i] // 10
            bit[i] %= 10
        elif bit[i] > 9 and i>=pos:
            while bit[i]>9:
                carrary = bit[i] // 10
                bit[i] %= 10
                i += 1
                bit[i]=carrary
    return bit

from math import log10        
def NewFact(num):
    sum=0
    for i in range(1,num+1):
        sum += log10(i)
    digit = int(sum)+1
    fact = (digit+1)*[0]
    fact[0] = 1 # 个位为1
    for i in range(2,num+1):
        for j in range(digit,-1,-1):
            if (fact[j] != 0):
                pos = j
                break
        for j in range(pos+1):
            fact[j] *= i
        fact = carry(fact,pos)
    for j in range(digit,-1,-1):
        if (fact[j] != 0):
            pos = j
            break
    
    # print(fact[0:pos+1])
    for i in range(pos,-1,-1):
        print(fact[i],end="")

def fact1(n):
    if n<=1 and n>=0:
        return 1
    else:
        return n*fact1(n-1)
def main():
    NewFact(500)
    print()
    print(fact1(500))

main()
    
    
           