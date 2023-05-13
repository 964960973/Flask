import time

import requests
import random
from lxml import etree
from sql_help1 import db
hity = str(input('请你输入要获取的城市'))
def sql_table():
    sql = f"""CREATE TABLE 安居客_{hity}_租房 (
         具体链接  varchar(200) ,
         房屋描述  varchar(200),
         房屋大小  varchar(200),
         租金  varchar(200))
         """
    db.create_table(sql)

def get_ip():
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

def get_ajk():
    page = 1
    proxies = get_ip()
    while True:
        url = f"https://{hity}.zu.anjuke.com/fangyuan/p{page}/"
        payload={}
        headers = {
          'authority': 'gz.zu.anjuke.com',
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'accept-language': 'zh-CN,zh;q=0.9',
          'cache-control': 'no-cache',
          # 'cookie': 'aQQ_ajkguid=2CED0DCF-0735-AE3E-CDB2-1C2BC114955D; id58=CrIezWMhMcNub+B4DDsPAg==; sessid=8D27608E-35FB-4467-A991-2E1EC379533D; _ga=GA1.2.1915158803.1663731811; 58tj_uuid=8d9f19c4-d37d-4961-95d3-eed378f37f18; als=0; wmda_uuid=db4677160158c4e14a038bc72bf0c718; wmda_visited_projects=%3B6289197098934; seo_source_type=0; isp=true; new_uv=2; __xsptplus8=8.1.1676619300.1676619596.11%234%7C%7C%7C%7C%7C%23%23Uy1pjANk45w5CaM6rul3XLRluEuphzZ0%23; ctid=12; twe=2; ajk-appVersion=; fzq_h=840592ab426f01e27b8164864c7b41dd_1681284786505_8bcc4feff1e04d299dd560986a3c8ff5_1900284436; obtain_by=2; lps=https%3A%2F%2Fgz.zu.anjuke.com%2F%3Ffrom%3DHomePage_TopBar%7Chttps%3A%2F%2Fguangzhou.anjuke.com%2F; cmctid=3; wmda_session_id_6289197098934=1681284795390-b85d5b5d-ab14-ca4b; xxzl_cid=60871cd99a7c49598d9ce0d8216bcf2b; xxzl_deviceid=33kF4cUsEU4aNmrk+H1p9SKkVHeTAAFgTU5aOaD9snsepPrPjiqAVFi54j8HToGi; aQQ_ajkguid=2CED0DCF-0735-AE3E-CDB2-1C2BC114955D; cmctid=3; ctid=12; seo_source_type=0; sessid=994DA5A0-F1BC-49D2-ADB4-06FF5E697D7B',
          'pragma': 'no-cache',
          'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
          'sec-fetch-dest': 'document',
          'sec-fetch-mode': 'navigate',
          'sec-fetch-site': 'none',
          'sec-fetch-user': '?1',
          'upgrade-insecure-requests': '1',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }
        try:
            response = requests.request("GET", url, headers=headers, data=payload,proxies=proxies)
        except Exception as e:
            proxies = get_ip()
            print("失败：case%s" % e)
            print(response.text)
            continue
        if '请在五分钟内完成验证' in response.text:
            proxies = get_ip()
            print('过验证码中')
            time.sleep(3)
            continue
        tree = etree.HTML(response.text)
        fawu_money = [] #年或月租金
        data_mj = []
        data = tree.xpath('//div[@class="zu-info"]')
        data_list = tree.xpath('//div[@class="zu-info"]/h3/a/@href')#具体链接
        data_miao = tree.xpath('//div[@class="zu-info"]/h3/a/b/text()')#房屋描述
        shi = tree.xpath('//div[@class="zu-info"]/p[1]/b[1]/text()')
        tin = tree.xpath('//div[@class="zu-info"]/p/b[2]/text()')
        m_j = tree.xpath('//div[@class="zu-info"]/p/b[3]/text()')
        for f,k,l in zip(shi,tin,m_j):
            p = str(f) + '室' + str(k) + '厅' + l+'平方'
            data_mj.append(p)
        data_money = tree.xpath('//div[@class="zu-side"]/p/text()')
        data_money_1 = tree.xpath('//div[@class="zu-side"]/p/strong/b/text()')
        for year,money in zip(data_money,data_money_1):
            year_money = money + '_' + year
            fawu_money.append(year_money)
        for q,w,e,r in zip(data_list,data_miao,data_mj,fawu_money):
            gods_url = str(q).split('?')[0]
            db.insert_one(f'insert into 安居客_{hity}_租房 (具体链接,房屋描述,房屋大小,租金) values("{gods_url}","{str(w)}","{str(e)}","{str(r)}");')
            print(f'插入成功url==={url}')
        page += 1
        print(f'当前为{page}页')
        # time.sleep(20)


if __name__ == '__main__':
    sql_table()
    get_ajk()
