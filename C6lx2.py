#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 07:20:40 2017

@author: foolwolf0068
"""
#编程题 6.20-28
# 6.20
def distance(x1,y1,x2,y2):
    d=((x1-x2)**2+(y1-y2)**2)**0.5
    return d
def main():
    x1,y1=1,1#eval(input("Enter the first point:"))
    x2,y2=5,4#eval(input("Enter the second point:"))
    print("The distance between the 1st point (",x1,",",y1,") and the 2nd point(", 
          x2,",",y2,") is",distance(x1,y1,x2,y2))
main()

#6.21
def sqrt(n):
    if n <0:
        print("n must be a positive number...")
        return 0
    n0=1
    while True:
        n1=(n0+(n/n0))/2
        if abs(n1-n0)<1e-4:
            return n1
        n0=n1
print(sqrt(3))
# 6.24
def isPrime(n):
    if n <0:
        print("n must be a positive number...")
        return 0
    if n==1:
        return False
    if n==2:
        return True
    n0=2
    while n0<=n/2+1:
        if n%n0==0:
            return False
        else:
            n0+=1
    return True
"""
def main():
    for i in range(1,101):
        if isPrime(i):
            print(i)
main()
"""

def isPalindrome(number):
    return True if reverse(number)==number else False

def reverse(number):
    if isinstance(number,int):
        str2=str(number)
        strnew=""
        for i in str2:
            strnew=i+strnew
        return int(strnew)
    else:
        print("目前只能计算正整数")
        return 0
def main(count):
    count0=0
    n=1
    while count0<count:
        if isPrime(n) and isPalindrome(n):
            count0+=1
            print(n,end=" ")
            if count0%10==0:
                print()        
        n+=1
    print()
main(30)

# 6.25
def isReversePrime(number):
    a=reverse(number)
    if (isPrime(number)) and (isPrime(a)) and (number!=a):
        return True
    else:
        return False
    
def main(count):
    count0=0
    n=1
    while count0<count:
        if isReversePrime(n):
            count0+=1
            print(n,end=" ")
            if count0%10==0:
                print()
        n+=1
    print()
main(50)

# 6.26
def MeiPrime(n):
    print("p\t","2^p-1")
    for i in range(1,n+1):
        a=2**i-1
        if isPrime(a):
            print(i,"\t",a)
MeiPrime(19)
    
# 6.27
def main(count):
    count0=0
    n=1
    while count0<count:
        if isPrime(n) and isPrime(n+2):
            count0+=1
            print("(",n,",",n+2,")")
            '''if count0%5==0:
                print()'''
            n+=2
        else:
            n+=1
            
main(10)

# 6.28
def main():
    from random import randint
    sum0=1
    while True:
        a=randint(1,6)
        b=randint(1,6)
        sum=a+b 
        
        print("You rolled",a,"+",b,"=",sum)
        if sum in [7,11]:        
            print("You win")
            break
        elif sum in [2,3,12]:
        #print("You rolled",a,"+",b,"=",sum)
            print("You lose")
            break
        elif sum in [4,5,6,8,9,10]:
            print("Point is",sum)
            if sum0==sum and sum0!=7:
               print("You win")
               break
            elif sum0==7:
               print("You lose")
               break
            sum0=sum
main()
            
    
        
        