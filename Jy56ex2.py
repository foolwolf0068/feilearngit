#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 02:17:26 2017
小甲鱼视频 爬虫 ooxx
@author: foolwolf0068
"""

import urllib.request
import os

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def get_page(url):
    
    html = url_open(url).decode('utf-8')
    
    a = html.find('current-comment-page') + 23
    b = html.find(']',a)
    
    print(html[a:b])
    return html[a:b]

url = "http://jandan.net/ooxx"
get_page(url)
#print(url_open(url))
#page_num = int(get_page(url))