import random
import threading
import time
import execjs
import requests
import redis
import re
from lxml import etree
from io import BytesIO
from fontTools.ttLib import TTFont
from sql_db import db

redis_client = redis.Redis(host='127.0.0.1', port=6379)


def maoyan_id():
    with open(r"./main.js", encoding='utf-8', errors='ignore') as f:
        ctx = execjs.compile(f.read())
    info = ctx.call('get_key')
    return info


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': '__mta=151755398.1683273129571.1683359663689.1683359887982.79; uuid_n_v=v1; uuid=BC799DB0EB1911EDB1C0EF0226805F3B23594ED5F6C74B6DB5D151ABC03E86F2; _csrf=caba64482463c5f33e0fc1e183fd7615caf448d686c0c414a88001adb939102c; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=187eae59ddcc8-063a1eabab45d3-26031b51-1fa400-187eae59ddcc8; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1683273129; __mta=151755398.1683273129571.1683359230978.1683359663689.78; _lxsdk=BC799DB0EB1911EDB1C0EF0226805F3B23594ED5F6C74B6DB5D151ABC03E86F2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1683359888; _lxsdk_s=187efc06016-add-e69-729%7C%7C41',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}


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


def good_oser():
    page = 150
    proxies = get_ip()
    while True:
        if page >= 1800:
            break
        url = f"https://www.maoyan.com/films?showType=3&offset={page}"
        payload = {}
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Cookie': '__mta=151755398.1683273129571.1683366685626.1683366776121.103; uuid_n_v=v1; uuid=BC799DB0EB1911EDB1C0EF0226805F3B23594ED5F6C74B6DB5D151ABC03E86F2; _csrf=caba64482463c5f33e0fc1e183fd7615caf448d686c0c414a88001adb939102c; _lxsdk_cuid=187eae59ddcc8-063a1eabab45d3-26031b51-1fa400-187eae59ddcc8; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1683273129; WEBDFPID=yzwx7y24yx4x5w57y909zuw9xv21x7x1812u960y8u497958z709v517-1998722525812-1683362524981MOEEKSUfd79fef3d01d5e9aadc18ccd4d0c95071848; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk=BC799DB0EB1911EDB1C0EF0226805F3B23594ED5F6C74B6DB5D151ABC03E86F2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1683509026; __mta=151755398.1683273129571.1683366776121.1683509025836.104; _lxsdk_s=187f8f4601f-50f-8ba-375%7C%7C10',
            'Pragma': 'no-cache',
            'Referer': 'https://www.maoyan.com/films?showType=3&offset=120',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }
        data = {}
        response = requests.request("GET", url, headers=headers, data=payload, proxies=proxies,timeout=10)
        if response.status_code != 200:  # 打印状态码
            proxies = get_ip()
            print(f'出现验证码请前往验证url==={url}')
            continue
        tree = etree.HTML(response.text)
        data_list_url = tree.xpath('//div[@class="channel-detail movie-item-title"]/a/@href')
        # data_list_title = tree.xpath('//div[@class="channel-detail movie-item-title"]/a/text()')
        for data_url in data_list_url:
            if redis_client.hget(f"mao_yan_tv_hget", data_url) == None:
                print(f"开始采集电影链接 goods_id== {data_url},当前网页 == {url}")
                redis_client.lpush(f"mao_yan_tv_list", data_url)
                redis_client.hset(f"mao_yan_tv_hget", data_url, "1")
            else:
                print(f"该电影已经采集过了 goods_url== {data_url},当前网页 == {url}")
                continue
        page += 30


def Font_Reverse(response, proxies):
    try:
        fount_url = 'https:' + ''.join(re.findall('format\("embedded-opentype"\),url\("(.*?)"\);}', response)[0])
        font_data = requests.get(url=fount_url, headers=headers, proxies=proxies).content
        # with open('demo.woff', 'wb') as f:
        #     f.write(font_data)
        # font = TTFont('demo.woff').saveXML('demo.xml')
        font = TTFont(BytesIO(font_data))
        # print(font.getGlyphNames()[1:-1])
        keys = font.getGlyphNames()[1:-1]
        xxx = []
        for i in keys:
            x_y = list(font['glyf'][i].coordinates)
            xxx.append((i, (x_y[-1][0] - x_y[0][0])))
        xxx.sort(key=lambda x: x[1])
        yyy = [2, 6, 4, 5, 3, 8, 1, 0, 9, 7]
        zzz = {}
        for m, n in enumerate(xxx):
            name = '&#x' + n[0][3:].lower() + ';'
            zzz[name] = yyy[m]
        data = response
        for m, n in zzz.items():
            data = data.replace(m, str(n))
            # print(m, str(n))
        return data
    except:
        return '出错了'


