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





def main():
    while True:
        contents = input('Please enter the contents you want to translate:\n')
        if contents.lower() in "quitqeexit":
            break
        else:
            #url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"#\
            #&sessionFrom=http://www.youdao.com/"
            url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"

            data = {}
            data['i'] = contents #'I love Feige.com!'
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
            data['ue'] = 'UTF-8'
            data['typoResult'] = 'true'

            data = urllib.parse.urlencode(data).encode('utf-8')
            req = urllib.request.Request(url,data,headers) # very import
            response = urllib.request.urlopen(req)
            html = response.read().decode('utf-8')
            target = json.loads(html)
            # print(html)
            print("The result：%s" %(target["translateResult"][0][0]["tgt"]))

if __name__=="__main__":
    main()
