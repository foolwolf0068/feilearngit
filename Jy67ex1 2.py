# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 19:27:24 2017
小甲鱼视频 67
@author: Administrator
"""

from tkinter import *

root = Tk()

e = Entry(root)
e.pack(padx = 20, pady = 20)

e.delete(0, END)
e.insert(0,"默认文本...")
mainloop()