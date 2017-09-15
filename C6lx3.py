#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 12:37:14 2017

@author: foolwolf0068
"""

# 编程题 6.29-28
# 6.29
def isValid(number):
    a=sumOfDoubleEvenPlace(number)+sumOfOddPlace(number)
    #print(sumOfDoubleEvenPlace(number),sumOfOddPlace(number),a)
    alog1=(prefixMatched(number,4))or(prefixMatched(number,5))
    alog2=(prefixMatched(number,6))or(prefixMatched(number,37))
    if (13<=getSize(number)<=16)and(a%10==0):
        if alog1 or alog2:
            return True
        else:
            return False
    else:
        return False
        
def sumOfDoubleEvenPlace(number):
    str1=str(number)
    sum0=0
    for i in str1[::2]:
        sum0+=getDigit(int(i)*2)
    return sum0
# print(sumOfDoubleEvenPlace(4388576018402626)) 
def getDigit(number):# return sum of the digits
    str1=str(number)    
    while True:
        a=len(str1)
        sum0=0
        for i in range(a):
            sum0+=int(str1[i])
        if sum0//10==0:
            break
        else:
            str1=str(sum0)
    return sum0
# print(getDigit(66))        
def sumOfOddPlace(number): 
    str1=str(number)
    sum1=0
    for i in str1[1::2]:
        sum1+=int(i)
    return sum1
# print(sumOfOddPlace(4388576018402626))
def prefixMatched(number,d): # return True if the digit d is a prefix for number
    #str1=str(number)
    str2=str(d)
    num=len(str2)    
    if getPrefix(number,num)==d:#(str1[:num]==str2):
        return True
    else:
        return False
#print(prefixMatched(4388,431))     
def getSize(d):# return the number of digits in d
    str1=str(d)
    return len(str1)
#print(getSize(12342))
def getPrefix(number,k):#
    str1=str(number)
    num=int(str1[0:k])
    return num
#print(getPrefix(346578,4))

def main(number):
    #number=eval(input("Please enter a number:"))
    if isValid(number):
        if (prefixMatched(number,4)):
            print("This Visa Credit number",number,"is valid!")
        elif (prefixMatched(number,5)):
            print("This Master Credit number",number,"is valid!")
        elif (prefixMatched(number,6)):
            print("This Discover Credit number",number,"is valid!")
        else:
            print("This American Express Credit number",number,"is valid!")
    else:
        print("This Credit number",number,"is not valid!")

main(4388576018407075)

# 6-35
def aOfGailv(n=100):
    from random import randint
    count=0
    for i in range(n):
        chr1=chr(randint(ord("A"),ord("Z")))
        if chr1=="A":
            count+=1
        """print(chr1,end="")
        if (i+1)%10==0:
            print()"""
    return count,(count/n)*100
times,rate1=aOfGailv(n=10000)
print("The upper case letter \"A\" happens",times,"times,and the rate is",rate1,"% .")

# 6-36
def aOfRandom(n,n1=10):
    from random import randint
    count=0
    for i in range(n):
        chr1=chr(randint(ord("A"),ord("Z")))
        if chr1=="A":
            count+=1
        print(chr1,end="")
        if (i+1)%n1==0:
            print()
aOfRandom(100,n1=10)