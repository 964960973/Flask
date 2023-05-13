# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GetLookItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()#相当于字典里的key
    time_name = scrapy.Field()
    pijia = scrapy.Field()
    pass
