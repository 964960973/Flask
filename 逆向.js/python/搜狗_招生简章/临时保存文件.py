import threading
import time
import redis
import requests
from lxml import etree
import re
import os
import random
import json
from urllib import parse
from concurrent.futures import ThreadPoolExecutor
UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"

time_year = time.localtime().tm_year
time_mon = time.localtime().tm_mon
time_day = time.localtime().tm_mday
time_name = str(time_year) + '_' + str(time_mon)+"_"+str(time_day)

redis_client = redis.Redis(host='127.0.0.1', port=6379)


def get_ip_1():
  # 提取代理API接口，获取1个代理IP
  api_url = "http://v2.api.juliangip.com/dynamic/getips?num=1&pt=1&result_type=text&split=1&trade_no=1324587523689164&sign=353a9894a22c17ae524f0ae6e412b44c"

  # 获取API接口返回的代理IP
  proxy_ip = requests.get(api_url).text

  # 用户名密码认证(动态代理/独享代理)
  username = "18038573677"
  password = "jti9iyhc"
  proxies = {
    "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
    "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
  }
  return proxies

def get_title(title):
    title = ''.join(str(title)).replace(' ','')
    if '?' in title:
        title = str(title).replace('?','_')
    elif '|' in title:
        title = str(title).replace('|', '_')
    elif '、' in title:
        title = str(title).replace('、', '_')
    elif '/' in title:
        title = str(title).replace('/', '_')
    elif '\\' in title:
        title = str(title).replace('\\', '_')
    elif '<' in title:
        title = str(title).replace('<', '_')
    elif '>' in title:
        title = str(title).replace('>', '_')
    elif ':' in title:
        title = str(title).replace(':', '_')
    elif '“' in title:
        title = str(title).replace('“', '_')
    else:
        title = title
    return title

def loing_index():
    proxies = get_ip_1()
    while True:
        try:
            url_info = redis_client.lpop(f"sou_gou_weix_goods_url_list").decode("utf-8")
        except:
            print('链接已全部跑完')
            print(f'主线程结束时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')
            break
        headers4 = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
            "cache-control": "max-age=0",
            "user-agent": UserAgent
        }
        try:
            response4 = requests.get(url_info, headers=headers4,proxies=proxies)
            if '该内容已被发布者删除' in response4.text:
                print('发布者内容已删除 无法获取')
                continue
            elif response4.status_code != 200:
                print('访问失败')
                continue
        except:
            proxies = get_ip_1()
            time.sleep(3)
            print('代理失效')
            continue
        html = etree.HTML(response4.text)
        try:
            title = html.xpath('//meta[@property="og:title"]/@content')[0]
        except:
            title = '杂乱无章'
        title = get_title(title)
        try:
            wen_ben_text = html.xpath('//div[@class="rich_media"]//text()')
        except:
            print('文本提取出现异常')
            continue
        wen_ben = ''
        timestamp = time.time()  # 获取13位时间戳
        for i in wen_ben_text:
            try:
                wen_ben += ''.join(i).replace(' ','').replace('\n','').split('varfirst_sce')[0]
            except:
                return

        list_length = int(len(['北京','天津', '上海', '重庆','南宁','拉萨','银川','乌鲁木齐','呼和浩特','香港', '澳门','台北','济南', '石家庄', '长春', '哈尔滨', '沈阳', '兰州','太原', '西安', '郑州', '合肥', '南京','杭州', '福州', '广州', '南昌','海口',  '贵阳', '长沙', '武汉', '成都', '昆明',  '西宁']))+1
        math = 1
        for citys in['北京','天津', '上海', '重庆','南宁','拉萨','银川','乌鲁木齐','呼和浩特','香港', '澳门','台北','济南', '石家庄', '长春', '哈尔滨', '沈阳', '兰州','太原', '西安', '郑州', '合肥', '南京','杭州', '福州', '广州', '南昌','海口',  '贵阳', '长沙', '武汉', '成都', '昆明',  '西宁']:
            if citys not in title:
                if math > list_length:
                    with open(f'D:/微信_搜狗/杂乱无章/{time_name}/{title + str(timestamp)}.txt', 'w',encoding='utf-8') as f:
                        f.write(str(title + '\n' + wen_ben + '\n' + url_info))
                        f.close()
                        print(title)
                        break
                else:
                    math += 1
                    continue
            else:
                with open(f'D:/微信_搜狗/{time_name}/{citys}/{title + str(timestamp)}.txt', 'w',encoding='utf-8') as f:
                    f.write(str(title + '\n' + wen_ben + '\n' + url_info))
                    f.close()
                    print(title)
                    break

def main():
    print(f'主线程开始时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')
    # 初始化6个线程，传递不同的参数
    # for i in range(4):
    t1 = threading.Thread(target=loing_index)
    t2 = threading.Thread(target=loing_index)
    t3 = threading.Thread(target=loing_index)
    t4 = threading.Thread(target=loing_index)
    t5 = threading.Thread(target=loing_index)
    # 开启三个线程
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    # 等待运行结束
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    print(f'主线程结束时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')

if __name__ == '__main__':
    main()