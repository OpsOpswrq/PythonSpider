import scrapy
import json

class BaidutranslationSpider(scrapy.Spider):
    name = 'baiduTranslation'
    allowed_domains = ['https://fanyi.baidu.com']
    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'
        kw = input("请输入查询的单词")
        data = {
            'kw':kw,
        }
        yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse_second)

    def parse_second(self,response):
        content = response.text
        obj = json.loads(content)
        for i in range(len(obj.get("data"))):
            print(obj.get("data")[i].get("v"))  # 对应原来的数据进行抽取
