#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 14:45:53 2017

@author: foolwolf0068
"""

class ProtectMe(object):
    def __init__(self):
        self.me='feige'
        self.__name='xiaofei' #私有属性
    def __python(self): # 私有方法
        print('I love you')
    def code(self):
        print('which languange do you like?')
        self.__python()
    #要调用私有属性的方法@property
    @property
    def name(self):
        return self.__name
    
    
if __name__ == "__main__":
    p = ProtectMe()
    print(p.me)
    #print(p.__name) #私有属性调用不可用(除非类中用了property函数)
    print(p.name)
    p.code()
    #p.__python() #私有方法调用不可用
class A(object):
    def __getattr__(self,name):
        print('You are using getattr')
    def __setattr(self,name,value):
        print('You are using setattr')
        self.__dict__[name]=value
                     
a=A()
a.x=4