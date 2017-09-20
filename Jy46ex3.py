#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 16:13:48 2017
小甲鱼视频
@author: foolwolf0068
"""


class Celsius:
    def __init__(self, value = 26.0):
        self.value = float(value)
        
    def __get__(self, instance, owner):
        return self.value
    
    def __set__(self, instance, value):
        self.value = float(value)
        
    def __delete__(self, instance):
        self.fdel(self, instance)

        
class Fahrenheit:

    def __get__(self, instance, owner):
        return instance.cel * 1.8 +32
    
    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) / 1.8

    
class Temperature:
    cel = Celsius()
    fah = Fahrenheit()


def main():
    temp = Temperature()
    print(temp.cel)
    temp.cel = 30
    print(temp.cel, temp.fah)

    temp.fah = 100
    print(temp.fah, temp.cel)
    
    
    
    
    
  
        

if __name__ == "__main__":
    main()
