#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 17:40:21 2017

@author: foolwolf0068
"""

# 6-17 检查点
def f(x,y=1,z=3):
    return x+y+z
print(f(1,2,3))
print(f(y=1,x=2,z=3))
print(f(1,z=4))

# 6-10
def sort(num1,num2):
    if num1>num2:
        return num1,num2
    else:
        return num2,num1
n1,n2=sort(3,5)
print("n1 is",n1)
print("n2 is",n2)

import random
print(random.randint(0,1))

# 6-12
import RandomCharacter
Numofchars=175
charperline=25
for i in range(Numofchars):
    print(RandomCharacter.getRandomUpperCaseLetter(),end="")
    if (i+1)%charperline==0:
        print()
import random
# 6.24
print(random.randint(34,55))   
# 6.25   
print(chr(random.randint(ord("B"),ord("M"))))
# 6.26
#from random import random
print(random.random()*50+6.5)
# 6.27
print(chr(random.randint(ord("a"),ord("z"))))

def getMonthName(month):
    monthvalue=["January","February","March","April","May","June",
                "July","August","September","October","November","December"]
    for i,value in enumerate(monthvalue,start=1):
        if i==month:
            return value
for i in range(1,13):
    print(getMonthName(i))
    
i=2
if i in [1,3,5,7,8,10,12]:
    x=31
elif i in [4,6,9,11]:
    x=30
else:
    x=0
print(x)