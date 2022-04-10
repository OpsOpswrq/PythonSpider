import urllib.request
import urllib.parse
import json
def create_request(page):
    url = "https://movie.douban.com/j/chart/top_list?type=25&interval_id=100%3A90&action=&"
    data = {
        'start': (page-1)*20,
        'limit': 20,
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
    }
    data = urllib.parse.urlencode(data)
    url+=data
    request = urllib.request.Request(url=url,headers=headers)
    return request
def get_content(req):
    res = urllib.request.urlopen(req)
    content = res.read().decode("utf8")
    dic1 = json.loads(content)
    return dic1
if __name__ == "__main__":
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))
    for page in range(start_page,end_page+1):
        request = create_request(page)
        content = get_content(request)
        for i in range(len(content)):
            print(content[i].get("title")+"  "+content[i].get("url"))
