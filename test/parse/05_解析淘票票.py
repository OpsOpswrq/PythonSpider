import urllib.request
url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1649474147833_97&jsoncallback=jsonp98&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
headers = {
'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'cookie': 'cna=XtW9GhXfXCUCAXjHObYnA23c; t=0cea42b4f0d0d4517f25cca911fb81b9; cookie2=193c2839a033834342c76851382f0311; v=0; _tb_token_=7e6e010380b07; xlly_s=1; _m_h5_tk=7895dc5f2dfb0c2c063efb9c27f25aa1_1649483113485; _m_h5_tk_enc=4edbdff1bf9240381471c7a3ee2337ac; tfstk=cg4cBsV8goof-InuAZgf54lX2NsdZ9x-HDnuzsm3ta4uDmaPiVtyY83XhYXC3h1..; l=eBx9GNBuLRRdzwchBO5BFurza77TaQRbzrVzaNbMiInca1ohtF9FmOC3HG-eSdtjgtfUueKyl-7T0Rep8aUdggiMW_N-1NKD7YJw-; isg=BPj4FSJ07guU1gKSV6hTiCajyaaKYVzrMmanPjJrnTPmTZo323CPe1wrBUV9GxTD',
'referer': 'https://dianying.taobao.com/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
'sec-ch-ua-mobile': "?0",
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36',
'x-requested-with': 'XMLHttpRequest'
}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf8")
content = content.split('(')[1].split(')')[0]
with open('../json/1.json','w',encoding="utf8") as fp:
    fp.write(content)

import json
import jsonpath

obj = json.load(open("../json/1.json", 'r', encoding="utf8"))
regionName_list = jsonpath.jsonpath(obj, '$..regionName')
print(regionName_list)