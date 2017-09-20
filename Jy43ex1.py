#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 18:02:56 2017
小甲鱼视频
@author: foolwolf0068
"""

class int(int):
    def __add__(self,other):
        return int.__sub__(self,other)
    '''def __sub__(self,other):
        return int.__add__(self,other)'''

def main():    
    a = int("5")
    print(a)
    b = int(3)
    print(b)

    print(a+b)

if __name__ == "__main__":
    main()
