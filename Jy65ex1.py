# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 17:35:26 2017
小甲鱼视频 65
@author: Administrator
"""

from tkinter import *

root = Tk()
textlabel = Label(root, 
                  text = "您下载的影片含有未成年人限制内容，\n请满18周岁后再点击观看！！！",
                  justify = LEFT,
                  padx = 10)
textlabel.pack(side = LEFT)

photo = PhotoImage(file = "18.gif")
imglabel = Label(root,image = photo)
imglabel.pack()

mainloop()