#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 17:59:14 2017
小甲鱼视频——53 爬虫
@author: foolwolf0068
"""

import urllib.request
path_name = "http://www.cqu.edu.cn"
response = urllib.request.urlopen(path_name)
html = response.read()
html = html.decode("utf-8")
print(html)

