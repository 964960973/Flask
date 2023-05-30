import threading
import time
import redis
import requests
from lxml import etree
import re
import os
import random
import json
from urllib import parse
from concurrent.futures import ThreadPoolExecutor

time_year = time.localtime().tm_year
time_mon = time.localtime().tm_mon
time_day = time.localtime().tm_mday
time_name = str(time_year) + '_' + str(time_mon)+"_"+str(time_day)

redis_client = redis.Redis(host='127.0.0.1', port=6379)

UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"

def get_mkdir():
    os.mkdir(f'D:/微信_搜狗/{time_name}')
    for name in ['北京', '天津', '上海', '重庆', '南宁', '拉萨', '银川', '乌鲁木齐', '呼和浩特', '香港', '澳门', '台北', '济南', '石家庄', '长春', '哈尔滨',
                 '沈阳', '兰州', '太原', '西安', '郑州', '合肥', '南京', '杭州', '福州', '广州', '南昌', '海口', '贵阳', '长沙', '武汉', '成都', '昆明',
                 '西宁','杂乱无章']:
        os.mkdir(f'D:/微信_搜狗/{time_name}/{name}')
        print('全部创建完毕')

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

def get_k_h(url):
    b = int(random.random() * 100) + 1
    a = url.find("url=")
    url = url + "&k=" + str(b) + "&h=" + url[a + 4 + 21 + b: a + 4 + 21 + b + 1]
    return url

def get_cookie(response1, uigs_para, UserAgent,proxies):
    SetCookie = response1.headers['Set-Cookie']
    cookie_params = {
        "ABTEST": str(SetCookie).split('ABTEST=')[1].split(';')[0],
        "SNUID": str(SetCookie).split('SNUID=')[1].split(';')[0],
        "IPLOC": str(SetCookie).split('IPLOC=')[1].split(';')[0],
        "SUID": str(SetCookie).split('SUID=')[1].split(';')[0],
    }

    url = "https://www.sogou.com/sug/css/m3.min.v.7.css"
    headers = {
        "Accept": "text/css,*/*;q=0.1",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Cookie": "SNUID={}; IPLOC={}".format(cookie_params['SNUID'], cookie_params['IPLOC']),
        "Host": "www.sogou.com",
        "Referer": "https://weixin.sogou.com/",
        "User-Agent": UserAgent
    }
    response2 = requests.get(url, headers=headers,proxies=proxies)
    SetCookie = response2.headers['Set-Cookie']
    cookie_params['SUID'] = str(SetCookie).split('SUID=')[1].split(';')[0]

    url = "https://weixin.sogou.com/websearch/wexinurlenc_sogou_profile.jsp"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Cookie": "ABTEST={}; SNUID={}; IPLOC={}; SUID={}".format(cookie_params['ABTEST'], cookie_params['SNUID'],
                                                                  cookie_params['IPLOC'],
                                                                  cookie_params['SUID']),
        "Host": "weixin.sogou.com",
        "Referer": response1.url,
        "User-Agent": UserAgent
    }
    response3 = requests.get(url, headers=headers,proxies=proxies)
    SetCookie = response3.headers['Set-Cookie']
    cookie_params['JSESSIONID'] = str(SetCookie).split('JSESSIONID=')[1].split(';')[0]

    url = "https://pb.sogou.com/pv.gif"
    headers = {
        "Accept": "image/webp,*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Cookie": "SNUID={}; IPLOC={}; SUID={}".format(cookie_params['SNUID'], cookie_params['IPLOC'],
                                                       cookie_params['SUID']),
        "Host": "pb.sogou.com",
        "Referer": "https://weixin.sogou.com/",
        "User-Agent": UserAgent
    }
    response4 = requests.get(url, headers=headers, params=uigs_para,proxies=proxies)
    SetCookie = response4.headers['Set-Cookie']
    cookie_params['SUV'] = str(SetCookie).split('SUV=')[1].split(';')[0]

    return cookie_params

def get_para(response):
    uigs_para = re.findall('var uigs_para = (.*?);', response.text, re.S)[0]
    if 'passportUserId ? "1" : "0"' in uigs_para:
        uigs_para = uigs_para.replace('passportUserId ? "1" : "0"', '0')
    uigs_para = json.loads(uigs_para)
    exp_id = re.findall('uigs_para.exp_id = "(.*?)";', response.text, re.S)[0]
    uigs_para['right'] = 'right0_0'
    uigs_para['exp_id'] = exp_id[:-1]
    return uigs_para

