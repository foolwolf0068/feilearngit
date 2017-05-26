#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 11:02:59 2017

@author: foolwolf0068
"""

import urllib
from jparser import PageModel
html = urllib.urlopen("http://www.pythontab.com").read().decode('gb18030')
pm = PageModel(html)
result = pm.extract()
print("**title**")
print(result['title'])
print("==content==")
for x in result['content']:
    if x['type'] == 'text':
        print(x['data'])
    if x['type'] == 'image':
        print("[IMAGE]", x['data']['src'])