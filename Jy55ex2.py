#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 01:27:40 2017
小甲鱼视频 爬虫 隐藏 代理服务器的使用
@author: foolwolf0068
"""

import urllib.request
import random

url = "http://whatismyip.host/"#"http://www.ip-adress.eu/"

iplist = ['122.72.32.88:80', '110.73.5.93:8123','116.7.243.58:53281','110.73.42.81:8123']

proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")]

urllib.request.install_opener(opener)

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"

req = urllib.request.Request(url)
req.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")

response = urllib.request.urlopen(req)

html = response.read().decode('utf-8')

print(html)
