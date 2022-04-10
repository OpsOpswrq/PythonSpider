import urllib.request
from bs4 import BeautifulSoup
url = 'https://www.starbucks.com.cn/menu/'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf8")
soup = BeautifulSoup(content,'lxml')
obj = soup.select('ul[class="grid padded-3 product"] div')
for i in range(len(obj)):
    url_img = 'https://www.starbucks.com.cn'+obj[i].attrs.get("style").split('"')[1]
    urllib.request.urlretrieve(url_img,str(i)+'.jpg')