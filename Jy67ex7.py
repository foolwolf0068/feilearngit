#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 23:36:02 2017
小甲鱼视频 67
@author: foolwolf0068
"""

from tkinter import *

master = Tk()
frame = Frame(master)
frame.pack(padx = 10, pady = 10)

def test4(content):
    return content.isdigit()
        
    

v1 = StringVar()    
v2 = StringVar()
v3 = StringVar()

testCMD = master.register(test4)

e1 = Entry(frame, textvariable= v1, validate = "key", \
           validatecommand = (testCMD, '%P')).grid(row = 0, column = 0)

Label(frame, text = "+").grid(row = 0, column = 2)

e2 = Entry(frame, textvariable= v2, validate = "key", \
           validatecommand = (testCMD, '%P')).grid(row = 0, column = 3)

Label(frame, text = "=").grid(row = 0, column = 4)

e3 = Entry(frame, textvariable = v3, state = "readonly").grid(row = 0, column = 5)

def calc():
    result =  int(v1.get()) + int(v2.get())
    v3.set(result)
    
Button(frame, text = "计算", command = calc).grid(row = 1, column = 2)

Button(frame, text = "退出", command = frame.quit).grid(row = 1, column = 3)
#e1.pack(padx = 10, pady = 10)
#e2.pack(padx = 10, pady = 10)
#e3.pack(padx = 10, pady = 10)



mainloop()