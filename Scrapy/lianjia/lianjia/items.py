# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    data_title = scrapy.Field()
    data_money_mi = scrapy.Field()
    data_money_tao = scrapy.Field()
    pass
