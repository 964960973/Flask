import json
import random
import base64
import time

import requests

# 获取动态变化且加密的x-apiKey
def get_x_apikey():
    # API_KEY固定字符串
    API_KEY = "a2c903cc-b31e-4547-9299-b6d07b7631ab"
    Key1 = API_KEY[0:8]
    Key2 = API_KEY[8:]
    #  交换API_KEY部分内容
    new_Key = Key2 + Key1
    # 获取当前时间，毫秒级
    cur_time = round(time.time() * 1000)
    # 处理获得的时间
    new_time = str(1 * cur_time + 1111111111111)
    # 生成三个0-9的随机整数
    random1 = str(random.randint(0, 9))
    random2 = str(random.randint(0, 9))
    random3 = str(random.randint(0, 9))
    # 再次处理时间字符串
    cur_time = new_time + random1 + random2 + random3
    # 将包含API_KEY和时间串的内容合并
    this_Key = new_Key + '|' + cur_time
    # 转码
    n_k = this_Key.encode('utf-8')
    # base64加秘
    x_apiKey = base64.b64encode(n_k)
    # 将加密后的x_apiKey返回
    return str(x_apiKey, encoding='utf8')

def login():
    limit = 1  +  int(input('输入你要展示多少条数据'))
    timestamp = int(time.time() * 1000)  # 获取13位时间戳
    apiKey = get_x_apikey()
    url = "https://www.oklink.com/api/explorer/v1/btc/transactionsNoRestrict?t={}&limit={}&offset=0".format(timestamp,str(limit))
    payload = {}
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'zh-CN',
        'App-Type': 'web',
        'Connection': 'keep-alive',
        'Cookie': 'aliyungf_tc=9b3140a3a51da6a948e4f1e6b538d2e6462854f0ca1495f3a9d1bf51162b5853; locale=zh_CN; _okcoin_legal_currency=CNY; first_ref=https%3A%2F%2Flink.csdn.net%2F%3Ftarget%3Dhttps%253A%252F%252Fwww.oklink.com%252Fbtc%252Ftx-list; Hm_lvt_5244adb4ce18f1d626ffc94627dd9fd7=1661233798; Hm_lpvt_5244adb4ce18f1d626ffc94627dd9fd7=1661233821',
        'Referer': 'https://www.oklink.com/zh-cn/btc/tx-list?limit=20&pageNum=1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'devId': '346a57fe-f799-4fcc-b9ef-f298e27e9466',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-apiKey': apiKey,
        'x-cdn': 'https://static.oklink.com',
        'x-utc': '8'
    }
    urls = []
    response = requests.request("GET", url, headers=headers, data=payload).text
    json_data = json.loads(response)
    list_json = json_data['data']['hits']
    for kk in list_json:
        l = kk['hash']
        url = 'https://www.oklink.com/zh-cn/btc/tx/'+ l
        urls.append(url)
    # print(urls)
    return urls
def index():
    timestamp = int(time.time() * 1000)  # 获取13位时间戳
    urls = login()
    apiKey = get_x_apikey()
    for url in urls:
        url_s = url + '?'+ str(timestamp)
        payload = {}
        headers = {
            'Accept': 'application/json',
            'Accept-Language': 'zh-CN',
            'App-Type': 'web',
            'Connection': 'keep-alive',
            'Cookie': 'aliyungf_tc=9b3140a3a51da6a948e4f1e6b538d2e6462854f0ca1495f3a9d1bf51162b5853; locale=zh_CN; _okcoin_legal_currency=CNY; first_ref=https%3A%2F%2Flink.csdn.net%2F%3Ftarget%3Dhttps%253A%252F%252Fwww.oklink.com%252Fbtc%252Ftx-list; Hm_lvt_5244adb4ce18f1d626ffc94627dd9fd7=1661233798; Hm_lpvt_5244adb4ce18f1d626ffc94627dd9fd7=1661235388',
            'Referer': 'https://www.oklink.com/zh-cn/btc/tx/23fdd9abdbabfd8b196ac6c90cf811759f4f48e97508fce2824877f1e86e2412',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'devId': '346a57fe-f799-4fcc-b9ef-f298e27e9466',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'x-apiKey': apiKey,
            'x-cdn': 'https://static.oklink.com',
            'x-utc': '8'
        }

        response = requests.request("GET", url_s, headers=headers, data=payload).text
        json_data = json.loads(response)
        json_list = json_data['data']
        for i in json_list:
            blockHeight = i['blockHeight']
            inputsValue = i['inputsValue'] + 'BTC'
            outputsValue = i['outputsValue'] + 'BTC'
            weight = i['weight']
            data = {
                '块高度':blockHeight,
                '输入':inputsValue,
                '输出':outputsValue,
                '交易重量':weight
            }
        print(data)



if __name__ == '__main__':
    index()