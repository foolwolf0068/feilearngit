#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 16:55:09 2017
小甲鱼视频
@author: foolwolf0068
"""

class Capstr(str):
    def __new__(cls,string):
        string = string.upper()
        return str.__new__(cls,string)
    



def main():
    a = Capstr("I love feige.com")
    print(a)

if __name__ == "__main__":
    main()
