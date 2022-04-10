import urllib.request

url = "https://www.baidu.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
}
request = urllib.request.Request(url=url,headers=headers)
handler = urllib.request.HTTPSHandler()
opener = urllib.request.build_opener(handler)
response = opener.open(request)
print(response.read().decode("utf8"))