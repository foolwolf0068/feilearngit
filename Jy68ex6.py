#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:24:17 2017
小甲鱼视频 68
@author: foolwolf0068
"""

from tkinter import *

root = Tk()

s1 = Scale(root, from_ = 0, to = 42, \
           tickinterval = 5, resolution = 5, length = 200)
s1.pack(side = RIGHT,fill = Y)

s2 = Scale(root, from_ = 0, to = 200, \
           tickinterval = 50,resolution = 2, length = 600, \
           orient = HORIZONTAL)
s2.pack(side = BOTTOM, fill = X)

def show():
    print(s1.get(), s2.get())
    
b1 = Button(root, text = "Get Positon", command = show)
b1.pack(side = LEFT)

b2 = Button(root, text = "Quit", command = root.quit)
b2.pack(side = RIGHT)

mainloop()