import urllib.request
import urllib.parse
url = 'https://www.baidu.com/s?wd='
name = urllib.parse.quote('喜多川海梦')
url+=name
head = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
}
request = urllib.request.Request(url=url,headers=head)
urlopen = urllib.request.urlopen(request)
print(urlopen.read().decode("utf8"))
