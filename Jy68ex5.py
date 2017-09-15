#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:18:56 2017
小甲鱼视频68
@author: foolwolf0068
"""

from tkinter import *

root = Tk()

s1 = Scale(root, from_ = 0, to = 42)
s1.pack()

s2 = Scale(root, from_ = 0, to = 200, orient = HORIZONTAL)
s2.pack()

def show():
    print(s1.get(), s2.get())
    
b1 = Button(root, text = "Get Positon", command = show)
b1.pack(side = LEFT)

b2 = Button(root, text = "Quit", command = root.quit)
b2.pack(side = RIGHT)

mainloop()