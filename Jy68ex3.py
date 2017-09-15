#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:03:38 2017
小甲鱼视频68
@author: foolwolf0068
滚动条组件
"""

from tkinter import *

root = Tk()

sb = Scrollbar(root)
sb.pack(side = RIGHT, fill = Y)

lb = Listbox(root, yscrollcommand = sb.set)
for i in range (1000):
    lb.insert(END, i)
lb.pack(side = LEFT, fill = BOTH)

sb.config(command = lb.yview)



mainloop()