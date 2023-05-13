import scrapy


class Spider1Spider(scrapy.Spider):
    name = 'spider_1'#爬虫名称
    allowed_domains = ['4399.com']#允许的域名
    start_urls = ['https://www.4399.com/flash/']#起始页


    def parse(self, response):#默认方法是用来处理解析的
        # response.json()
        # response.css()#css选择器解析
        # response.xpath()xpath选择器解析
        # 获取所有的名称
        # txt = response.xpath('//ul[@class="n-game cf"]/li/a/b/text()').extract()#提取内容返回一个列表
        # print(txt)
        li_txt = response.xpath('//ul[@class="n-game cf"]/li')
        for li in li_txt:
            oser = li.xpath('./a/b/text()').extract_first()#提取内容返回一个数据
            cart = li.xpath('./em/a/text()').extract_first()#提取内容返回一个数据
            data = li.xpath('./em/text()').extract_first()#提取内容返回一个数据
            dict_1 = {
                'name':oser,
                'cart':cart,
                'data':data
            }
            #将数据传递给管道
            yield dict_1 #返回数据传递管道pipeline