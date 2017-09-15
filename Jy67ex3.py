#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 17:21:45 2017
小甲鱼视频 67
密码显示为 ****
@author: foolwolf0068
"""

from tkinter import *

root = Tk()
Label(root, text = "用户名：").grid(row = 0, column = 0)
Label(root, text = "密码：").grid(row = 1, column = 0)

v1 = StringVar()
v2 = StringVar()

e1 = Entry(root, textvariable = v1)
e1.grid(row = 0, column = 1, padx = 10, pady = 5)

e2 = Entry(root, textvariable = v2, show = "*")
e2.grid(row = 1, column = 1, padx = 10, pady = 5)

def show():
    print("用户名是：%s " % e1.get())
    print("密码是：%s " % e2.get())
b1 = Button(root, text = "获取信息", width = 10, command = show)
b1.grid(row = 3, column = 0, sticky = W, padx = 10, pady = 5)
b2 = Button(root, text = "退出", width = 10, command = root.quit)
b2.grid(row = 3, column = 1, sticky = E, padx = 10, pady = 5)

mainloop()