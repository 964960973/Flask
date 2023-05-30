# -*- coding: utf-8 -*-
# @Date: 2020/8/14 12:29
# @Author: Ricky Rau

import requests
from lxml import etree
import re
import os
from multiprocessing.dummy import Pool

def main():
    if not os.path.exists('./li_video'):
        os.mkdir('./li_video')     #先创建一个文件夹，用于存储视频
    url = 'https://www.pearvideo.com/category_59'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    dic_list = getDic(url, headers)
    pool = Pool(4)
    pool.map(get_video_data, dic_list)   #使用线程池对视频数据进行请求（主要用于处理较为耗时的阻塞操作）
    pool.close()   #关闭进程池，不再接受新的进程
    pool.join()    #主进程阻塞等待子进程的退出

def getDic(url, headers):
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="listvideoListUl"]/li')
    video_data_list = []   #用来储存视频名称与链接
    for li in li_list:
        video_name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
        detail_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
        detail_text = requests.get(url=detail_url, headers=headers).text
        #此处解析到的源代码（可通过开发者工具中的network进行查看），与一般的网页源代码有所差异，只能使用正则表达式进行匹配
        ex = 'srcUrl="(.*?)",vdoUrl=srcUrl'
        video_url = re.findall(ex, detail_text)[0]
        dic = {
            'video_name': video_name,
            'video_url': video_url
        }
        video_data_list.append(dic)
    return video_data_list

def get_video_data(dic):
    url = dic['video_url']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    #对视频链接发起请求，获取视频的二进制数据
    video_data = requests.get(url=url, headers=headers).content
    #持久化存储操作
    with open('./li_video/' + dic['video_name'], 'wb') as fp:
        fp.write(video_data)
        print(dic['video_name'], '下载完成！')

if __name__ == '__main__':
    main()