def get_title(title):
    title = ''.join(str(title)).replace(' ','')
    if '?' in title:
        title = str(title).replace('?','_')
    elif '|' in title:
        title = str(title).replace('|', '_')
    elif '、' in title:
        title = str(title).replace('、', '_')
    elif '/' in title:
        title = str(title).replace('/', '_')
    elif '\\' in title:
        title = str(title).replace('\\', '_')
    elif '<' in title:
        title = str(title).replace('<', '_')
    elif '>' in title:
        title = str(title).replace('>', '_')
    elif ':' in title:
        title = str(title).replace(':', '_')
    elif '“' in title:
        title = str(title).replace('“', '_')
    else:
        title = title
    return title

def main_v4():
    try:
        name_list = ['北京', '天津', '上海', '重庆', '南宁', '拉萨', '银川', '乌鲁木齐', '呼和浩特', '香港', '澳门', '台北', '济南', '石家庄', '长春', '哈尔滨',
                     '沈阳', '兰州', '太原', '西安', '郑州', '合肥', '南京', '杭州', '福州', '广州', '南昌', '海口', '贵阳', '长沙', '武汉', '成都', '昆明',
                     '西宁']
        for name in name_list:
            # proxies = get_ip_1()
            for page in range(1,11):
                goods_url = 'https://weixin.sogou.com/weixin?type=2&s_from=input&query=%E5%8C%97%E4%BA%AC%E6%8B%9B%E7%94%9F%E7%AE%80%E7%AB%A0&_sug_=n&_sug_type_=&page=9' # 转变字符串进行编码改写+页数
                headers1 = {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Host": "weixin.sogou.com",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": UserAgent,
                }
                proxies = get_ip_1()
                response1 = requests.get(goods_url, headers=headers1,proxies=proxies)
                time.sleep(0.5)
                if '我们的系统检测到您网络中存在异常访问请求' in response1.text:
                    print('代理失效')
                    time.sleep(1)
                    proxies = get_ip_1()
                    redis_client.lpush('url_get_info_sougo',goods_url)
                    print(f'存储失败进入此数据最后重新跑==url_get_info_sougo')
                    continue
                html = etree.HTML(response1.text)
                urls = ['https://weixin.sogou.com' + i for i in html.xpath('//div[@class="img-box"]/a/@href')]#xpath匹配链接
                para = get_para(response1)
                params = get_cookie(response1, para, UserAgent,proxies)
                for url in urls:
                    url = get_k_h(url)
                    headers3 = {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                        "Connection": "keep-alive",
                        "Cookie": "ABTEST={}; SNUID={}; IPLOC={}; SUID={}; JSESSIONID={}; SUV={}".format(params['ABTEST'],
                                                                                                         params['SNUID'],
                                                                                                         params['IPLOC'],
                                                                                                         params['SUID'],
                                                                                                         params['JSESSIONID'],
                                                                                                         params['SUV']),
                        "Host": "weixin.sogou.com",
                        "Referer": goods_url,
                        "Upgrade-Insecure-Requests": "1",
                        "User-Agent": UserAgent
                    }
                    response3 = requests.get(url, headers=headers3,proxies=proxies)

                    fragments = re.findall("'(.*)';",response3.text)
                    url_link = ""
                    for u in fragments[1:]:
                        url_link += u
                    redis_client.lpush('sou_gou_weix_goods_url_list',url_link)
                    print(f'存储成功url=={url_link}\n 当前城市为{name}')
    except:
        print(f'url==={goods_url}存储失败')
