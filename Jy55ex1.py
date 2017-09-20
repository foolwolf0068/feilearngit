#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 01:27:40 2017
小甲鱼视频 爬虫 隐藏 代理服务器的使用
@author: foolwolf0068
"""

import urllib.request
import random

url = "http://www.ip138.com/"

iplist = ['111.62.251.130:8080','210.38.1.130:8080','120.199.224.79:80','111.13.7.42:81']

proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('user-agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)

html = response.read().decode('utf-8')

print(html)
