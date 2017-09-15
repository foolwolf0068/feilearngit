# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 14:34:40 2017
求最大公约数和最小公倍数的程序
@author: Administrator
"""

def gcd(a,b):
    if a>=b:
        m,n=a,b
    else:
        m,n=b,a
    
    while True:
        r=m%n
        if r==0:
            return n
        m=n
        n=r     

def lcm(a,b):
    return (a*b)/gcd(a,b)

def main():
    a=25
    b=18
    print(gcd(a,b),lcm(a,b))
main()
    

class new_int(int):
    def __add__(self,other):
        print("now call __add__ method")
        return int.__sub__(self,other)
    def __sub__(self,other):
        print("now call __sub__ method")
        return int.__add__(self,other)

char1 = "1"
char2 = "3"
    
    