def main_v4_1():
    while True:
        try:
            goods_url = redis_client.lpop('url_get_info_sougo').decode("utf-8")
        except:
            break
        headers1 = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Host": "weixin.sogou.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": UserAgent,
        }
        response1 = requests.get(goods_url, headers=headers1, proxies=proxies)
        if '我们的系统检测到您网络中存在异常访问请求' in response1.text:
            print('代理失效')
            time.sleep(1)
            proxies = get_ip_1()
            redis_client.lpush('url_get_info_sougo', goods_url)
            print(f'存储失败进入此数据最后重新跑==url_get_info_sougo')
            continue
        html = etree.HTML(response1.text)
        urls = ['https://weixin.sogou.com' + i for i in html.xpath('//div[@class="img-box"]/a/@href')]  # xpath匹配链接
        para = get_para(response1)
        params = get_cookie(response1, para, UserAgent, proxies)
        for url in urls:
            url = get_k_h(url)
            headers3 = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                "Connection": "keep-alive",
                "Cookie": "ABTEST={}; SNUID={}; IPLOC={}; SUID={}; JSESSIONID={}; SUV={}".format(params['ABTEST'],
                                                                                                 params['SNUID'],
                                                                                                 params['IPLOC'],
                                                                                                 params['SUID'],
                                                                                                 params['JSESSIONID'],
                                                                                                 params['SUV']),
                "Host": "weixin.sogou.com",
                "Referer": goods_url,
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": UserAgent
            }
            response3 = requests.get(url, headers=headers3, proxies=proxies)

            fragments = re.findall("'(.*)';", response3.text)
            url_link = ""
            for u in fragments[1:]:
                url_link += u
            redis_client.lpush('sou_gou_weix_goods_url_list', url_link)
            print(f'存储成功url=={url_link}')


def loing_index():
    proxies = get_ip_1()
    while True:
        try:
            url_info = redis_client.lpop(f"sou_gou_weix_goods_url_list").decode("utf-8")
        except:
            print('链接已全部跑完')
            print(f'主线程结束时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')
            break
        headers4 = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
            "cache-control": "max-age=0",
            "user-agent": UserAgent
        }
        try:
            response4 = requests.get(url_info, headers=headers4,proxies=proxies)
            if '该内容已被发布者删除' in response4.text:
                print('发布者内容已删除 无法获取')
                continue

        except:
            proxies = get_ip_1()
            time.sleep(1)
            continue
        html = etree.HTML(response4.text)
        print(response4.status_code)
        try:
            title = html.xpath('//meta[@property="og:title"]/@content')[0]
        except:
            title = '杂乱无章'
        title = get_title(title)
        try:
            wen_ben_text = html.xpath('//div[@class="rich_media"]//text()')
        except:
            print('文本提取出现异常')
            continue
        wen_ben = ''
        timestamp = time.time()  # 获取13位时间戳
        for i in wen_ben_text:

            try:
                wen_ben += ''.join(i).replace(' ','').replace('\n','').split('varfirst_sce')[0]
            except:
                return

        list_length = int(len(['北京','天津', '上海', '重庆','南宁','拉萨','银川','乌鲁木齐','呼和浩特','香港', '澳门','台北','济南', '石家庄', '长春', '哈尔滨', '沈阳', '兰州','太原', '西安', '郑州', '合肥', '南京','杭州', '福州', '广州', '南昌','海口',  '贵阳', '长沙', '武汉', '成都', '昆明',  '西宁']))+1
        math = 1
        for citys in['北京','天津', '上海', '重庆','南宁','拉萨','银川','乌鲁木齐','呼和浩特','香港', '澳门','台北','济南', '石家庄', '长春', '哈尔滨', '沈阳', '兰州','太原', '西安', '郑州', '合肥', '南京','杭州', '福州', '广州', '南昌','海口',  '贵阳', '长沙', '武汉', '成都', '昆明',  '西宁']:
            if citys not in title:
                if math > list_length:
                    with open(f'D:/微信_搜狗/杂乱无章/{title + str(timestamp)}.txt', 'w',encoding='utf-8') as f:
                        f.write(str(title + '\n' + wen_ben + '\n' + url_info))
                        f.close()
                        print(wen_ben)
                        break
                else:
                    math += 1
                    continue
            else:
                with open(f'D:/微信_搜狗/{citys}/{title + str(timestamp)}.txt', 'w',encoding='utf-8') as f:
                    f.write(str(title + '\n' + wen_ben + '\n' + url_info))
                    f.close()
                    print(wen_ben)
                    break

def main():
    print(f'主线程开始时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')
    # 初始化6个线程，传递不同的参数
    # for i in range(4):
    t1 = threading.Thread(target=loing_index)
    t2 = threading.Thread(target=loing_index)
    t3 = threading.Thread(target=loing_index)
    t4 = threading.Thread(target=loing_index)
    t5 = threading.Thread(target=loing_index)
    t6 = threading.Thread(target=loing_index)
    # 开启三个线程
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    # 等待运行结束
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    print(f'主线程结束时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')
pool = ThreadPoolExecutor(max_workers = 10)  #定义两个线程

if __name__ == '__main__':
    main_v4()
    # main()
    # loing()
    # get_mkdir()