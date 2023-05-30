import json
import requests
import redis
import time
import threading
redis_client = redis.Redis(host='127.0.0.1', port=6379)
def get_ip_1():
    api_url = "http://v2.api.juliangip.com/dynamic/getips?filter=1&num=1&pt=1&result_type=text&split=1&trade_no=1028952470599693&sign=dd32a5f08252819be2e8f6fe24c51396"

    # 获取API接口返回的代理IP
    proxy_ip = requests.get(api_url).text

    # 用户名密码认证(动态代理/独享代理)
    username = "19120940131"
    password = "pgblut9k"
    proxies = {
      "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
      "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
    }
    return proxies

def good_link():
    page = 50
    while True:
        if page <= 60:
            url = "https://rt.huashi6.com/front/works/ai_filter"
            payload = '{\"groupFilters\":[\"\"],\"index\":'+str(page)+',\"size\":40,\"sort\":\"hottest\"}'
            headers = {
                'authority': 'rt.huashi6.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'zh-CN,zh;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json;charset=UTF-8',
                'cookie': 'u_third_platform_source=baidu; auth_tk=NzExM2NhNWNkODE0NDk4NGE2NTFhZjE2MWU5MWQ3NDRMN1hmVw==; hstud=rny0qe1(23042810; _ga=GA1.1.1175863963.1682649453; Hm_lvt_a3e2ff554f3229fd90bcfe77f75b9806=1682649453,1683967937; Hm_lpvt_a3e2ff554f3229fd90bcfe77f75b9806=1683967965; _ga_Q14GVGCL77=GS1.1.1683967936.11.1.1683967973.0.0.0',
                'origin': 'https://www.huashi6.com',
                'pragma': 'no-cache',
                'referer': 'https://www.huashi6.com/ai',
                'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
            }
            proxies = get_ip_1()
            try:
                response = requests.request("POST", url, headers=headers, data=payload,proxies=proxies,timeout=10).text
            except:
                continue
            resp = json.loads(response)['data']['datas']
            for images in resp:
                image = 'https://img2.huashi6.com/' + images['coverImage']['path']
                redis_client.lpush('AI_pzhan',image)
                print(f'保存成功image === {image}')
            page += 1

def get_image():
    while True:
        url = redis_client.lpop('AI_pzhan').decode("utf-8")
        time_name = str(time.time())
        headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"
        }
        response = requests.get(url, headers=headers).content
        with open(f"D:/p站/{time_name}.jpg", "wb") as f:
            f.write(response)
            print(f'图片保存成功image ===={url}')



def main():
    print(f'主线程开始时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')
    # 初始化3个线程，传递不同的参数
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
    main()