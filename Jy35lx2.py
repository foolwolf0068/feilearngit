#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:15:21 2017
小甲鱼视频 35
@author: foolwolf0068
"""
from easygui import *

# diropenbox(msg=None, title=None, default=None)
title1 = "打开"
default1 = "/Users/********/feilearngit/*.txt"
filetypes1 = "*.txt"#["*.css", ["*.htm", "*.html", "HTML files"]]
filename = fileopenbox(msg="请选择要打开的文件：", title=title1, default=default1, 
            filetypes = filetypes1, multiple=False)

print(filename)

if filename != None:   

    msg1 = "文件%s内容如下："%filename
    with open(filename) as f:
        contents = f.readlines()
        
    textbox(msg=msg1, title='显示文件内容 ', text=contents, 
            codebox=False, callback=None, run=True)


# filesavebox(msg=None, title=None, default='', filetypes=None)
