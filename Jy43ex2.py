#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 18:02:56 2017
小甲鱼视频
@author: foolwolf0068
"""

class Nint(int):
    def __radd__(self,other):
        return int.__sub__(other,self)
    
    def __rsub__(self,other):
        return int.__sub__(other,self)

def main():    
    a = Nint("5")
    print(a)
    b = Nint(3)
    
    print(b)
    # radd
    print(1+b)

    print(a+b)
    # rsub
    print(3 - a)

    

if __name__ == "__main__":
    main()