def good_link():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': '__mta=151755398.1683273129571.1683359663689.1683359887982.79; uuid_n_v=v1; uuid=BC799DB0EB1911EDB1C0EF0226805F3B23594ED5F6C74B6DB5D151ABC03E86F2; _csrf=caba64482463c5f33e0fc1e183fd7615caf448d686c0c414a88001adb939102c; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=187eae59ddcc8-063a1eabab45d3-26031b51-1fa400-187eae59ddcc8; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1683273129; __mta=151755398.1683273129571.1683359230978.1683359663689.78; _lxsdk=BC799DB0EB1911EDB1C0EF0226805F3B23594ED5F6C74B6DB5D151ABC03E86F2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1683359888; _lxsdk_s=187efc06016-add-e69-729%7C%7C41',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }
    proxies = get_ip()
    while True:
        try:
            old_id = redis_client.lpop('mao_yan_tv_list').decode("utf-8")
        except:
            break
        info = maoyan_id()
        timeStamp = info['timeStamp']
        index = info['index']
        signKey = info['signKey']
        # url = 'https://www.maoyan.com/ajax/films/175?timeStamp=1683363132214&index=6&signKey=5550532c8f82303657741dd1d3e8c1bc&channelId=40011&sVersion=1&webdriver=false'
        url = f"https://www.maoyan.com/ajax{str(old_id)}?timeStamp={timeStamp}&index={index}&signKey={signKey}&channelId=40011&sVersion=1&webdriver=false"
        payload = {}
        try:
            response = requests.request("GET", url, headers=headers, data=payload, proxies=proxies)
            if response.status_code != 200:  # 打印状态码
                proxies = get_ip()
                print(f'出现验证码请前往验证url==={url}')
                continue
        except:
            redis_client.rpush('mao_yan_tv_list', old_id)
            continue
        data_response = Font_Reverse(response.text, proxies)
        if data_response != '出错了':
            tree = etree.HTML(data_response)
            ellipsis = ''
            try:
                TV_id = str(old_id).split('films/')[1]  # 电影ID
                tittle_name = tree.xpath('//h1[@class="name"]/text()')[0]  # 电影名称
                try:
                    ellipsies = tree.xpath('//div[@class="movie-brief-container"]/ul/li[1]/a/text()')  # 电影类别
                    for ellipsi in ellipsies:
                        if ellipsi == '':
                            continue
                        ellipsis = ellipsis + ellipsi
                except:
                    ellipsis = '暂无数据'
                try:
                    qitu_shichang = tree.xpath('//div[@class="movie-brief-container"]/ul/li[2]/text()')  # 出版地区
                    regions = str(qitu_shichang[0]).split('/')[0].strip()
                    tv_time = str(qitu_shichang[0]).split('/')[1].strip()
                except:
                    regions = '暂无数据'
                    tv_time = '暂无数据'
                try:
                    ellipsis_time = tree.xpath('//div[@class="movie-brief-container"]/ul/li[3]/text()')  # 上映时间
                except:
                    ellipsis_time = '暂无数据'
                try:
                    pin_fen = str(
                        tree.xpath('//div[@class="movie-index-content score normal-score"]/span/span/text()')[0]) + str(
                        tree.xpath('//div[@class="movie-index-content box"]/span[2]/text()')[0])  # 电影评分,满分10分
                except:
                    pin_fen = '暂无数据'
                try:
                    box_piao = str(tree.xpath('//div[@class="movie-index-content box"]/span[1]/text()')[0]) + str(
                        tree.xpath('//div[@class="movie-index-content box"]/span[2]/text()')[0])  # 已出售票房
                except:
                    box_piao = '暂无数据'
                jain_jie = tree.xpath('//span[@class="dra"]/text()')[0]  # 电影简介
                if len(jain_jie) > 900:
                    jain_jie = jain_jie[:800]
                db.insert_one(f'insert into 猫眼电影 (电影id,电影名称,电影类别,出版地区,电影时长,上映时间,电影评分,已售票房,电影简介) values("{str(TV_id)}","{str(tittle_name)}","{str(ellipsis)}","{str(regions)}","{str(tv_time)}","{str(ellipsis_time)}","{str(pin_fen)}","{str(box_piao)}","{str(jain_jie)}");')
                print('插入成功')
            except:
                redis_client.rpush('mao_yan_tv_list', old_id)
                print(f'url==={url},匹配有误')
                continue

        else:
            redis_client.rpush('mao_yan_tv_list', old_id)
            continue


def main():
    print(f'主线程开始时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')
    # 初始化3个线程，传递不同的参数
    t1 = threading.Thread(target=good_link)
    t2 = threading.Thread(target=good_link)
    t3 = threading.Thread(target=good_link)
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
    # good_oser()
    # main()
    good_link()
