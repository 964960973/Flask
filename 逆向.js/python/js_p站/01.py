import threading
import time

import requests
from lxml import etree
import redis

redis_client = redis.Redis(host='127.0.0.1', port=6379)

def get_image_other(url):
    time_name = time.time()
    url = url
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers).content
    except:
        return
    with open(f"D:/p站/{time_name}.jpg","wb") as f:
        f.write(response)
        print('保存成功')

def good_lokin():
  for page in range(1,13):
    url = f"https://www.huashi6.com/rank/month/2022-{page}-01"
    payload = {}
    headers = {
      'authority': 'www.huashi6.com',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'accept-language': 'zh-CN,zh;q=0.9',
      'cache-control': 'no-cache',
      'cookie': 'u_third_platform_source=baidu; auth_tk=NzExM2NhNWNkODE0NDk4NGE2NTFhZjE2MWU5MWQ3NDRMN1hmVw==; hstud=rny0qe1(23042810; _ga=GA1.1.1175863963.1682649453; Hm_lvt_a3e2ff554f3229fd90bcfe77f75b9806=1682649453; Hm_lpvt_a3e2ff554f3229fd90bcfe77f75b9806=1682649575; _ga_Q14GVGCL77=GS1.1.1682649453.1.1.1682649578.0.0.0',
      'pragma': 'no-cache',
      'referer': 'https://www.huashi6.com/',
      'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-user': '?1',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload).text
    tree = etree.HTML(response)
    data = tree.xpath('//a[@class="c-rank-item"]/@href')
    for i in data:
      redis_client.lpush('p_list',i)
    print('插入成功')


def mobie():
    while True:
        url = redis_client.lpop('p_list').decode("utf-8")
        payload = {}
        headers = {
          'authority': 'www.huashi6.com',
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'accept-language': 'zh-CN,zh;q=0.9',
          'cache-control': 'no-cache',
          'cookie': 'u_third_platform_source=baidu; auth_tk=NzExM2NhNWNkODE0NDk4NGE2NTFhZjE2MWU5MWQ3NDRMN1hmVw==; hstud=rny0qe1(23042810; _ga=GA1.1.1175863963.1682649453; Hm_lvt_a3e2ff554f3229fd90bcfe77f75b9806=1682649453; _ga_Q14GVGCL77=GS1.1.1682649453.1.1.1682650116.0.0.0; Hm_lpvt_a3e2ff554f3229fd90bcfe77f75b9806=1682650117',
          'pragma': 'no-cache',
          'referer': 'https://www.huashi6.com/draw/1376607',
          'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
          'sec-fetch-dest': 'document',
          'sec-fetch-mode': 'navigate',
          'sec-fetch-site': 'same-origin',
          'sec-fetch-user': '?1',
          'upgrade-insecure-requests': '1',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }
        response = requests.request("GET", url, headers=headers, data=payload).text
        tree = etree.HTML(response)
        s = tree.xpath('//picture[@class="c-img-loading img-vec"]/img/@data-original')
        for i in s:
            if i == None or i == '':
                continue
            a = 'https:' + i
            get_image_other(a)

def main():
    print(f'主线程开始时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')
    # 初始化3个线程，传递不同的参数
    t1 = threading.Thread(target=mobie)
    t2 = threading.Thread(target=mobie)
    t3 = threading.Thread(target=mobie)
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
    main()