'''
FishC C53
'''
import urllib.request
import chardet
def main():
    '''
        url open without proxy build on 18.09.2017
    '''
    url = "http://www.fishc.com/" # http://www.cqu.edu.cn/v1/
    headers = {}
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
    data = None
    req = urllib.request.Request(url,data,headers)

    response = urllib.request.urlopen(req)
    print(response.geturl())
    print(response.info())
    print(response.getcode()) # ce shi shi fou lian jie cheng gong :200
    
    html = response.read()#.decode("utf-8")
    print(html[:301])


'''
def main():
    url = "http://www.cqu.edu.cn/" # http://www.cqu.edu.cn/v1/
    html = url_open(url)
    print(html)
'''

if __name__ == "__main__":
    main()
