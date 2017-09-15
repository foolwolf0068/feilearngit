# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 14:16:22 2017

@author: Administrator
"""

from tkinter import *
def processOk():
    print("OK,button is clicked by you!")
    
def processCancel():
    print("Cancel button is clicked by you!")
    
window=Tk()
btOk=Button(window,text="OK",fg="red",command=processOk)
btCancel=Button(window,text="Cancel",bg="yellow",command=processCancel)
btOk.pack()
btCancel.pack()
window.mainloop()