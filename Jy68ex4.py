#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:14:46 2017
小甲鱼视频 68 
@author: foolwolf0068
Scale 组件 滑块
"""

from tkinter import *

root = Tk()

Scale(root, from_ = 0, to = 42).pack()
Scale(root, from_ = 0, to = 200, orient = HORIZONTAL).pack()

mainloop()