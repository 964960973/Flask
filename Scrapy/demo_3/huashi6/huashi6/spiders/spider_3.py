import scrapy

# from urllib.parse import urljoin

from huashi6.items import Huashi6Item

class Spider3Spider(scrapy.Spider):
    name = 'spider_3'
    allowed_domains = ['huashi6.com']
    start_urls = ['https://www.huashi6.com/rank/month/2023-04-01']

    def parse(self, response,**kwargs):
        txt = response.xpath('//div[@class="p-rank-list"]/a')
        for href in txt:
            href = href.xpath('./@href').extract_first()
            # print(href)
#           根据scrapy运行原理，此处应该对href进行处理，
#           处理成一个请求，交给引擎
            yield scrapy.Request(
                url=response.urljoin(href),
                method = 'get',#请求方式
                callback=self.parse_detail#回调函数 进行解析响应内容
            )
        #下一页
        next_href = response.xpath('//div[@class="rank-pagination-item"]/span[contains(text(),"前几月")]').extract_first()
        if next_href:
            new_urls = response.xpath('//a[@class="rank-pagination-item"]/@href').extract()
            for new_url in new_urls:
                yield scrapy.Request(
                    url=response.urljoin(new_url),
                    callback=self.parse
                )

    def parse_detail(self, response,**kwargs):
        try:
            img_src = 'https://img2.huashi6.com/images' + str(response.xpath('//picture[@class="c-img-loading img-vec"]/img/@data-original').extract_first()).split('images')[1].split('jpg?')[0] + 'jpg'
        except:
            img_src = 'https://img2.huashi6.com/images' + response.xpath('//picture[@class="c-img-loading c-spider-img img-vec"]/source/@srcset').extract_first().split('images')[1].split('jpg?|')[0] + 'jpg'
        img_name = response.xpath('//div[@class="container c-app-bread"]/p/a[3]/text()').extract_first()
        item = Huashi6Item()
        item['img_src'] = img_src
        item['img_name'] = img_name
        yield item

