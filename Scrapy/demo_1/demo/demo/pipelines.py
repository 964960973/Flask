# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 管道默认不生效 去seeting打开管道
class DemoPipeline:
    def process_item(self, item, spider):#定死不能更改的item就是数据return就是传递给下一个管道
        print(item)
        return item


class DemoPipeline_1:
    def process_item(self, item, spider):#定死不能更改的item就是数据return就是传递给下一个管道
        item['2'] = '我是管道2'
        print(item)
        return item