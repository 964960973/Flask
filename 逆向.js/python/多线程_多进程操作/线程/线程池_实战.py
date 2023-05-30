import json

import requests
import random
import time
from concurrent.futures import ThreadPoolExecutor
import requests
import threading
from lxml import etree
import redis


redis_client = redis.Redis(host='127.0.0.1', port=6379)


def get_image():
    lock = threading.Lock()
    while True:
        try:
            list = []
            lock.acquire()
            url = redis_client.lpop('q').decode("utf-8")
            redis_client.lpush('w',url)
            goods_id = str(time.time())
            lock.release()
            if goods_id not in list:
                list.append(goods_id)
            else:
                print('大件事了')
        except:
            break
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"
        }
        response = requests.get(url, headers=headers).content
        with open(f"D:/p站/{goods_id}.jpg", "wb") as f:
            f.write(response)
            print(f'图片保存成功image ===={goods_id}')



def good_link(url):
    headers = {
        'authority': 'rt.huashi6.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'cookie': 'u_third_platform_source=baidu; auth_tk=NzExM2NhNWNkODE0NDk4NGE2NTFhZjE2MWU5MWQ3NDRMN1hmVw==; hstud=rny0qe1(23042810; _ga=GA1.1.1175863963.1682649453; ab_test=v2021; Hm_lvt_a3e2ff554f3229fd90bcfe77f75b9806=1682649453,1683967937,1684814145,1684823631; Hm_lpvt_a3e2ff554f3229fd90bcfe77f75b9806=1684823638; _ga_Q14GVGCL77=GS1.1.1684823630.13.1.1684823643.0.0.0',
        'origin': 'https://www.huashi6.com',
        'pragma': 'no-cache',
        'referer': 'https://www.huashi6.com/hot',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }
    response = requests.request("GET", url, headers=headers).text
    data = json.loads(response)
    image_data = data['data']['datas']
    for image_src in image_data:
        image_url = 'https://img2.huashi6.com/' + image_src['painter']['coverImageUrl']
        redis_client.lpush('data_list_proxy', image_url)
        print(image_url)
        print(f'插入成功当前页数page==={str(url).split("index=")[1]}')


def ThreadPoolExecutor_1():
    pool = ThreadPoolExecutor(3)
    for page in range(10, 30):
        time_name = str(time.time()).replace('.', '')
        url = f"https://rt.huashi6.com/front/works/hotlist?_ts_={time_name}&index={page}"
        pool.submit(good_link, url)
        print('线程出发了哦')
    pool.shutdown(True)  # 等待线程池中的子线程全部执行完毕
    print('全部执行完毕')

def ThreadPoolExecutor_2():
    pool = ThreadPoolExecutor(20)
    for i in range(1000):
        pool.submit(get_image)

# ThreadPoolExecutor_1()
ThreadPoolExecutor_2()