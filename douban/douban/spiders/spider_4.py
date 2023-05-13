import scrapy


class Spider4Spider(scrapy.Spider):
    name = 'spider_4'
    allowed_domains = ['douban.com','doubanio.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']
    page = 1#记录当前爬取的第一页
    def parse(self, response,**kwargs):
        print('回调函数被执行')
        li_list = response.xpath('//ol[@class="grid_view"]/li')
        for li in li_list:
            title = li.xpath('./div/div[2]/div[1]/a/span/text()').extract_first()
            new_url = li.xpath('./div/div[2]/div[1]/a/@href').extract_first()
            xin_ji = li.xpath('./div/div[2]/div[2]/div/span[2]/text()').extract_first()
            pin_jia = li.xpath('./div/div[2]/div[2]/div/span[4]/text()').extract_first()
            title_opp = li.xpath('./div/div[2]/div[2]/p[2]/span/text()').extract_first()


            img_src = li.xpath('./div/div[1]/a/img/@src').extract_first()
            # print(title,new_url,xin_ji,pin_jia,title_opp)
            #生成信息让其保存到csv文件中
            yield {
                'img_src':img_src,
                'title':title,
                'new_url':new_url,
                'xin_ji':xin_ji,
                'pin_jia':pin_jia,
                'title_opp':title_opp,
            }

            yield scrapy.Request(url=response.urljoin(img_src), callback=self.parse_img, cb_kwargs={"img_name":title})
        # next_page_url = response.xpath('//span[@class="next"]/a/@href').extract_first()
        # next_page_url = 'https://movie.douban.com/top250' + next_page_url
        self.page += 1
        if self.page <= 11:
            next_page_url = 'https://movie.douban.com/top250?start=%d&filter=' % ((self.page - 1) * 25)
            yield scrapy.Request(url=next_page_url,callback=self.parse)

    def parse_img(self, response,img_name):
        print('图片处理的回调函数')
        yield{
            'type':'img',
            'img_name':img_name + '.jpg',
            'img_bytes':response.body
        }
