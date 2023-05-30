import requests
import requests
from lxml import etree
import json
import time

import pymongo
import requests

from chaojiying import Chaojiying_Client

# requests.packages.urllib3.disable_warnings()

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



def get_uuid():
    proxies = get_ip_1()
    for page in range(1,10):
        url = f"https://weixin.sogou.com/weixin?ie=utf8&s_from=input&_sug_=n&_sug_type_=&type=2&query=%E5%B9%BF%E5%B7%9E%E6%8B%9B%E7%94%9F%E7%AE%80%E7%AB%A0&page={page}&ie=utf8"
        payload = {}
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Cookie': 'IPLOC=CN4401; SUID=992744717810870A0000000063FDB34C; SNUID=6EDFBC89F7FD02451E3970B7F8677547; SUV=00C3E8BF7144279963FDB357994F3017; cuid=AAFdWKNNQwAAAAqHS0+44gAASQU=; browerV=3; osV=1; ssuid=7748218330; sw_uuid=7717224448; ariaDefaultTheme=default; ariaFixed=true; ariaReadtype=1; ariaStatus=false; ABTEST=0|1677649323|v17; sst0=956; ld=1kllllllll20@bnqlllllp5MiCyllllltUyXuyllll7llllllylll5@@@@@@@@@@; ld=Mlllllllll20@bnqlllllp5@lBollllltUyXuyllllZllllllylll5@@@@@@@@@@',
            'Pragma': 'no-cache',
            'Referer': 'https://www.sogou.com/sogou?query=%E6%9D%AD%E5%B7%9E%E6%8B%9B%E7%94%9F%E7%AE%80%E7%AB%A0',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }
        resp = requests.get(url, headers=headers, allow_redirects=False,proxies=proxies).text
        tree = etree.HTML(resp)
        good_id = tree.xpath('//a[@target="_blank"]/@href')
        for url in good_id:
            if 'link' not in url:
                continue
            urrls = 'https://weixin.sogou.com' + url
            print(urrls)



get_uuid()