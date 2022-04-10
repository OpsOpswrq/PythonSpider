# eg:请求百度翻译
import urllib.parse
import urllib.request
import json
url = 'https://fanyi.baidu.com/sug'
head = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
}
kw = input('请输入查询的单词')
data = {
    'kw':kw
}
data = urllib.parse.urlencode(data).encode("utf8")   # 这里还要转换，因为服务器处理的是utf-8的数据，important
request = urllib.request.Request(url=url,headers=head,data=data)   # post的方式
response = urllib.request.urlopen(request)
content = response.read().decode("utf8")
json1 = json.loads(content)
print(json1)
count = len(json1.get("data"))
for i in range(count):
    print(json1.get("data")[i].get("v"))
