#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:45:14 2017
小甲鱼视频 35 
@author: foolwolf0068
"""
from easygui import *

def main():
    msg = "【*真实姓名】为必填项。\n【*手机号码】为必填项。\n【*E-mail】为必填项。"
    fieldNames = ["用户名", "*真实姓名","地址","*手机号码","QQ","*E-mail"]
    title = '账号中心'
    fieldValues = multenterbox(msg, title, fields=fieldNames, values=[], 
                 callback=None, run=True)
    
    # make sure that none of the fields was left blank
    while 1:
        if fieldValues is None: break
        errmsg = ""
        for i in range(len(fieldNames)):
            if (i in [1,3,5]) and fieldValues[i].strip() == "":
                errmsg += ('"%s" 是必填项.\n\n' % fieldNames[i])
        if errmsg == "":
            break # no problems found
        fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
    
    #filesavebox(msg="请选择存放喵文件夹", title="浏览文件夹", default='', filetypes=None)
    # print("Reply was: %s" % str(fieldValues))

if __name__ == "__main__":
    main()