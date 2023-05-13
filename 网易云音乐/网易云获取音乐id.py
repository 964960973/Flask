import json
import urllib.parse
import requests
import execjs
import time
import subprocess
from sql_help import db
name = input('输入你想获取的歌手名称')

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

def sql_table(name):
    sql = f"""CREATE TABLE 网易云_{name} (
         歌曲id  varchar(200) ,
         歌曲名称  varchar(200),
         详情链接  varchar(200))
         """
    db.tables(sql)

def music_url(id):
  ids = id
  # data = '{"ids":"[1473782328]","level":"standard","encodeType":"aac","csrf_token":""}'
  data = '{"ids":"'+str([ids])+'","level":"standard","encodeType":"aac","csrf_token":""}'
  with open(r"./网易云.js", encoding="utf-8") as f:
    ctx = execjs.compile(f.read())
  info = ctx.call('d', data, '010001','00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7','0CoJUm6Qyw8W8jud')
  return info['encText'], info['encSecKey']

def music_pinlun(id,cursor):
  ids = id
  if cursor == None or cursor == '':
      cursor = -1
  # data = '{"rid":"R_SO_4_1974443815","threadId":"R_SO_4_1974443815","pageNo":"1","pageSize":"20","cursor":"-1","offset":"0","orderType":"1","csrf_token":""}'
  data = '{"rid":"R_SO_4_'+str(f'{ids}')+'","threadId":"R_SO_4_'+str(f'{ids}"')+',"pageNo":"1","pageSize":"20","cursor":"'+str(cursor)+'","offset":"0","orderType":"1","csrf_token":""}'
  with open(r"./网易云.js", encoding="utf-8") as f:
    ctx = execjs.compile(f.read())
  info = ctx.call('d', data, '010001','00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7','0CoJUm6Qyw8W8jud')
  return info['encText'], info['encSecKey']



def getpwd():
    name = '赵雷'
    data = '{"hlpretag":"<span class=\\"s-fc7\\">","hlposttag":"</span>","id":"3865036","s":' + str(f'"{name}"') + ',"type":"1","offset":"0","total":"true","limit":"30","csrf_token":""}'
    # data1 = '{"hlpretag":"<span class=\\"s-fc7\\">","hlposttag":"</span>","id":"3865036","s":"赵雷","type":"1","offset":"0","total":"true","limit":"30","csrf_token":""}'
    with open(r"./网易云.js", encoding="utf-8") as f:
        ctx = execjs.compile(f.read())
    info = ctx.call('d',data,'010001','00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7','0CoJUm6Qyw8W8jud')
    return info['encText'],info['encSecKey']

def mobie(id,proxies):
    params,encSecKey = music_url(id)
    payload = f'params={urllib.parse.quote(params)}&encSecKey={encSecKey}'
    url = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token="
    headers = {
        'authority': 'music.163.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': '__bid_n=18599d34aab4ea8bc94207; _ntes_nnid=e317165257b3c5f764769cf5950924b1,1675753104383; _ntes_nuid=e317165257b3c5f764769cf5950924b1; P_INFO=18038573677|1675756508|1|music|00&99|null&null&null#gud&440100#10#0|&0||18038573677; unisdk_udid=1cc9614d920a2367dcd7b2cee2088f22; FPTOKEN=mME2WHG5136xLuqhzJpo6RVuqBg25QlM/ilER4VNCQwJ6H1OFm7NjGiVLMUCXru0QXaeX25d6/PDIanKUUWEjec3cLlw5aQh8ltDaewpGn2Wyg8Nk+idVy1S/IQjloNRRzFLGIpkO3QV9UfuogkCIgnle0/GO14OqhywQcDDhXQHbkBuEmx5NReFjd36yM2Ehp4vhajIrfyPlQcWtJx5eT1wzSgyax3tX+8Il731oWTOXwqQ2agUEh5WMmOiIPBM0dv9Zo5YP3QLV6yD7PzaJx7LffMHhjBiW3YEqK0XXevYX2TZiHHT8MJMwuxH5Dnf8hZStFw1pQ25KGBcRghmjHKv2QjIp67uNsaU3eF46fXoUpDXbL9yaHIjZa8YlyclihQlO2lB/nCdG/U7VA4kvg==|5po6spzmeyDF56GR8dWTD+qL0TkfkfLJVz9keHK9G/Q=|10|59a4d73803bd7559f1d94b5dd0a9e06f; NMTID=00Ow8CUhEBLw5zi9kftuVWWuC1Ob_gAAAGHtupB7A; WEVNSM=1.0.0; WNMCID=njflwx.1682401018750.01.0; WM_TID=P2COx%2FCUUkhEAVEEBUOALByYid4Nal%2Bp; WM_NI=Uh8dlqorUEzSCU1gnk2TaVXEgRskF2BpiPRka5MruZENWwxl8txKpnhYIvfiFCCJnUNcY4dwxil500Lc6LBp%2BQT4vCK5RawDy6opH%2B74RVDBGllzgxzQ86Zuk8TPasPxV1M%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee85ef33f78ea1a3b380b3868bb6c85e928f9b82d845b1f5a0b8b36f85ad8899f82af0fea7c3b92a97b8f885ef7badae9ba6f959818bff88ed61f28cafb7db4fa58ebd8cc53a82b0a7b1d161a3eb8393f85287929998fb68fcacb8acf366ac878797e563869d8dabed5f8ebd97d5e77dbcb7a4d6b33c90bdfaadc17ce98f9cd5f54989eb9e82f650bbeaa191cb21f5ec9eb7c74a85b4a49be674ba8ff8d7d97fa9e89cb1e47994a89ad2d037e2a3; playerid=93815170; JSESSIONID-WYYY=KksVORmG6MU9zlYfyf1i%5C%2FkkBwiAG2k6v6SmfDbvR0lmYnm6f%5C88xeDkN6nYhA9%2FAvMAGK9GCnRuEFx2rcOb%5C7bAZnZxD%2BxYiI8ing51k6UxOVIvITPJ4%2BSgc4SVE6wpu8fxw%2B2a35WX2bl2CiOx2C3U7%5C6pqh38D1ROPVFbmuBFZICI%3A1682479174308; _iuqxldmzr_=33; NMTID=00OJGNhBGCcWfEhakTwsddMVE9MkxYAAAGHt7HJyA',
        'origin': 'https://music.163.com',
        'pragma': 'no-cache',
        'referer': 'https://music.163.com/',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }
    response = requests.request("POST", url, headers=headers, data=payload,proxies=proxies)
    data = json.loads(response.text)
    music = data['data'][0]['url']
    return music

