#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:41:27 2017

小甲鱼视频 69
@author: foolwolf0068
Text 组件 强大 灵活
"""

from tkinter import *

root = Tk()

text1 = Text(root, width = 30, height = 2)
text1.pack()

text1.insert(INSERT,"I love \n")
text1.insert(END,"Feige...")

def show():
    print("哎呀，我被点了。。。")
b1 = Button(text1, text = "按钮", command = show)
text1.window_create(INSERT,  window = b1)

mainloop()