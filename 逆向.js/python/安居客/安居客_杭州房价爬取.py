import os
import time
import json
import redis
import requests
import threading
from lxml import etree
from openpyxl import load_workbook
from lxml.doctestcompare import strip
from openpyxl.drawing.image import Image

redis_client = redis.Redis(host='127.0.0.1', port=6379)

headers = {
    'authority': 'hz.fang.anjuke.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'isp=true; isp=true; aQQ_ajkguid=2CED0DCF-0735-AE3E-CDB2-1C2BC114955D; id58=CrIezWMhMcNub+B4DDsPAg==; sessid=8D27608E-35FB-4467-A991-2E1EC379533D; ajk-appVersion=; _ga=GA1.2.1915158803.1663731811; 58tj_uuid=8d9f19c4-d37d-4961-95d3-eed378f37f18; als=0; seo_source_type=0; obtain_by=2; twe=2; ctid=18; lps=https%3A%2F%2Fhz.zu.anjuke.com%2F%3Ffrom%3DHomePage_TopBar%7Chttps%3A%2F%2Fhangzhou.anjuke.com%2F; cmctid=79; fzq_h=f2f9d4dde06d685fb6b69e6c09a0e423_1676617986329_19439dfb4093439bb09b2d00e67c4e91_1900291817; isp=true; isp=true; wmda_uuid=81ad20fd0c7394a325be1fcd2e9361f2; wmda_new_uuid=1; wmda_session_id_8788302075828=1676617992587-3aa4dc4a-8515-d841; wmda_visited_projects=%3B8788302075828; init_refer=https%253A%252F%252Fhangzhou.anjuke.com%252F; new_uv=2; new_session=0; ajk_member_id=254466887; ajk_member_verify=PskhGWumGXXGpoo5YNrPEEPMwcAOlhwbDJef1WqFS9g%3D; ajk_member_verify2=MjU0NDY2ODg3fFdSZ3hrVlF8MQ%3D%3D; ajkAuthTicket=TT=047552f212c04063fa71b13b39645bf2&TS=1676618183086&PBODY=c5KVcg70ypxI4TFP4l-mlcNgv-bs7AcmrIr0UQYdKGwKMltTS9p05Dzu8gjKDK7ulE7iOrX4G6asfeHvhjO47vFSUoxYV1zHcmP5ipTFEzSbiA_hq-wDHhm0vnU7lBLhKvXOs18khm370MRCIV6jrKCCh5iaYDCNTsCArCA4q5g&VER=2&CUID=XWOIf9ZlZpbacRRfXr1vL6S2r3T3qS61; xxzl_cid=23f60213b548494b99d2d6ac6b3e6185; xxzl_deviceid=o1QM5Jo0AVfLlLe4GfiUeVz/3/EbxVpcpgp4Dr+KzthZI60nRCrldIKrIrrV8/LJ; aQQ_ajkguid=2CED0DCF-0735-AE3E-CDB2-1C2BC114955D; ajkAuthTicket=TT=047552f212c04063fa71b13b39645bf2&TS=1676618195835&PBODY=FW4nIppGg-C8dSuIfj3qkoVkknfuELpzLUQa8z0n6eRCTx_NE5pmU0KBTpgM3SGLfAvrhTgKADhsas4ECMYFVdEq7Ea5rujGFsDGlg5P8DNAYNKSBET-sVMp249JOAx9axTSZ4zHTfviLYJz6yXjy1w3loEq_ow2SBzEng79IMA&VER=2&CUID=XWOIf9ZlZpbacRRfXr1vL6S2r3T3qS61; cmctid=79; ctid=18; seo_source_type=0; sessid=994DA5A0-F1BC-49D2-ADB4-06FF5E697D7B',
    'pragma': 'no-cache',
    'referer': 'https://hz.fang.anjuke.com/loupan/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

def get_link():
    for page in range(1,2):
        url = f'https://hz.sydc.anjuke.com/xzl-zu/p{page}/'
        payload = {}
        time.sleep(2)
        response = requests.request("GET", url, headers=headers, data=payload).text
        tree = etree.HTML(response)
        get_urls = tree.xpath('//div[@class="list-item"]/a/@href')
        for get_url in get_urls:
            redis_client.lpush('hz_fang',get_url)
            print(f'存储成功url===={get_urls}')


def good_link():
    while True:
        try:
            url = redis_client.lpop('hz_fang').decode("utf-8")
        except:
            print('链接已经采集完毕,终止程序')
            break
