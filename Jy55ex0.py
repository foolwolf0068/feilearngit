#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:29:32 2017

@author: foolwolf0068
"""



import urllib.request
import chardet,os
import re



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
        html = response.read().decode('utf-8')        
    return html

def get_page(html):
    a = html.find('current-comment-page') + 23
    b = html.find(']',a)    
    return html[a:b]

def address_get(html):
    
    rep = r'<img src="([^"]+\.jpg|[^"]+\.gif)"'
    imglist = re.findall(rep, html)
   
    
    for each in imglist:        
        filename = each.split("/")[-1]
        imgurl = "http:"+each
        if "thumb180" in imgurl:
            imgurl = imgurl.replace("thumb180","mw690")
        print(imgurl)
            
        urllib.request.urlretrieve(imgurl,filename)
    
def main():

    pages = 5    
    path = os.getcwd()
    path = os.path.join(path,'ooxx2')
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path) #'''                #创建文件夹
    url = "http://jandan.net/ooxx/"
    html = url_open(url)
    page_current = int(get_page(html))
    for i in range(pages):
        url_new = url + "page-"+str(page_current-i)+"#comments"
        html = url_open(url_new)
        address_get(html) 
   
    
if __name__ == "__main__":
    main()
    