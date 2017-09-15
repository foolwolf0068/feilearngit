#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:45:34 2017

小甲鱼视频 69
@author: foolwolf0068
Text 组件 强大 灵活
"""

from tkinter import *

root = Tk()

text1 = Text(root, width = 30, height = 20)
text1.pack()

photo = PhotoImage(file='/Users/foolwolf0068/feilearngit/meinv.gif')

def show():
    text1.image_create(END, image = photo)
    
b1 = Button(text1, text = "按钮", command = show)
text1.window_create(INSERT,  window = b1)

mainloop()
