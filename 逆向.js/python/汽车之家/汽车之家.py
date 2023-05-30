import time
import json

import requests
from lxml import etree

for i in range(1,10):
  page = i
name = '可可西里' #城市名
timestamp = int(time.time() * 1000)
def index():
  url = "https://you.autohome.com.cn/summary/getsearchresultlist?ps=20&pg={}&q={},9&_={}".format(page,name,timestamp)
  payload={}
  headers = {
    'authority': 'you.autohome.com.cn',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'sessionip=113.68.39.215; sessionid=0C5AFB62-0399-45DE-9CF7-4C35280E6078%7C%7C2022-08-22+14%3A44%3A35.626%7C%7Cwww.baidu.com; autoid=761098905d0dec6ca037fa4706f04c26; sessionvid=B6C70CE1-2088-4210-95CB-05CED5C688E1; area=440111; v_no=5; visit_info_ad=0C5AFB62-0399-45DE-9CF7-4C35280E6078||B6C70CE1-2088-4210-95CB-05CED5C688E1||-1||-1||5; ref=www.baidu.com%7C0%7C0%7C0%7C2022-08-22+14%3A45%3A11.202%7C2022-08-22+14%3A44%3A35.626; JSESSIONID=C3477F0BF90354010C84F9DAB1040357',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
  } #伪装信息
  urls = []
  response = requests.request("GET", url, headers=headers, data=payload).text
  data_json = json.loads(response)
  data_list = data_json['result']['hitlist']
  for i in data_list:
    url = i['url']
    urls.append(url)
  return urls

def login():
  urls = index()
  for i in urls:
    try:
      page_s = []
      url = 'https://you.autohome.com.cn'+i
      payload = {}
      headers = {
        'authority': 'you.autohome.com.cn',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'sessionip=113.68.39.215; sessionid=0C5AFB62-0399-45DE-9CF7-4C35280E6078%7C%7C2022-08-22+14%3A44%3A35.626%7C%7Cwww.baidu.com; autoid=761098905d0dec6ca037fa4706f04c26; sessionvid=B6C70CE1-2088-4210-95CB-05CED5C688E1; area=440111; JSESSIONID=1D7952E84B9D8BFCDFAD5B80D695FCCB; v_no=19; visit_info_ad=0C5AFB62-0399-45DE-9CF7-4C35280E6078||B6C70CE1-2088-4210-95CB-05CED5C688E1||-1||-1||19; ref=www.baidu.com%7C0%7C0%7C0%7C2022-08-22+15%3A01%3A30.031%7C2022-08-22+14%3A44%3A35.626',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
      }
      response = requests.request("GET", url, headers=headers, data=payload).text
      data_xpath = etree.HTML(response)
      data = data_xpath.xpath('//img[@class="detail-responsive lazy-load min3 lazyload"]/@data-original')
      for jpg_url in data:
        if 'x0_1_autohomecar__'in jpg_url:
          page = jpg_url.split('x0_1_autohomecar__')[0]
          a = jpg_url.split('x0_1_autohomecar__')[1]
          s = page.split('/')[-1]
          pages = page.replace(s, a)
          # print(pages)
          page_s.append(pages)
        else:
          print('出现问题' +jpg_url)
      text = data_xpath.xpath('//h4[@class="item-title fl"]/span/text()')
      for i in text:
        print(i)
      data_item = data_xpath.xpath('//div[@class="journey-content"]/p/text()')
      str(data_item).replace('\\xa0\\','')
      print(data_item)
      return page_s
    except:
      print('*' * 100)
      continue
def with_open():
    url = login()
    for i in url:
      headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"
      }
      timestamp = int(time.time() * 1000)
      response = requests.get(i, headers=headers).content
      with open(f"E://汽车之家/{timestamp}.jpg", "wb") as f:
        print('保存中')
        f.write(response)
        print('保存完毕' + i )

if __name__ == '__main__':
    with_open()