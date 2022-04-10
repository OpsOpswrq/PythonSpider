import urllib.request
import urllib.parse
import urllib.error
url = "https://qq.mail/111"
try:
    urlopen = urllib.request.urlopen(url)
    content = urlopen.read().encode("utf8")
except urllib.error.HTTPError:
    print("网址后面有问题")
except urllib.error.URLError:
    print("网址错误")
