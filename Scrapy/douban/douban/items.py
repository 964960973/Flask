# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    img_src = scrapy.Field()
    title = scrapy.Field()
    new_url = scrapy.Field()
    xin_ji = scrapy.Field()
    pin_jia = scrapy.Field()
    title_opp = scrapy.Field()
    img_name = scrapy.Field()
    img_bytes = scrapy.Field()
    pass
