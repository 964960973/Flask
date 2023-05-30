import requests
import re
from lxml import etree
url = 'https://mp.weixin.qq.com/s?src=11&timestamp=1677726149&ver=4381&signature=fj5ifF68uw6kmGeph9vY4IeL6plA*ck4yCiAjqKlVybiscWM-VQ7nKh5eAHXgsBEIHLxftU3pSIrX0js2kLuEpk1Up1l*OIczhoWCsRBGwwT0FmqRPebCQaDXm*BuPB7&new=1'
headers4 = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "max-age=0",
    "user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
response4 = requests.get(url, headers=headers4)
html = etree.HTML(response4.text)
print(response4.status_code)
print(html.xpath('//meta[@property="og:title"]/@content')[0])
a = html.xpath('//span[@class="profile_meta_value"]/text()')
