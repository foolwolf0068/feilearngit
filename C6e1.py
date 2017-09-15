#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 15:42:07 2017

@author: foolwolf0068
"""

def sum(i1,i2):
    result=0
    for i in range(i1,i2+1):
        result+=i
    return result

def main():
    print("Sum from 1 to 10 is",sum(1,10))
    print("Sum from 20 to 37 is",sum(20,37))
    print("Sum from 35 to 49 is",sum(35,49))
    
main()

# example 6-1
def max(num1,num2):
    if num1>num2:
        result =num1
    else:
        result=num2
    return result

def main():
    i=5
    j=2
    k=max(i,j)
    print("The larger number of",i,"and",j,"is",k)
main()

#example 6-2 无返回值
def printGrade(score):
    if score >=90:
        print("A")
    elif score >=80:
        print("B")
    elif score >=70:
        print("C")
    elif score >=60:
        print("D")
    else:
        print("F")

def main():
    score=eval(input("Enter a score:"))
    print("The grade is ",end="")
    printGrade(score)
main()

#example 6-2 有返回值
def getGrade(score):
    if score >=90:
        return "A"
    elif score >=80:
        return "B"
    elif score >=70:
        return "C"
    elif score >=60:
        return "D"
    else:
        return "F"

def main():
    score=eval(input("Enter a score:"))
    print("The grade is",getGrade(score),end="")
    
main()

# example 6-4
def main():
    x=1
    print("Before the call, x is",x)
    increment(x)
    print("After the call, x is",x)
def increment(n):
    n+=1
    print("\tn inside the function is",n)
main()

# example 6-6
from GCDFunction import gcd
n1=eval(input("Enter the first integer: "))
n2=eval(input("Enter the second integer: "))
print("The greatest common divisor for",n1,"and",n2,"is",gcd(n1,n2))