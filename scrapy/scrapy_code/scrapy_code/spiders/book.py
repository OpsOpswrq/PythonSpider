import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_code.items import ScrapyCodeItem

class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['m.dushu.com']
    start_urls = ['https://m.dushu.com/book/1188_0_0_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/book/1188_0_0_\d+\.html'), callback='parse_item', follow=False),
    )
    def parse_item(self, response):
        src_img = response.xpath('//div[@class="item-media"]/img[1]/@src')
        name_list = response.xpath('//div[@class="item-title"]/text()')
        for i in range(len(src_img)):
            src= src_img[i].extract()
            name = name_list[i].extract()
            book = ScrapyCodeItem(name=name,src=src)
            yield book
