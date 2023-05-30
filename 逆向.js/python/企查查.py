import requests
import random
import execjs
import json
import pandas as pd
import time

url = 'https://bbs.vivo.com.cn/api/community/forum/threads'
headers = {
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json;charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4621.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="21", " Not;A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://bbs.vivo.com.cn',
    'referer': 'https://bbs.vivo.com.cn/newbbs/forum/9',
    'cookie': 'cookieId=e1c6727a-9b29-1c13-a417-1b74440b9d521639290997482; KL9d_2132_saltkey=pU2Rr4AV; KL9d_2132_lastvisit=1639287439; Hm_lvt_9ef7debb81babe8b94af7f2c274869fd=1639291140,1639713347; Hm_lvt_a7471116b9007c038d41873ab9121a9e=1639291040,1639713440; sessionId=b6c66b37-b88e-f74d-fa6b-b7e526d5e5f7'
}


def get_timestamp():
    timestamp = int(time.time() * 1000)  # 获取13位时间戳
    return timestamp


def get_str_():
    num = int(float(str(random.random() * 10000000)[:10]))  # 获取随机数
    str_ = str(get_timestamp()) + str(num) + '1'  # 获取21位随机数
    return str_


def get_cxt():
    with open("./1.js") as file:  # 打开js文件
        cxt = execjs.compile(file.read())  # 导入js文件
        return cxt


def get_nonce():
    nonce = get_cxt().call('MD5', get_str_(), '32')  # 调用js文件md5函数加密，获取nonce
    return nonce



def get_data():  # 获取第一页data
    data = {
        'forumId': "9",
        'imgSpecs': ["t577x324", "t577x4096"],
        'lastId': "",
        'nonce': get_nonce(),
        'order': '1',
        'pageNum': '1',
        'pageSize': '1000',
        'timestamp': get_timestamp(),
        'topicId': ""
    }
    return data


def main():
    res = requests.post(url, headers=headers, data=json.dumps(get_data())).text  # 请求第一页数据
    datss = json.loads(res)['data']['list']
    data_list = []
    for data in datss:
        bbsname = data['author']['bbsName']
        name = data['forum']['name']
        summary = data['summary']
        tid = data['tid']
        data_list.append({
            'bbsname': bbsname,
            'name': name,
            'summary': summary,
            'tid': tid
        })
    return data_list


if __name__ == '__main__':
    df = pd.DataFrame(main())
    # df.index = df.index + 1
    print(df)
    df.to_excel('手机圈子0.xlsx')