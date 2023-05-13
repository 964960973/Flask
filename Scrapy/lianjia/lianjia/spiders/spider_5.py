import scrapy


class Spider5Spider(scrapy.Spider):
    name = 'spider_5'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://hz.fang.lianjia.com/loupan/']
    page = 1
    def parse(self, response):
        new_urls = response.xpath('//a[@class="resblock-img-wrapper "]/@href').extract()
        for new_url in new_urls:
            new_url = 'https://hz.fang.lianjia.com' + new_url
            yield scrapy.Request(
                url=response.urljoin(new_url),
                method='get',  # 请求方式
                callback=self.parse_detail  # 回调函数 进行解析响应内容
            )
        self.page += 1
        if self.page <= 10:
            next_page_url = 'https://hz.fang.lianjia.com/loupan/pg%d/' % (self.page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_detail(self,response):
        data_title = response.xpath('//div[@class="mod-wrap mod-resblock-name-bar clearfix"]/div/div/h2/text()').extract_first()
        data_money_mi = response.xpath('//span[@class="price-number"]/text()')[0].extract()
        data_money_tao = response.xpath('//span[@class="price-number"]/text()')[1].extract()
        yield {
            'data_title':data_title,
            'data_money_mi':data_money_mi,
            'data_money_tao':data_money_tao,
        }
        print(data_title)



