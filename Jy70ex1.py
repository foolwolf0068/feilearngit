#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 17:12:28 2017
小甲鱼视频 70
@author: foolwolf0068
"""
from tkinter import *

root = Tk()

text1 = Text(root, width = 30, height = 5)
text1.pack()

text1.insert(INSERT, "I love Feige.com!")

text1.tag_add("tag1", "1.7","1.12","1.14")
text1.tag_add("tag2", "1.7","1.12","1.14")
text1.tag_config("tag1", background = "yellow", foreground = "red")
text1.tag_config("tag2", foreground = "blue")

mainloop()
