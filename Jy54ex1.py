#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 18:10:18 2017
小甲鱼视频 爬虫 实战
@author: foolwolf0068
"""

import urllib.request
req = urllib.request.Request("http://placekitten.com/g/500/600")  # request
response = urllib.request.urlopen(req)
cat_img = response.read()
with open("cat_500_600.jpeg","wb") as f:
    f.write(cat_img)
