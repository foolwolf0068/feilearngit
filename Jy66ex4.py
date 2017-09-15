# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 19:15:32 2017
小甲鱼视频 66
@author: Administrator
"""

from tkinter import *

root = Tk()
group = LabelFrame(root, text = "最好的编程语言是？", padx = 5, pady= 5)
group.pack(padx = 10, pady = 10)
Langs = [
        ("Python",1),
        ("R",2),
        ("C",3),
        ("Perl",4),
        ("Ruby",5)
        ]

v = IntVar()
# v.set(1)
for lang,num in Langs:
    b = Radiobutton(group, text = lang, variable = v, value = num, 
                    indicatoron = False)
    b.pack(fill = X)
mainloop()
