#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:36:18 2017
小甲鱼视频 69
@author: foolwolf0068
Text 组件 强大 灵活
"""

from tkinter import *

root = Tk()

text = Text(root, width = 30, height = 2)
text.pack()

text.insert(INSERT,"I love \n")
text.insert(END,"Feige...")
mainloop()
