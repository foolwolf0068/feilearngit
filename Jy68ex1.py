#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 00:06:01 2017
小甲鱼视频 68
@author: foolwolf0068
"""

from tkinter import *

master = Tk()

theLB = Listbox(master, selectmode = EXTENDED) # selectmode = SINGLE,
theLB.pack()

theLB.insert(0,"feige")
theLB.insert(END,"feige23")

for item in "feige":
    theLB.insert(END,item)
    
theButton = Button(master, text = "Delete",\
                   command = lambda x=theLB:x.delete(ACTIVE))
theButton.pack()

mainloop()
