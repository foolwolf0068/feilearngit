# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 14:36:41 2017

@author: Administrator
"""

from tkinter import *
class processButtonEvent(object):
    def __init__(self):
        window=Tk()
        btOk=Button(window,text="OK",fg="red",command=processOk)
        btCancel=Button(window,text="Cancel",bg="yellow",command=processCancel)
        btOk.pack()
        btCancel.pack()
        window.mainloop()
    def processOk(self):
        print("OK,button is clicked by you!")
    
    def processCancel(self):
        print("Cancel button is clicked by you!")
        
processButtonEvent()