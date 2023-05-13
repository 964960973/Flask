# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy.pipelines.images import ImagesPipeline
import scrapy
import pymysql
from huashi6.settings import MYSQL

class Huashi6Pipeline:
    def process_item(self, item, spider):
        # 数据存储
        return item


class GetLookPipeline_mysql:
    '''
    我们希望的是，在爬虫开始的时候，打开这个文件，
    在执行过程中不断地往里存储数据，在执行完毕后关掉这个文件
    '''
    def open_spider(self,spider):
        self.conn = pymysql.connect(
            host=MYSQL['host'],
            port=MYSQL['port'],
            user=MYSQL['user'],
            password=MYSQL['password'],
            database=MYSQL['database']
        )

    def close_spider(self,spider):
        if self.conn:
            self.conn.close()
    def process_item(self, item, spider):
        try:
            cursor = self.conn.cursor()
            sql = 'insert into huashi6 (name,img_src,local_path) values (%s, %s, %s)'
            cursor.execute(sql,(item['img_name'],item['img_src'],item['local_path']))
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            if cursor:
                cursor.close()
        return item


class Huashi_6(ImagesPipeline):#利用图片管道帮助我们完成下载操作
    def get_media_requests(self,item,info):#准备下载的
        yield scrapy.Request(item['img_src'])#直接返回一个请求

    def file_path(self, request,response=None, info=None):#准备的文件路径
        file_name = request.url.split('/')[-1]#request.url可以直接获取到请求的url
        return f'img/{file_name}'#img/xxx.jpg
    def item_completed(self,results, item, info):#返回文件的详细信息
        ok,finfo = results[0]
        print(finfo)
        try:
            item['local_path'] = finfo.get("path","")
        except:
            return item
        return item


