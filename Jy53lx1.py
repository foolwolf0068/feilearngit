#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 11:14:53 2017

@author: foolwolf0068
"""

import urllib.request
import chardet
def main():
    '''
        url open without proxy build on 18.09.2017
    '''
    # url = "http://www.fishc.com/" # http://www.cqu.edu.cn/v1/
    url = input("请输入URL: ")
    url += "//"
    headers = {}
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
    data = None
    req = urllib.request.Request(url,data,headers)

    response = urllib.request.urlopen(req)
    
    encode_type = chardet.detect(response.read())
    print('该网页使用的编码是: %s'\
          % encode_type['encoding'])
   




if __name__ == "__main__":
    main()