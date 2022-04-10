import json
import urllib.parse
import urllib.request


def create_request(keyword,page):
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
    data = {
        'cname': keyword,
        'pageIndex': page,
        'pageSize': 10,
        'pid': ""
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
    }
    data = urllib.parse.urlencode(data).encode("utf-8")
    request = urllib.request.Request(url=url,headers=headers,data=data)
    return request


def get_content(request):
    content = urllib.request.urlopen(request)
    dic1 = json.loads(content.read().decode("utf-8"))
    return dic1


if __name__  == "__main__":
    start_page = int(input("请输入起始页"))
    end_page = int(input("请输入结束页"))
    key_word = input("请输入地址")
    for page in range(start_page,end_page+1):
        request = create_request(key_word,page)
        content = get_content(request)
        for i in range(len(content.get("Table1"))):
            print(content.get("Table1")[i].get("addressDetail")+"  "+content.get("Table1")[i].get("storeName"))