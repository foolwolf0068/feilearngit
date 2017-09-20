#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 11:23:56 2017
小甲鱼视频 53 lx 3
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
    # 判断编码格式
    encode_type = chardet.detect(response.read())
    if encode_type['encoding'] == 'GB2312':
        response = urllib.request.urlopen(req)
        html = response.read().decode('GBK')
    else:
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        
    return html

def file_read(filename):
    f = open(filename)
    contents = f.readlines()
    f.close()
    return contents

def html_save(filename,html):
    f = open(filename,'w')
    f.writelines(html)
    f.close()
    
    

def main():
    filename = 'urls.txt'
    sites = file_read(filename)
    print(sites)
    #html = url_open("http://www.cqu.edu.cn")
    #html = url_open("http://www.fishc.com")
    #print(html)
    #for site in sites:
        #print(site)
    num = 1
    for site in sites:        
        html = url_open(site)        
        #print(html)
        subfilename = "url_" + str(num)+".txt"
        html_save(subfilename,html)
        num += 1
        
    print("文件[%s]中的 %d 个网址的网页已保存完毕"%(filename, num-1))
    


if __name__ == "__main__":
    main()
