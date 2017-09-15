#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 20:11:01 2017

@author: foolwolf0068
"""
# 8.8
def binaryToDecimal(binaryString):
    num=len(binaryString)
    num1=0
    for i in range(num):
        num1+=int(binaryString[i])*(2**(num-1-i))
    return num1

def main():
    s=input("Enter a binary string:")
    a=binaryToDecimal(s)
    print("Binary string",s,"converts to decimal number",a)
    
main()

# 8.9

def decimalToHex(decimalValue):
    hex=""
    while decimalValue !=0:
        hexValue=decimalValue%16
        hex=toHexChar(hexValue)+hex
        decimalValue=decimalValue//16
    return hex

def toHexChar(hexValue):
    if 0<=hexValue<=9:
        return chr(hexValue+ord("0"))
    else:
        return chr(hexValue -10+ord("A"))

def binaryToHex(binaryString):
    dec1=binaryToDecimal(binaryString)
    return decimalToHex(dec1)

def main1():
    s1=input("Enter a binary string:")
    a1=binaryToHex(s1)
    print("Binary string",s1,"converts to hex number",a1)
main1() 