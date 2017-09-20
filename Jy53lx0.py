#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 11:10:36 2017
小甲鱼视频 54 lx0
@author: foolwolf0068
"""
import urllib.request
import chardet
def url_open(url):
    '''
        url open without proxy build on 18.09.2017
    '''
    # url = "http://www.fishc.com/" 
    headers = {}
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
    data = None
    req = urllib.request.Request(url,data,headers)

    response = urllib.request.urlopen(req)
    #print(response.geturl())
    #print(response.info())
   # print(response.getcode()) # ce shi shi fou lian jie cheng gong :200
    
    # html = response.read().decode("utf-8")
    
    #print(chardet.detect(response.read()))
    # codetype = chardet.detect(response.read())['encoding']
    if chardet.detect(response.read())['encoding'] == 'GB2312':
        response = urllib.request.urlopen(req)
        html = response.read().decode('GBK')
    else:
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
    return html
    # print(html[:300])

def main():
    url = "http://www.fishc.com/"
    html = url_open(url)
    print(html[:300])


if __name__ == "__main__":
    main()
