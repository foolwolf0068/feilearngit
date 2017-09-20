#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 16:41:37 2017
小甲鱼视频 generator
@author: foolwolf0068
"""
def myGen():
    print("Generator is called....")
    yield 1
    yield 2

def Fibs_yield():
    a = 0
    b = 1
    while True:
        a, b = b, a+b
        yield a

def main():    
    for i in myGen():
        print(i)
    #
    for each in Fibs_yield():
        if each > 1000:
            break
        print(each, end = " ")
    print()
    # list tudaoshi
    a = [i for i in range(100) if not(i%2) and i%3]
    print(a)
    # dict tuidaoshi
    b = {i:i%2 ==0 for i in range(10)}
    print(b)
    # generator tuidaoshi
    c = (i for i in range(10))
    for i in c:
        print(next(c))

    d = sum(i for i in range(100) if i %2)
    print(d)

    e = sum((i for i in range(100) if i %2))
    print(e)
    
if __name__ == "__main__":
    main()
