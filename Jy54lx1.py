#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 17:04:13 2017
小甲鱼视频 54 下载一只猫
@author: foolwolf0068
"""
from easygui import *
import urllib.request
import chardet
import sys
"""
req = urllib.request.Request("http://placekitten.com/g/500/600")  # request
response = urllib.request.urlopen(req)
cat_img = response.read()
with open("cat_500_600.jpeg","wb") as f:
    f.write(cat_img)"""

def url_open(url):
    headers = {}
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
    data = None
    req = urllib.request.Request(url,data,headers)
    response = urllib.request.urlopen(req)
    # 判断编码格式
    encode_type = chardet.detect(response.read())
    if encode_type['encoding'] == 'GB2312':
        response = urllib.request.urlopen(req)
        html = response.read().decode('GBK')
    else:
        response = urllib.request.urlopen(req)
        html = response.read()# .decode('utf-8')
        
    return html

def main():
    msg = "请填写喵的尺寸"
    fieldNames = ["宽", "高"]
    title = '下载一直喵'
    fieldValues = multenterbox(msg, title, fields=fieldNames, values=[], 
                 callback=None, run=True)    
    # make sure that none of the fields was left blank
    while 1:
        if fieldValues is None: break
        errmsg = ""
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
                errmsg += ('"%s" 是必填项.\n\n' % fieldNames[i])
        if errmsg == "":
            break # no problems found
        fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
    
    print(fieldValues)
    if fieldValues != None:
    
        url = "http://placekitten.com/g/" + fieldValues[0] + "/" + fieldValues[1]
        print(url)
        cat_img = url_open(url)
        filename = filesavebox(msg="请选择存放喵文件夹", title="浏览文件夹",
                               default='/Users/foolwolf0068/feilearngit/', 
                               filetypes=["*.jpg", "*.jpeg"])
        print(filename)
        
        if filename != None :
      
            with open(filename,"wb") as f:
                f.write(cat_img)
        else:
            sys.exit()
        # filesavebox(msg="请选择存放喵文件夹", title="浏览文件夹", default='', filetypes=None)
    else:
        sys.exit()


if __name__ == "__main__":
    main()
    
