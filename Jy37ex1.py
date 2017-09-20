#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 20:05:13 2017

@author: foolwolf0068
"""

class Ball:
    def __init__(self,name):
        self.name = name
    def kick(self):
        print("my name is",self.name,",god,you kid me?")
        
class person:
    name = "feige"
    
def main():
    b= Ball('toudu')
    b.kick()
    c= Ball('fanqie')
    c.kick()
    
    d=person()
    print(d.name)

if __name__ == "__main__":
    main()
        
