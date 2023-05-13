# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql
import pymongo

from get_look.settings import MYSQL
'''
存储数据的方案：
    1.数据存储到csv文件
    2.数据存储到mysql数据库中
    3.数控存储在MongoDb中
    4.文件的存储
'''

class GetLookPipeline:
    '''
    我们希望的是，在爬虫开始的时候，打开这个文件，
    在执行过程中不断地往里存储数据，在执行完毕后关掉这个文件
    '''
    def open_spider(self,spider):
        print('开始存储文件')
        self.f = open('./豆瓣.csv',mode='a',encoding='utf-8')

    def close_spider(self,spider):
        self.f.close()
        print('文件保存完毕')

    def process_item(self, item, spider):
        # with open('./豆瓣.csv',mode='a',encoding='utf-8')as f:
        self.f.write(f"{item['name']},{item['time_name']},{item['pijia']}\n")
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
            sql = 'insert into douban (书名, 时间, 评价) values (%s, %s, %s)'
            cursor.execute(sql,(item['name'],item['time_name'],item['pijia']))
            self.conn.commit()

        except:
            self.conn.rollback()
        finally:
            if cursor:
                cursor.close()
        return item


class GetLookPipeline_mongdb:
    '''
    我们希望的是，在爬虫开始的时候，打开这个文件，
    在执行过程中不断地往里存储数据，在执行完毕后关掉这个文件
    '''
    def open_spider(self,spider):
        #建立链接
        self.client = pymongo.MongoClient(host='localhost',port=27017)
        # 要执行的数据库名称
        db = self.client['douban']
        #指定豆瓣集合
        self.collection = db['豆瓣']

    def close_spider(self,spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.insert({"name":item['name'],"time_name":item['time_name'],"pijia":item['pijia']})
        return item
