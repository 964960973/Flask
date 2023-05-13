import scrapy
from get_look.items import GetLookItem

class Spider1Spider(scrapy.Spider):
    name = 'spider_2'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/latest']

    def parse(self, response,**kwargs):
        txt = response.xpath('//li[@class="media clearfix"]')
        for li in txt:
            s = li.xpath('./div/h2/a/text()').extract()[0]
            ll = li.xpath('./div/p/text()').extract()[0]
            loo = li.xpath('./div/p/span/text()').extract()[0]

            douban = GetLookItem()
            douban['name'] = s
            douban['time_name'] = ll
            douban['pijia'] = loo
            yield douban

            # dic = {
            #     '书名': s,
            #     '作者_时间': ll,
            #     '评价人数': loo
            # }
            # yield dic
