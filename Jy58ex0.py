#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 12:54:17 2017
小甲鱼视频 58 淘宝 贴吧图片抓取
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

def address_get(html):
    rep = r'<img class="BDE_Image" pic_type="\d{0,3}" width="\d{0,3}" height="\d{0,3}" src="([^"]+\.jpg)"'
    imglist = re.findall(rep, html)
   
    '''
    for each in imglist:
        print(each)
        '''
    for each in imglist:
        filename = "/Users/foolwolf0068/feilearngit//"+each.split("/")[-1]
        urllib.request.urlretrieve(each,filename,None)
    
    
    
def main():
    
    url = "http://tieba.baidu.com/p/5330684727"
    html = url_open(url)
    address_get(html)
    

if __name__ == '__main__':
    main()