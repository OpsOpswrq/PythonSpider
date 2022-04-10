import scrapy


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['https://car.autohome.com.cn/price/brand-15.html']
    start_urls = ['https://car.autohome.com.cn/price/brand-15.html']

    def parse(self, response):
        print("=======================")
        span_list = response.xpath('//div[@class="list-cont-main"]//a[@class="font-bold"]/text()')
        price_list = response.xpath('//div[@class="list-cont-main"]//span[@class="font-arial"]/text()')
        for i in range(len(price_list)):
            print(span_list[i].extract())
            print(price_list[i].extract())



# https://m.dushu.com/book/1188_0_0_3.html
# https://m.dushu.com/book/1188.html
# //a[@class="button button-middle"]/@href