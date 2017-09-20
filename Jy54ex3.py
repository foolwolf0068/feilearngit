import urllib.request
import urllib.parse
import json

def main():
    while True:
        content=input("请输入需要翻译的内容（退出输入q）：")
        if content in ("Q","q","quit"):
            break
        else:
            url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/"

            data={}
            data["type"]="AUTO"
            data["i"] = content
            data["doctype"] = "json"
            data["xmlVersion"] = "1.8"
            data["keyfrom"] = "fanyi.web"
            data["ue"] = "utf-8"
            data["action"] = "FY_BY_CLICKBUTTON"
            data["typoResult"] = "true"
            data=urllib.parse.urlencode(data).encode("utf-8")

            # 增加headers，模拟登陆，而不是对服务器识别为机器登陆。
            headers={}
            headers["User-Agent"]="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"

            req=urllib.request.Request(url,data,headers)

            #或者使用Request.add_header(key,value)
            # req=urllib.request.Request(url,data)
            # req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36")

            response=urllib.request.urlopen(req)
            html=response.read().decode("utf-8")

            target=json.loads(html)
            # print (type(target))
            # print (target["translateResult"])
            # print (target["translateResult"][0][0])
            print("翻译的结果为：%s" %(target["translateResult"][0][0]["tgt"]))

if __name__=="__main__":
    main()
