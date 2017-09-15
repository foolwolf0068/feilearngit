#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 22:30:46 2017
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

v1 = StringVar()
v2 = StringVar()
e1 = Entry(master, textvariable= v1, validate = "focusout", \
           validatecommand = test, invalidcommand = test3)
e2 = Entry(master, textvariable= v2, validate = "focusout", \
           show = "*", validatecommand = test2)
e1.pack(padx = 10, pady = 10)
e2.pack(padx = 10, pady = 10)

mainloop()