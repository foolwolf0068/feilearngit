#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 20:49:06 2017

@author: foolwolf0068
"""

# 8.11
def decimalToBinary(decimalValue):
    bin=""
    while decimalValue !=0:
        binValue=decimalValue%2
        bin=toHexChar(binValue)+bin
        decimalValue=decimalValue//2
    return bin

def toBinChar(binValue):
    return chr(binValue+ord("0"))

def main():
    decimalValue=eval(input("Enter a decimal number: "))
    print("The hex number for decimal",decimalValue,"is",decimalToBinary(decimalValue))
    
main()