# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 18:09:29 2017
小甲鱼视频 66

@author: Administrator
"""

from tkinter import *

root = Tk()

v = IntVar()

c = Checkbutton(root, text = "测试一下", variable = v)
c.pack()

l = Label(root, textvariable = v)
l.pack()

mainloop()
