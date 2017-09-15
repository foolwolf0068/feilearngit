#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 13:14:34 2017

@author: foolwolf0068
"""

import math
class Circle(object):
    def __init__(self,radius=1):
        self.radius=radius
    def gePerimeter(self):
        return 2*self.radius*math.pi
    def getArea(self):
        return self.radius*self.radius*math.pi
    def setRadius(self,radius):
        self.radius=radius

        