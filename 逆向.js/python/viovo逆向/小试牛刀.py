
import requests
import random
import execjs
import json

import time

from lxml import etree
url = 'https://bbs.vivo.com.cn/newbbs/thread/33772816'
headers = {
    'content-type': 'application/json;charset=UTF-8',
}


def get_timestamp():
    timestamp = int(time.time() * 1000)  # 获取13位时间戳
    return timestamp


def get_tamp_str():
    num = int(float(str(random.random() * 10000000)[:10]))  # 获取随机数
    str_ = str(get_timestamp()) + str(num) + '1'  # 获取21位随机数
    return str_


def get_cxt():
    # main.js 扣出来的md5代码，放在这个文件的一个目录即可
    with open("main.js", 'r') as file:  # 打开js文件
        cxt = execjs.compile(file.read())  # 导入js文件
        return cxt


def get_nonce():
    nonce = get_cxt().call('md5', get_tamp_str(), 32)  # 调用js文件md5函数加密，获取nonce
    return nonce


def get_data():
    time.sleep(2)
    data = {
        'imgSpecs': ["t577x324", "t577x4096"],
        'lastId': "",
        'nonce': get_nonce(),
        'pageNum': '3',
        'pageSize': '30',
        'timestamp': get_timestamp(),
    }
    return data

def main():
    res = requests.post(url, headers=headers,
                        data=json.dumps(get_data())).text
    tempRes = json.loads(res)['data']['list']
    list = []
    for data in tempRes:
        # bbsname = data.get('author').get('bbsName')
        # name = data.get('forum').get('name')
        # summary = data.get('summary')
        tid = data.get('tid')
        list.append(tid)
        # title = data.get('title')
        # list.append({
        #     # '标头': title,
        #     # '名字': bbsname,
        #     # '圈子': name,
        #     # '内容': summary,
        #     '详情页链接': tid
        # })
    return list


def dump_josn():
    json_data = main()
    for i in json_data:
        ids = 'https://bbs.vivo.com.cn/newbbs/thread/' + i
        # print(ids)
        url = ids
        payload = {}
        headers = {
            'authority': 'bbs.vivo.com.cn',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': 'Hm_lvt_9ef7debb81babe8b94af7f2c274869fd=1660875333; cookieId=de09f2fb-44be-ba9e-1349-2c38b628b2111660875332728; sessionId=92a893dc-4f34-cfec-9549-4781944cfd5e; Hm_lpvt_9ef7debb81babe8b94af7f2c274869fd=1660876485',
            'if-none-match': '"59f24-y1FpYxBZ9I1Bz6/lZrSuLO1c2k4"',
            'referer': 'https://bbs.vivo.com.cn/newbbs/',
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
        tree = etree.HTML(response)
        if len(tree.xpath('//div[@class="thread-content"]/text()')) != 0:
            title = tree.xpath('//div[@class="thread-content"]/text()')
            title = ''.join(title)
            if len('标题'+title) < 1:
                # print('获取中')
                print('-------________------')
            else:
                print('标题'+title)
        elif len(tree.xpath('//span[@class="title-content"]/text()')) != 0:
            title = tree.xpath('//span[@class="title-content"]/text()')
            title = ''.join(title)
            # print('获取中')
            print('标题'+title)
        else:
            title = '-----_____------'
            print(title)
        if 'common-image' in response:
            if len(tree.xpath('//div[@class="common-image"]/img/@data-src')) != 0:
                pages= tree.xpath('//div[@class="common-image"]/img/@data-src')
                for page in pages:
                    # print('获取中')
                    print(page)

            elif len(tree.xpath('//div[@class="common-image"]/img/@data-src')) != 0:
                pages = tree.xpath('//div[@class="common-image"]/img/@data-src')
                for page in pages:
                    # print('获取中')
                    print(page)
        else:
            print('视频信息，暂未获取到图片')
    # print('已获取完信息！！！！！！！！！！！！！！！！！over！！！！！！！！！！！！')

def penlen():
    json_data = main()
    for id in json_data:
        # print(get_nonce())
        url = "https://bbs.vivo.com.cn/api/community/comment/queryComment"
        timestamp = get_timestamp()
        noce = get_nonce()
        headers = {
            'authority': 'bbs.vivo.com.cn',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'content-type': 'application/json;charset=UTF-8',
            'cookie': 'Hm_lvt_9ef7debb81babe8b94af7f2c274869fd=1660875333; cookieId=de09f2fb-44be-ba9e-1349-2c38b628b2111660875332728; sessionId=92a893dc-4f34-cfec-9549-4781944cfd5e; Hm_lpvt_9ef7debb81babe8b94af7f2c274869fd=1660876485',
            'origin': 'https://bbs.vivo.com.cn',
            'referer': 'https://bbs.vivo.com.cn/newbbs/thread/33776026',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
        }
        payload = '{"tid":'+id+',"pageNum":1,"pageSize":20,"lastId":"","order":2,"timestamp":'+str(timestamp)+',"nonce":"'+str(noce)+'"}'
        response = requests.request("POST", url, headers=headers, data=payload).text
        if '服务器错误'not in response:
            response = json.loads(response)
            data = response['data']['list']
            for i in data:
                if 'fans_name' in i:
                    fans_name = i['fans_name']  # 粉丝网名
                elif 'userName' in i:
                    fans_name = i['userName']
                else:
                    fans_name = '-_-'
                text = i['text']  # 留言信息
                id = i['id']  # 粉丝追评id
                datas = {
                    '粉丝网名': fans_name,
                    '评论信息': text
                }
                print(datas)
        else:
            continue

if __name__ == '__main__':
    dump_josn()
    penlen()