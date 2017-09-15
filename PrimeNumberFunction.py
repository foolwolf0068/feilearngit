#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 16:34:09 2017

@author: foolwolf0068
Chapter 6 
example 6-7
"""

def isPrime(number):
    divisor=2
    while divisor <= number/2:
        if number % divisor ==0:
            return False
        divisor+=1
    return True
def printPrimeNembers(numberOfPrimes):
    Num_of_Primes=50
    Num_of_Prime_per_line=10
    count=0
    number=2
    while count<numberOfPrimes:
        if isPrime(number):
            count+=1
            print(number,end=" ")
            if count%Num_of_Prime_per_line==0:
                print()
        number+=1
def main():
    print("the first 50 prime numbers are")
    print(printPrimeNembers(50))

main()