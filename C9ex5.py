#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 22:29:23 2017
PYthon 语言程序设计
@author: foolwolf0068
"""
# ex 9-5
from tkinter import *

class ChangeLabelDemo:
    def __init__(self):
        window = Tk()
        window.title("Change Label Demo")
        
        # Add a label to framel
        frame1 = Frame(window)
        frame1.pack()
        self.lbl = Label(frame1, text = "Programming is fun.")
        self.lbl.pack()
        
        
        # Add a label , entry, button, two radio buttons to frame2
        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text = "Eeter text:")
        self.msg = StringVar()
        entry = Entry(frame2, textvariabel = self.msg)
        btChangeText = Button()
        