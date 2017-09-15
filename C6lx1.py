#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 17:15:59 2017

@author: foolwolf0068
"""

#编程题 6.1-18
# 6.1
def getPentagonalNumber(n):
    return int(n*(3*n-1)/2)
def main(n):
    printLine=7
    for i in range(1,n+1):
        print(format(getPentagonalNumber(i),"6d"),end=" ")
        if i%printLine==0:
            print()
    print()
main(50)

#6.2
def sumDigits(n):
    if isinstance(n,int):
        str1=str(n) # 数字转化为字符
        sum=0
        for i in str1:
            sum+=int(i)
        return sum
    else:
        print("The number",n,"is not a positvie integer,Please enter a positvie integer!!!")
        return 0
def main(n):
    print("The digits sum of",n,"is",sumDigits(n))

main(2345.0)
# 6.34
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
def main(n):
    if isPalindrome(n):
        print("The number",n,"is a palindrome!")
    else:
        print("The number",n,"is not a palindrome!")
main(232232)

# 6.4
def main(n):
    print("The reverse number of",n,"is",reverse(n))
main(234)

# 6.5
def displaySortedNumbers(n1,n2,n3):
    L=[n1,n2,n3]
    for i in L:
        if i==max(L):
            n3=i
        elif i==min(L):
            n1=i
        else:
            n2=i
    return n1,n2,n3
def main():
    n1,n2,n3=31,12.4,15#eval(input("Enter three numbers:"))
    print("Enter three numbers:",n1,n2,n3)
    print("The sorted numbers:",displaySortedNumbers(n1,n2,n3))
main()

# 6.6
def displayPattern(n):
    if isinstance(n,int):        
        for i in range(1,n+1):
            #str1=" "
            print(" "*2*(n-i),end='')
            for j in range(i,0,-1):
                #str1=str(j)+str1                
                print(format(j,"d"),end=" ")
            print()
    else:
        print(n,'is not a positive integer... !')
        print("Please enter a positive integer... !")
def main(n):
    displayPattern(n)
main(9)

# 6.7
def futureInvestmentValue(investmentAmount,monthlyInterestRate,years):
    return investmentAmount*(1+monthlyInterestRate)**(years*12)

def main(years):
    amount=1000#eval(input("The amount invested:"))    
    rate1=9/1200#eval(input("Annual interest rate:"))/1200
    print("Years\t","Future Value\t")
    for i in range(1,years+1):
        a=futureInvestmentValue(amount,rate1,i)
        print(i,"\t",format(a,">8.2f"),"\t")
main(30)

# 6.13
def m(n):
    a=0
    for i in range(1,n+1):
        a+=n/(n+1)
    return a
def main(n):
    print("i\t","m(i)\t")
    for i in range(1,n+1):
        print(i,"\t",format(m(i),">.4f"))
main(20)

#6.14
def m1(n):
    a1=0
    for i in range(1,n+1):
        a1+=((-1)**(i+1))/(2*i-1)
    return a1*4
def main(n):
    print("i\t","m(i)\t")
    for i in range(1,n+1,100):
        print(i,"\t",format(m1(i),">.4f"))
main(1000)

#6.16
def numberOfDaysInAYear(year):
    if isLeapYear(year):
        return 366
    else:
        return 365
    
def isLeapYear(year):
    if year%400==0 or(year%4==0 and year%100!=0):
        return True
    else:
        return False
def main(a,b):
    if a>b:
        a,b=b,a
    print("Year\t","Days in this year\t")
    for i in range(a,b+1):
        print(i,"\t",numberOfDaysInAYear(i))
        
main(2010,2020)

#6.17
def isValid(side1,side2,side3):
    if (side1+side2>side3)and(side1+side3>side2)and(side3+side2>side1):
        return True
    else:
        return False
def area(side1,side2,side3):
    s0=(side1+side2+side3)/2.0
    area1=(s0*(s0-side1)*(s0-side2)*(s0-side3))**0.5
    return area1

def main():
    n1,n2,n3=eval(input("Enter three sides in double:"))
    if isValid(n1,n2,n3):
        print("The area of the triangle is",area(n1,n2,n3))
    else:
        print("Input is invalid!...")
main()

# 6.18
def printMatrix(n):
    from random import randint
    for i in range(n):
        for j in range(n):
            print(randint(0,1),end=" ")
        print()
def main():
    n=eval(input("Enter n:"))
    printMatrix(n)
main()       
        