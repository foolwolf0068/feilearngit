#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:53:06 2017

@author: foolwolf0068
"""

import easygui as g
import os

file_path = g.fileopenbox(default="*.txt")

with open(file_path) as f:
    title = os.path.basename(file_path)
    msg = "文件【%s】的内容如下：" % title
    text = f.read()
    g.textbox(msg, title, text)
