# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 17:16:13 2017
小甲鱼视频 64
@author: Administrator
"""
# ex64

import tkinter as tk

class APP:
    def __init__(self,master):
        frame = tk.Frame(master)
        frame.pack(side = tk.RIGHT)
        
        self.hi_there = tk.Button(frame, text = "打招呼", fg = "red",command = self.say_hi)
        self.hi_there.pack()
    def say_hi(self):
        print("大家好，我是飞哥!!!")
        
root = tk.Tk()
app = APP(root)

root.mainloop()
