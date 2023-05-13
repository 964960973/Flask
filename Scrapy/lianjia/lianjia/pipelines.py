# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import hashlib
from itemadapter import ItemAdapter
import pymysql
from scrapy.exceptions import DropItem
from lianjia.settings import MYSQL
from redis import StrictRedis
class LianjiaPipeline:
    def process_item(self, item, spider):
        redis_client =StrictRedis(host='127.0.0.1', port=6379,db=0)
        item_str = json.dumps(item)
        md5 = hashlib.md5()
        md5.update(item_str)
        hash_val = md5.hexdigest()
        redis_client.get(hash_val)
        #判断目的去重是否存在rendis中，存在则跳过，不存在则传递下一个
        if redis_client.get(hash_val):
            raise DropItem('已经存在，为你丢掉中')
        else:
            #不存在插入并rendis传递给下一个管道
            redis_client.set(hash_val,item_str)
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
            sql = 'insert into Lianjia (data_title,data_money_mi,data_money_tao) values (%s, %s, %s)'
            cursor.execute(sql,(item['data_title'],item['data_money_mi'],item['data_money_tao']))
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            if cursor:
                cursor.close()
        return item
