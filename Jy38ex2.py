#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 20:21:48 2017

@author: foolwolf0068
"""

import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)
    def move(self):
        self.x -= 1
        print("My position is:",self.x,self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        #Fish.__init__(self) # 方法一 继承父类
        super().__init__()# 方法二 继承父类
        self.hungry = True
    
    def eat(self):
        if self.hungry:
            print("My dream is eating every time.")
            self.hungry = False
        else:
            print("I am full...")

class Base1:
    def foo1(self):
        print("This foo1 belongs to base1.")
        
class Base2:
    def foo2(self):
        print("This foo2 belongs to base2.")
        
class Base3(Base1,Base2):
    pass
def main():
    fish = Fish()
    fish.move()
    goldfish=Goldfish()
    goldfish.move()
    shark= Shark()
    shark.eat()
    shark.eat()



    b=Base3()
    b.foo1()
    b.foo2()
if __name__ == "__main__":
    main()
