# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 19:24:36 2017

@author: Administrator
"""

num=1
while True:
    if num%2==1 and num%3==2 and num%5==4 and num%6==5 and num%7==0:
        break
    else:
        num+=2
print(num)

def isPrime(n):
    if n <=1:
        return False
    if n == 2:
        return True
    j=2
    while (j*j<=n):
        if n % j ==0:
            return False
        j += 1
    return True

def main(n):
    for i in range(1,n+1):
        if isPrime(i):
            print(i,end=" ")
    print()

main(100)


def main1(n):
    if n<6:
        print("you must enter a number (n>= 6):")
    for i in range(6,n+1,2):
        flag = 1
        for j in range(2,(int(i/2)+1)):
            if (j % 2 ==0) or ((i-j) % 2==0):
                continue
            if isPrime(j) and isPrime(i-j):
                print(i,"=",j,"+",i-j)
                flag=0
                break
        if flag==1:
            print("The even number is not good!")

main1(10000)
        