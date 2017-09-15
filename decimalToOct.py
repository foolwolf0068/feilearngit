#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 17:13:55 2017

@author: foolwolf0068
Chapter 6
十进制转换成为八进制
十进制转换为二进制
"""
# 转换为八进制
def decimalToOct(decimalValue):
    oct=""
    while decimalValue !=0:
        octValue=decimalValue%8
        oct=toOctChar(octValue)+oct
        decimalValue=decimalValue//8
    return oct

# 转换二进制
def decimalToBin(decimalValue):
    bin=""
    while decimalValue !=0:
        binValue=decimalValue%2
        bin=toOctChar(binValue)+bin
        decimalValue=decimalValue//2
    return bin

def toOctChar(hexValue):
    return chr(hexValue+ord("0"))

def main():
    decimalValue=eval(input("Enter a decimal number: "))
    print("The oct number for decimal",decimalValue,"is",decimalToOct(decimalValue))
    print("The bin number for decimal",decimalValue,"is",decimalToBin(decimalValue))

main()

# 6-17 检查点
def f(x,y=1,z=3):
    return x+y+z
print(f(1,2,3))
print(f(y=1,x=2,z=3))
print(f(1,z=4))