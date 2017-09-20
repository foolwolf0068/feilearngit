#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 16:41:37 2017
小甲鱼视频
@author: foolwolf0068
"""
class Fibs:
    def __init__(self, n = 20):
        self.a = 0
        self.b = 1
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a+self.b
        if self.a > self.n:
            raise StopIteration
        return self.a
    


def main():    
    for i in "Feige":
        print(i)

    links = {1:'feige',\
             2:'qiaoer',\
             3:'chao'}
    for each in links:
        print("%s --> %s"%(each,links[each]))
    fibs = Fibs(100)
    '''for each in fibs:
        if each < 20:
            print(each)
        else:
            break'''

    for each in fibs:
        
        print(each)
        

    


if __name__ == "__main__":
    main()
