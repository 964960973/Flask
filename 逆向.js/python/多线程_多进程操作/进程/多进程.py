import requests
import threading
from lxml import etree
import multiprocessing

headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cache-Control': 'no-cache',
  'Connection': 'keep-alive',
  'Cookie': 'PHP_SESSION=9c2n2kfh6ooa8dg2s32b3t9r0t; Hm_lvt_9535c3ea6eb286566c2c14dc19269572=1684805253; Hm_lpvt_9535c3ea6eb286566c2c14dc19269572=1684805261',
  'Pragma': 'no-cache',
  'Referer': 'https://www.kepuchina.cn/',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

def task(name,url):
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload).text
    tree = etree.HTML(response)
    title = tree.xpath('//h2[@class="il_text"]/a/text()')
    for i in title:
      print(name + i)


url_list = [('page_1',"https://www.kepuchina.cn/list/listinfo?at_id=AT202111191005438501&page=1"),
            ('page_2', "https://www.kepuchina.cn/list/listinfo?at_id=AT202111191005438501&page=2"),
            ('page_3',"https://www.kepuchina.cn/list/listinfo?at_id=AT202111191005438501&page=3")
            ]
if __name__ == '__main__':
    for name,url in url_list:
        t = multiprocessing.Process(target=task, args=(name,url))
        t.start()
