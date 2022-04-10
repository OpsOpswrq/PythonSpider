import scrapy
import scrapy_code.items

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['e.dangdang.com']
    start_urls = ['http://e.dangdang.com/list-QCWX-dd_sale-0-1.html']
    base_url = 'https://e.dangdang.com/list-QCWX-dd_sale-0-'
    page = 1
    def parse(self, response):
        print("====================")
        src = response.xpath('//div[@class="book book_list clearfix"]//span[@class="bookcover"]//img[2]/@src')
        name = response.xpath('//div[@class="book book_list clearfix"]//span[@class="bookcover"]//img[2]/@alt')
        for i in range(len(src)):
            src_img = src[i].extract()
            src_name = name[i].extract()
            book = scrapy_code.items.ScrapyCodeItem(src=src_img,name=src_name)
            yield book
            if DangdangSpider.page<100:
                DangdangSpider.page += 1
                url = DangdangSpider.base_url+str(DangdangSpider.page)+'.html'
                yield scrapy.Request(url=url,callback=self.parse)
