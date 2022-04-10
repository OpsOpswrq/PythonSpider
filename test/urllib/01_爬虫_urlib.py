import urllib.request
url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)
content1 = response.read().decode('utf8')
print(content1)
content2 = response.readline().decode('utf8')
print(content2)
content3 = response.readlines()
for s in content3:
    s = s.decode('utf8')
    print(s)
code = response.getcode()
print(code)
headers = response.getheaders()
print(headers)
url_img = 'https://img2.baidu.com/it/u=331121307,2721562722&fm=253&fmt=auto&app=138&f=JPEG?w=561&h=500'
urllib.request.urlretrieve(url_img,'img1.png')
url_html = 'http://www.baidu.com'
urllib.request.urlretrieve(url_html,"baidu.html")
url_mp4 = 'https://www.ixigua.com/2b6ea4dd-4d49-4a45-8847-c5d3f3ab287e'
urllib.request.urlretrieve(url_mp4,"1.mov")
