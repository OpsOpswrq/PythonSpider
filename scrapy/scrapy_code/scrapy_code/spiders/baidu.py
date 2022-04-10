import scrapy
import scrapy as scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/s?wd=ip']
    def parse(self, response, **kwargs):
        url = 'https://www.baidu.com/s?wd=ip'
        yield scrapy.Request(url=url,callback=self.download)
    def download(self,response):
        with open('daili.html','w',encoding="utf8") as fp:
            fp.write(response.text)
