# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 17:44:24 2017
小甲鱼视频 65
@author: Administrator
"""

from tkinter import *

root = Tk()

photo = PhotoImage(file = "bg.gif")
theLabel = Label(root,
                 text = "FeiGe study \n Python",
                 justify = LEFT,
                 image = photo,
                 compound = CENTER,
                 font = ("宋体", 20),
                 fg = "white")

theLabel.pack()

mainloop()