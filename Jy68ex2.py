#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 14:57:41 2017
小甲鱼视频 68
@author: foolwolf0068
添加height
"""

from tkinter import *

master = Tk()

theLB = Listbox(master, selectmode = EXTENDED, height = 9) # selectmode = SINGLE,
theLB.pack()

for item in range(11):
    theLB.insert(END,item)


mainloop()