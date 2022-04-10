import urllib.request
import lxml.etree
def create_request(page):
    if page==1:
        url = 'https://sc.chinaz.com/tupian/shuaigetupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/shuaigetupian_'+str(page)+'.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
    }
    request = urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf8")
    return content
def down_img(content):
    tree = lxml.etree.HTML(content)
    url_img = tree.xpath('//div[@id="container"]//a/img/@src2')
    for i in range(len(url_img)):
        urllib.request.urlretrieve("https:"+url_img[i],str(i)+'.jpg')
if __name__ == '__main__':
    start_page = int(input('请输入起始页'))
    end_page = int(input('请输入结束页'))
    for i in range(start_page,end_page+1):
        request = create_request(i)
        content = get_content(request)
        down_img(content)