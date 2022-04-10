import requests
url = 'https://www.baidu.com'
head = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
}
response = requests.get(url=url,headers=head)
response.encoding = 'utf8'
print(response.text)
print(response.url)
print(response.content.decode('utf8'))
print(response.status_code)
print(response.headers)