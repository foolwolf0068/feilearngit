#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 23:35:17 2017
小甲鱼视频 67
@author: foolwolf0068
"""
from tkinter import *

root = Tk()
e = Entry(root)
e.pack(padx = 20, pady = 20)

e.delete(0, END)

e.insert(0, "默认文本...")

mainloop()
