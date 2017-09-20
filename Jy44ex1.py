#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 18:12:17 2017
小甲鱼视频44
@author: foolwolf0068
"""

class A():
    def __str__(self):
        return "Feige is handsome!"


class B():
    def __repr__(self):
        return "Feige is pretty..."

def main():
    a = A()
    print(a)        
    b = B()
    print(b)


if __name__ == "__main__":
    main()
