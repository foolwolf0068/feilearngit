#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 16:55:09 2017
小甲鱼视频
@author: foolwolf0068
"""
class C:
    def __init__(self):
        print("this is __init__")
        
    def __del__(self):
        print("this is __del__")

def main():
    c1 = C()
    c2 = c1
    c3 = c2
    del c3
    del c2
    del c1

if __name__ == "__main__":
    main()

    



        
