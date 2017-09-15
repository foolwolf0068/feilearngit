#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 23:22:40 2017
小甲鱼视频 60
@author: foolwolf0068
"""


import urllib.request
# import os

def url_open(url):
    
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read().decode("utf-8")
    
    return html

def get_img(html):
    p = r'(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])'
    ip_list = re.findall(p,html)
    
    for each in ip_list:
        #filename = each.split('/')[-1]
        #urllib.request.urlretrieve(each,filename,None)
        print(each)



if __name__ == '__main__':
    url = "http://cn-proxy.com"
    get_img(url_open(url))