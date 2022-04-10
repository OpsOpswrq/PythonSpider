import random
import urllib.request
url = "http://www.baidu.com/s?wd=ip"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
}
request = urllib.request.Request(url=url,headers=headers)
proxy_pool = [{'http':'180.97.34.35:80'},
{'http':'180.97.34.35:80'}]
proxy = random.choice(proxy_pool)
print(proxy)
handler = urllib.request.ProxyHandler(proxies=proxy)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
content = response.read().decode("utf8")
with open("daili.html",'w',encoding="utf-8") as fp:
    fp.write(content)
print(content)