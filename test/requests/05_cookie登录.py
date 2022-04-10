import requests
from lxml import etree
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
}
response =  requests.get(url=url,headers=headers)
content = response.text
tree = etree.HTML(content)
viewState = tree.xpath('//input[@id="__VIEWSTATE"]/@value')
viewStateGenerator = tree.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')
url_img = 'https://so.gushiwen.cn/RandCode.ashx'
session = requests.session()
response_img = session.get(url_img)
content_img = response_img.content
with open("Ensure.jpg",'wb') as fp:
    fp.write(content_img)
code_name = input("请输入验证码")
data={
    '__VIEWSTATE': viewState,
    '__VIEWSTATEGENERATOR': viewStateGenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '2560965468@qq.com',
    'pwd': '123456',
    'code': code_name,
    'denglu': '登录'
}
url_login = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
response = session.post(url=url_login,data=data,headers=headers)
content = response.text
with open("success.html",'w',encoding="utf8") as fp:
    fp.write(content)






