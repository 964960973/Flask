import json
import redis
import requests
import threading
from openpyxl import load_workbook
import os
from openpyxl.drawing.image import Image
import time
from lxml import etree
from lxml.doctestcompare import strip

redis_client = redis.Redis(host='127.0.0.1', port=6379)

def get_image():
    while True:
        try:
            ids = time.time()
            try:
                url = redis_client.lpop('image_url_ppp').decode("utf-8")
            except:
                break
            headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"
            }
            response = requests.get(url, headers=headers).content
            with open(f"D:/壁纸/{ids}.jpg", "wb") as f:
                f.write(response)
                print(f'保存成功url==={url}')
        except:
            continue


def get_link():
    for page in range(1,20):
        url = f"https://wallhaven.cc/hot?page={page}"
        payload = {}
        headers = {
            'authority': 'wallhaven.cc',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'cookie': '_pk_id.1.01b8=4e704b19470de582.1676621857.; _pk_ref.1.01b8=%5B%22%22%2C%22%22%2C1676881100%2C%22https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%3A%2F%2Fwallhaven.cc%2F%22%5D; _pk_ses.1.01b8=1; XSRF-TOKEN=eyJpdiI6IlFyZmRlOFhNVStZNE5wdk4yQzZxNmc9PSIsInZhbHVlIjoiU3BDMmI2TkExbHJGblA5VTdwVkFGNzQya3J6dFMxNkJFblNUbkhRbGJaTFlLc1J0cyt2enplTktUOThGTU1BMSIsIm1hYyI6IjUwZjBmZjBlODVkYzliMDM1ZTkyYTkzODQ2ZDI1YTc5MmZlNmUxMGI5OGZmMDM3Nzc5MWNhMmUyN2MzZDEyODUifQ%3D%3D; wallhaven_session=eyJpdiI6IlhIY3laRDVTRjZqVVIzTE5uenNtR3c9PSIsInZhbHVlIjoiQSs3ZjhPODdab2JqMExqMUd1Z0IyeVI1SFA5U3VJWWtIUmhMdmFmQkJyTHlaY2l3UVNoSTY5YUM5YWZ5YVwvYU8iLCJtYWMiOiJkYjEzYTA4MDJjNGQxZjdjNDI2MWU3YjYxMjg3MWJlZjk5YjRlMjdjNmEwYWZiY2IwYWMwZjExNzVlOTJmMTJmIn0%3D; XSRF-TOKEN=eyJpdiI6InB2XC9GazlRYyszWWtxM0dtU2cwXC90Zz09IiwidmFsdWUiOiJsZUE5Tk5Hc3U2bTZsVHRlQ1wvanBSdVYzaDN1UlhaTGdRNEVVZWNTdmJWSXkzcXpMY0k4N25hWDBUVjB2UGdXWCIsIm1hYyI6ImI0YzI4ZGMxZDc0YTRkMDc5ZGNlMzdhZjY0MjJiZjQ2YTYwN2IzMjI4NzljMTBlNDYzYTY4OTEwMGY2ZDgzZjkifQ%3D%3D; wallhaven_session=eyJpdiI6InBvcU1pelJBSitaQkY2ZXRqVEtVemc9PSIsInZhbHVlIjoiZGc4ZDNxa2pWMjRCdmZrWHRWNlVOSTNpKzlHZko3akQxUGdpNXBhY3JiaFpcL1EwMkhUMExqeWZNcWFBNWVFZzIiLCJtYWMiOiJkMTZlOGRlYzczM2FmMDVmZDAxMWU0MTY1OGEyZjQxOGQ5YTJhMTNlYmZkNTIxNzU4NjRjYWM1M2U5NDBhYmZjIn0%3D',
            'pragma': 'no-cache',
            'referer': 'https://wallhaven.cc/hot?page=5',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
        }

        response = requests.request("GET", url, headers=headers, data=payload).text
        tree = etree.HTML(response)
        data = tree.xpath('//img[@class="lazyload"]/@data-src')
        for image in data:
            image_path = str(image).replace('small','full').split('full')[0] .replace('https://th.','https://w.') + 'full/'
            ids = str(image).split('small/')[1].split('/')[0]
            id = str(image).split('small/')[1].split('/')[1]
            image_url = image_path + ids + '/wallhaven-' + id
            print(image_url)
            redis_client.lpush('image_url_ppp',image_url)
def main():
    print(f'主线程开始时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')
    # 初始化3个线程，传递不同的参数
    # for i in range(4):
    t1 = threading.Thread(target=get_image)
    t2 = threading.Thread(target=get_image)
    t3 = threading.Thread(target=get_image)
    # 开启三个线程
    t1.start()
    t2.start()
    t3.start()
    # 等待运行结束
    t1.join()
    t2.join()
    t3.join()
    print(f'主线程结束时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')

if __name__ == '__main__':
    # get_link()
    main()