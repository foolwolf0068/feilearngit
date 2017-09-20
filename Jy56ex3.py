#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 20:16:25 2017
小甲鱼视频 ooxx爬虫 修改
@author: foolwolf0068
"""

from bs4 import BeautifulSoup
import urllib.request
import chardet
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
        html = response.read()# .decode('utf-8')
        
    return html


def get_page(url):
    
    html = url_open(url).decode('utf-8')
    
    # a = html.find('current-comment-page') + 23
    # b = html.find(']',a)
    result = re.findall(r"\w{4}\"\>\[([1-9]{1}\d{0,2})]", html)
    
    #print(result[:])
    #print(html[a:b])
    #return html[a:b]
    return result[0]   
    
    
def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []
    
    a = html.find('img src=')
    while a != -1:
        
        b = html.find('.jpg',a,a+255)
        if b != -1:
            img_addrs.append(html[a+9:b+4])
        else:
            b = a + 9
        
        a = html.find('img src=',b)
    for i in range(len(img_addrs)):
        img_addrs[i] = "http:" + img_addrs[i]
    return img_addrs

def main():
    url = "http://jandan.net/ooxx/"
    print(get_page(url))
    
    
if __name__ == '__main__':
    main()
    