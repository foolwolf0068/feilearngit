#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 15:49:14 2017

@author: foolwolf0068
"""
import math
radius=eval(input('Enter a value:'))
area=math.pi*radius**2
print("The area for the circle of radius",radius, "is",area)

#2.1
width=5.5
height=2
print("The area is:",width*height)

#2.2
miles=100
kilometers=miles*1.609
print("The kilometers is:",kilometers)

#2-4
num1,num2,num3=eval(input("Enter three numbers separated by commas: "))
aver1=(num1+num2+num3)/3.0
print("The average of",num1,num2,num3,"is:" ,aver1)
