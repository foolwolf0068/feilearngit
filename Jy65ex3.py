# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 17:52:56 2017
小甲鱼视频 65
@author: Administrator
"""
from tkinter import *

def callback():
    var.set("吹吧你，我才不信呢~~~")
    
root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set("您下载的影片含有未成年人限制内容，\n请满18周岁后再点击观看！！！")
textlabel = Label(frame1, 
                  textvariable = var,
                  justify = LEFT,
                  )
textlabel.pack(side = LEFT)

photo = PhotoImage(file = "18.gif")
imglabel = Label(frame1,image = photo)
imglabel.pack(side = RIGHT)

theButton = Button(frame2, text = "我已满18周岁",command = callback )
theButton.pack()

frame1.pack(padx = 10, pady = 10)
frame2.pack(padx = 10, pady = 10)
mainloop()