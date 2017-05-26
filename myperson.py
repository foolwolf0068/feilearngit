#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 09:05:49 2017

@author: foolwolf0068
"""

class person(object): #创建类
    def __init__(self,name):#析构函数
        self.name=name
    def getName(self):#类的方法1
        return self.name
    def breast(self,n):#类的方法2
        self.breast=n
    def color(self,color):#类的方法3
        print('%s is %s.'%(self.name,color))
    def how(self):#类的方法4
        print('%s\'s breast is %s.'%(self.name,self.breast))
girl=person('canglaoshi')#实例化类
girl.breast(90)#调用类的方法
girl.color('white')
girl.how()
#命名空间测试
def foo(num,str):
    name='feige'
    print(locals())
foo(30,'feige.com')
#作用域测试
def outer_foo():
    a=10
    def inner_foo():
        #global a
        a=30
        print('inner_foo,a=',a)
    inner_foo()
    print('out_foo,a=',a)
a=20
outer_foo()
print('a=',a)
