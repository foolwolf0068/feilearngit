#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 10:12:08 2017

@author: foolwolf0068
"""

class person(object):
    def speak(self):
        print('I love you very much!')
    def setHeight(self):
        print('The height is 1.7m.')
    def breast(self,n):
        print('My breast is:',n)
    def eye(self):
        print('Two eyes')

class girl(person):
    age=28
    def color(self):
        print('The girl is white.')
    def setHeight(self):
        print('The height is 1.67m.')
# 继承测试

if __name__=='__main__':
    cang=girl()
    cang.setHeight()
    cang.speak()
    cang.breast(90)
   
class Hotgirl(girl):
    pass

if __name__=='__main__':
    kong=Hotgirl()
    kong.eye()
    kong.breast(98)
    kong.color()
    print(kong.age)

#多重继承
class k1(object):
    def foo(self):
        print('k1-foo')
        
class k2(object):
    def foo(self):
        print('k2-foo')
    def bar(self):
        print('k2-bar')
class j1(k1,k2):
    pass

class j2(k1,k2):
    def bar(self):
        print('j2-bar')
class c(j1,j2):
    pass

if __name__=='__main__':
    print(c.__mro__)
    m=c()
    m.foo()
    m.bar()
        
    