def wnag_yi_music():
    params,encSecKey = getpwd()
    url = "https://music.163.com/weapi/cloudsearch/get/web?csrf_token="
    payload = f'params={urllib.parse.quote(params)}&encSecKey={encSecKey}'
    headers = {
          'authority': 'music.163.com',
          'accept': '*/*',
          'accept-language': 'zh-CN,zh;q=0.9',
          'cache-control': 'no-cache',
          'content-type': 'application/x-www-form-urlencoded',
          'cookie': '__bid_n=18599d34aab4ea8bc94207; _ntes_nnid=e317165257b3c5f764769cf5950924b1,1675753104383; _ntes_nuid=e317165257b3c5f764769cf5950924b1; P_INFO=18038573677|1675756508|1|music|00&99|null&null&null#gud&440100#10#0|&0||18038573677; unisdk_udid=1cc9614d920a2367dcd7b2cee2088f22; FPTOKEN=mME2WHG5136xLuqhzJpo6RVuqBg25QlM/ilER4VNCQwJ6H1OFm7NjGiVLMUCXru0QXaeX25d6/PDIanKUUWEjec3cLlw5aQh8ltDaewpGn2Wyg8Nk+idVy1S/IQjloNRRzFLGIpkO3QV9UfuogkCIgnle0/GO14OqhywQcDDhXQHbkBuEmx5NReFjd36yM2Ehp4vhajIrfyPlQcWtJx5eT1wzSgyax3tX+8Il731oWTOXwqQ2agUEh5WMmOiIPBM0dv9Zo5YP3QLV6yD7PzaJx7LffMHhjBiW3YEqK0XXevYX2TZiHHT8MJMwuxH5Dnf8hZStFw1pQ25KGBcRghmjHKv2QjIp67uNsaU3eF46fXoUpDXbL9yaHIjZa8YlyclihQlO2lB/nCdG/U7VA4kvg==|5po6spzmeyDF56GR8dWTD+qL0TkfkfLJVz9keHK9G/Q=|10|59a4d73803bd7559f1d94b5dd0a9e06f; NMTID=00Ow8CUhEBLw5zi9kftuVWWuC1Ob_gAAAGHtupB7A; WEVNSM=1.0.0; WNMCID=njflwx.1682401018750.01.0; WM_TID=P2COx%2FCUUkhEAVEEBUOALByYid4Nal%2Bp; WM_NI=eXc7FhbAMW6mubX2hAT11cUbDSpDb%2FFViLY1ZfMy1wWIv%2FedAVw5X01QBC6DzaUUC9W47%2BM8krXzbIVO1kjoltrSxN%2BPBmdqQTqwqMKtPSy0ek3IFFssa2XtqPgxo%2BdwZzc%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee87b44a8fefffaec659ad8e8ab7d14b968a8b83c16bb4b0bdd0d961a999e58cdb2af0fea7c3b92aa788add8c564a29f83b8b567b7be98d3eb4b98efff84d86a888dc0a5e125868aa7addc3b9aba839ab47d9597bad0e870838ab9d6db3cf38f8ea4b550babf9bb6c23395ecf9ccd034a9ae989be1439691ff8ce965b0acbeb4fb46e9908e8ee77b938cbf98f44789aca0b4fc3ca7b5fdaac54eb1adafd3db80b390a999ee21a8a9969be237e2a3; JSESSIONID-WYYY=FtA8Im634H8mMVoUh4xsUwRD4mm2QAmCYnqCqeDvo%2Bj1oIzCu7s41d2wA%2F%5C%5Ce3rvnJB02N23tfyEzj%5C9OgqOQTJxkkxCBV37MJN2c8kpnuKj8J8ivATNBtKRCVdWYZGWYs2c1AeQUlhX9ugiPHAhk0Fn0GZ20lj6RJk5ssI2SNszO2fI%3A1682417803020; _iuqxldmzr_=33; NMTID=00OJGNhBGCcWfEhakTwsddMVE9MkxYAAAGHt7HJyA',
          'origin': 'https://music.163.com',
          'pragma': 'no-cache',
          'referer': 'https://music.163.com/song?id=1974443814',
          'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-origin',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }
    sql_table(name)
    proxies = get_ip()
    response = requests.request("POST", url, headers=headers, data=payload,proxies=proxies).text
    data_list = json.loads(response)['result']['songs']
    for data in data_list:
        music_name = data['name']
        music_id = str(data['id'])
        index_url = 'https://music.163.com/#/song?id=' + str(data['id'])
        # music_url_1 = mobie(music_id,proxies)
        try:
            db.insert_one(f'insert into 网易云_{name} (歌曲id,歌曲名称,详情链接) values("{str(music_id)}","{str(music_name)}","{str(index_url)}");')
        except:
            print(music_name,music_id,index_url)
        print('插入成功')


wnag_yi_music()