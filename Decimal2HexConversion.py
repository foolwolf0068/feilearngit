#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 16:59:03 2017

@author: foolwolf0068
Chapter 6
example 6-8
十进制转换成为十六进制
"""
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

def main():
    decimalValue=eval(input("Enter a decimal number: "))
    print("The hex number for decimal",decimalValue,"is",decimalToHex(decimalValue))
    
main()