# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 19:30:27 2017
小甲鱼视频 67
@author: Administrator
"""

from tkinter import *

root = Tk()

Label(root, text = "用户名：").grid(row = 0, column = 0)
Label(root, text = "密码：").grid(row = 1, column = 0)
v1 = StringVar()
v2 = StringVar()

e1 = Entry(root,textvariable = v1)
e2 = Entry(root,textvariable = v2, show = "*")
e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)

def show():
    print("用户名：%s" % e1.get())
    print("密码：%s" % e2.get())
Button(root, text = "获取信息", width = 10, command = show).grid(row = 3, column = 0, sticky = W, padx = 10, pady = 5)
Button(root, text = "退出", width = 10, command = root.quit).grid(row = 3, column = 1, sticky = E, padx = 10, pady = 5)
mainloop()
