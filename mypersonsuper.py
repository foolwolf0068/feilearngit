#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 10:49:04 2017

@author: foolwolf0068
"""

class Person(object):
    def __init__(self):
        self.height=160
    def about(self,name):
        print('{} is about {}'.format(name,self.height))
        
class Girl(Person):
    def __init__(self):
        super(Girl,self).__init__()
        self.beast=90
    def about(self,name):
        print('{} is a hot girl, she is about {}, and her beast is {}'.format(name,self.height,self.beast))
        super(Girl,self).about(name)

if __name__=='__main__':
    cang=Girl()
    cang.about('canglaoshi')