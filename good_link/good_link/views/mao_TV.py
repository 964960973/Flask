from ..Miao_sql import db
from flask import Blueprint, session, redirect, url_for, render_template, request
import requests
import execjs
import redis
import re
from lxml import etree
from io import BytesIO
from fontTools.ttLib import TTFont

MiAo = Blueprint('Miao', __name__)

redis_client = redis.Redis(host='127.0.0.1', port=6379)


def maoyan_id():
    with open(r"./good_link/js逆向/猫眼.js", encoding="utf-8") as f:
        ctx = execjs.compile(f.read())
    info = ctx.call('get_key')
    return info



def sql_table(id):
    sql = f"""CREATE TABLE 猫眼_{id} (
         热门评论  varchar(2000) ,
         评论名称  varchar(200) ,
         评论头像  varchar(200) ,
         点赞人数  varchar(200))
         """
    db.tables(sql)


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


def good_link(PlId):
    sql_table(PlId)
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
    old_id = '/films/' + str(PlId)
    proxies = get_ip()
    info = maoyan_id()
    timeStamp = info['timeStamp']
    index = info['index']
    signKey = info['signKey']
    url = f"https://www.maoyan.com/ajax{str(old_id)}?timeStamp={timeStamp}&index={index}&signKey={signKey}&channelId=40011&sVersion=1&webdriver=false"
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload, proxies=proxies)
    data_response = Font_Reverse(response.text, proxies)
    if data_response != '出错了':
        tree = etree.HTML(data_response)
        pin_len_text_list = tree.xpath('//div[@class="comment-content"]/text()')
        pin_len_name_list = tree.xpath('//div[@class="user"]/span[1]/text()')
        pin_len_img_list = tree.xpath('//div[@class="portrait-container"]/div/img/@src')
        pin_len_math_list = tree.xpath('//div[@class="approve "]/span/text()')
        for pin_len_text,pin_len_name,pin_len_img,pin_len_math in zip(pin_len_text_list,pin_len_name_list,pin_len_img_list,pin_len_math_list):
            try:
                pin_len_img = str(pin_len_img).split('@')[0]
            except:
                pin_len_img = pin_len_img
            db.insert_one(f'insert into 猫眼_{PlId} (热门评论,评论名称,评论头像,点赞人数) values("{str(pin_len_text)}","{str(pin_len_name)}","{str(pin_len_img)}","{str(pin_len_math)}");')
            print('插入成功')


@MiAo.route('/miao', methods=["GET", "POST"])
def Miao():
    jobs = db.fetchall('select * from 猫眼电影')
    return render_template('./MiaoKey/demo.html', jobs=jobs)

@MiAo.route('/Miao_pl', methods=["GET", "POST"])
def Miao_pl():
    PlId = str(request.args.get('plxt'))
    try:
        datas = db.fetchall(f'select * from 猫眼_{PlId}')
    except:
        good_link(PlId)
    finally:
        datas = db.fetchall(f'select * from 猫眼_{PlId}')
    return render_template('./MiaoKey/Miao_pl.html', datas=datas)

