import requests
import json
url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
head = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
}
kw = input('请输入查询的单词')
data = {
    'i': kw,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '16494182620572',
    'sign': 'c521d2d26a9fc119a78cf48ce1525f28',
    'lts': '1649418262057',
    'bv': 'cfddf5227f0e08de65d069a5a4aeacca',
    'doctype': 'json',
    'version': 2.1,
   'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
}
response = requests.post(url=url,data=data,headers=head)
content = response.text
obj = json.loads(content)
print(obj.get("translateResult")[0][0].get("tgt"))
