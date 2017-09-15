#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 17:59:14 2017
小甲鱼视频——53 爬虫
@author: foolwolf0068
"""

import urllib.request
response = urllib.request.urlopen("http://www.fishc.com")
html = response.read()
html = html.decode("utf-8")
print(html)

