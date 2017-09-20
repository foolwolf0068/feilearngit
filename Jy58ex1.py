#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:35:30 2017
小甲鱼视频 58 IP地址正则表达式
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
        html = response.read().decode('utf-8')
        
    return html

def ip_find(html):
    rep = r'((?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5]))'
    portnum = re.compile(r'>([1-9]\d{0,4})<')
    portnums = portnum.findall(html)
    ipmatch = re.compile(rep)
    iplist = ipmatch.findall(html)
    # print(portnums)
    # print(iplist) # 打印IP地址测试
    return iplist,portnums
    
def ip_get():
    url = "http://www.xicidaili.com/wt/"
    html = url_open(url)
    # print(html)
    iplist, portnum = ip_find(html)
    myip_list = []
    for i in range(len(iplist)):
        print(iplist[i]+":"+portnum[i])
        myip_list.append(iplist[i]+":"+portnum[i])
    

if __name__ == '__main__':
    ip_get()