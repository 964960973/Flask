# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DoubanPipeline:
    def process_item(self, item, spider):
        # print(item)
        msg_type = item.get('type')
        download_path = os.getcwd() + '/download'
        if not os.path.exists(download_path):#判断文件或文件夹,如果没有则创建该文件
            os.makedirs(download_path)

        if msg_type == 'img':
            img_name = item['img_name']
            img_bytes = item['img_bytes']
            with open(download_path + '/'+img_name,'wb')as f:
                f.write(img_bytes)
                print('图片保存完成')
        else:
            with open(download_path + '/豆瓣电影top250.csv','a') as f:
                f_csv = csv.DictWriter(f,['img_src','title','new_url','xin_ji','pin_jia','title_opp'])
                f_csv.writerows([item])
                print('保存完毕')
            return item


