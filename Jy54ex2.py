#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 18:16:53 2017
小甲鱼视频 爬虫 实战
@author: foolwolf0068
"""

import urllib.request
import urllib.parse
import json

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'

data = {}
data['i'] = 'I love Feige.com!'
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '1504089666655'
data['sign'] = 'c4adf2cfc626975b6fe1e241a93bbf0c'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
#data['ue'] = 'UTF-8'
data['typoResult'] = 'true'
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data,head)
html = response.read().decode('utf-8')
target = json.loads(html)
print(html)

