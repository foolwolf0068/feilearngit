#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 22:36:02 2017
小甲鱼视频 67
@author: foolwolf0068
"""

from tkinter import *


master = Tk()

def test():
    if e1.get() == "foolwolf":
        print("Correct!")
        return True
    else:
        print("False!!!")
        e1.delete(0, END)
        return False

def test2():
    if e2.get() != "a123":
        print('test2 False')
        return False
    else:
        print("test2 True")
        return True
def test3():
    print("test3被调用了...")
    e1.delete(0, END)
    return True

def test4(content, reason, name):
    if content == "feige":
        print("test4 correct!")
        print(content, reason, name)
        return True
    else:
        print("test4 False...")
        print(content, reason, name)
        return False
    

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
e1 = Entry(master, textvariable= v1, validate = "focusout", \
           validatecommand = test, invalidcommand = test3)
e2 = Entry(master, textvariable= v2, validate = "focusout", \
           show = "*", validatecommand = test2)

testCMD = master.register(test4)
e3 = Entry(master, textvariable= v3, validate = "focusout", \
           validatecommand = (testCMD, '%P', '%v', '%W'))
e1.pack(padx = 10, pady = 10)
e2.pack(padx = 10, pady = 10)
e3.pack(padx = 10, pady = 10)




mainloop()