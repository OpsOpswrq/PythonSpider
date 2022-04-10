import requests
url = 'https://www.baidu.com/s?'
head = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
}
kw = input("请输入查询的内容")
data={
    'wd':kw
}
response = requests.get(url=url,params=data,headers=head)
content = response.text
with open("lp.html",'w',encoding='utf8') as fp:
    fp.write(content)