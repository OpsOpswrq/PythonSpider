import urllib.request
url = 'https://mail.qq.com/cgi-bin/frame_html?sid=i9c64dqQE7bmlAxu'
headers = {
    'cookie':' ',
    'referer':'https: // mail.qq.com / zh_CN / htmledition / ajax_proxy.html?mail.qq.com & v = 140521',
    'user-agent':'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 100.0.4896.60Safari / 537.36Edg / 100.0.1185.29'
}
request = urllib.request.Request(url=url,headers=headers)
content = urllib.request.urlopen(request)
print(content.read().decode('utf8'))
