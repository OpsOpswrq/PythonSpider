import scrapy
from scrapy_code.items import ScrapyCodeItem

class DyttSpider(scrapy.Spider):
    name = 'dytt'
    allowed_domains = ['www.dygod.net']
    start_urls = ['https://www.dygod.net/html/gndy/dyzz/index.html']

    def parse(self, response):
        title_list = response.xpath('//a[@class="ulink"]/@title')
        page_list = response.xpath('//a[@class="ulink"]/@href')
        for i in range(len(title_list)):
            page_src = 'https://www.dygod.net'+page_list[i].extract()
            name = title_list[i].extract()
            yield scrapy.Request(url=page_src,callback=self.page_second,meta={'name':name})


    def page_second(self,response):
        content = response.xpath('//div[@id="Zoom"]//img[1]/@src')
        src_img = 'https://www.dygod.net'+content.extract()[0]
        name = response.meta['name']
        movie = ScrapyCodeItem(name=name,src=src_img)
        yield movie
