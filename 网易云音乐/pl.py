import requests

import json
import urllib.parse
import requests
import execjs
import time
import subprocess
from sql_help import db

def sql_pl(id):
    sql = f"""CREATE TABLE 网易云_{id} (
         歌曲id  varchar(200) ,
         评语  varchar(255),
         发布时间 varchar(200),
         点赞数  varchar(200) ,
         发布者名称  varchar(200),
         发布者头像 varchar(200))
         """
    db.tables(sql)

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



def lopp():
    cursor = -1
    id = '1974443815'
    url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
    params,encSecKey = music_pinlun(id,cursor)
    sql_pl(id)
    payload = f'params={urllib.parse.quote(params)}&encSecKey={encSecKey}'
    # payload = 'params=Bu80MA1vF7xESm7jHHWF6xdU7TZad1yjjTLd5kur%2BMz4UAoQOLM5QIiBdHLeJq4mxlGRAJzFXD0W8sCQ3k6kUUZyyk5M3nMQuTqMWstSQUrGl0H2yQNGJQJ7pkLnwC%2FxuPkCYF1zSWtXiey3ngYF5LH41EsT0ukh1lHo8AhLyUF%2Fhfjr5fZCFRD5Gzwz8XAF5lh0uo09tICOP7qH%2FH6nX3mwuqqCWPk3%2F6T9D4Vd5IXwqKCKoV2UVip0bXYANaTCKmCcvi6HGHeVKG2Or0NIkczQfOloEw9vndfvc8aXDxU%3D&encSecKey=61d880b067e6ce09c7036149e66b9730056dd18ea7a76f85b3929ea13bcc25bb2ad17a8d5c3e1972accf5131bb4eecd5d609862a8a5c66e048cbd0b1c4e3f0887c926490023e60a61dece9057f9413cb1385c540814996ad500c1294cb3c7bac9428a622181ef56ad47d43e7d9cd19578e8f0bffadf74d3f6aecde26115a9383'
    headers = {
      'authority': 'music.163.com',
      'accept': '*/*',
      'accept-language': 'zh-CN,zh;q=0.9',
      'cache-control': 'no-cache',
      'content-type': 'application/x-www-form-urlencoded',
      'cookie': '__bid_n=18599d34aab4ea8bc94207; _ntes_nnid=e317165257b3c5f764769cf5950924b1,1675753104383; _ntes_nuid=e317165257b3c5f764769cf5950924b1; P_INFO=18038573677|1675756508|1|music|00&99|null&null&null#gud&440100#10#0|&0||18038573677; unisdk_udid=1cc9614d920a2367dcd7b2cee2088f22; FPTOKEN=mME2WHG5136xLuqhzJpo6RVuqBg25QlM/ilER4VNCQwJ6H1OFm7NjGiVLMUCXru0QXaeX25d6/PDIanKUUWEjec3cLlw5aQh8ltDaewpGn2Wyg8Nk+idVy1S/IQjloNRRzFLGIpkO3QV9UfuogkCIgnle0/GO14OqhywQcDDhXQHbkBuEmx5NReFjd36yM2Ehp4vhajIrfyPlQcWtJx5eT1wzSgyax3tX+8Il731oWTOXwqQ2agUEh5WMmOiIPBM0dv9Zo5YP3QLV6yD7PzaJx7LffMHhjBiW3YEqK0XXevYX2TZiHHT8MJMwuxH5Dnf8hZStFw1pQ25KGBcRghmjHKv2QjIp67uNsaU3eF46fXoUpDXbL9yaHIjZa8YlyclihQlO2lB/nCdG/U7VA4kvg==|5po6spzmeyDF56GR8dWTD+qL0TkfkfLJVz9keHK9G/Q=|10|59a4d73803bd7559f1d94b5dd0a9e06f; NMTID=00Ow8CUhEBLw5zi9kftuVWWuC1Ob_gAAAGHtupB7A; WEVNSM=1.0.0; WNMCID=njflwx.1682401018750.01.0; WM_TID=P2COx%2FCUUkhEAVEEBUOALByYid4Nal%2Bp; playerid=38101295; WM_NI=mOU%2Bx4mmwRGWBSlHohXstW2sWscLj06PMgRfpDEpfnAudtK9cgH%2FuMx4CdP5UuOevMn1XYTFLRNE4Yh9qP2Ed5HXjyqiXLWjif4bkBnNRxowRYwBexC8pdAvhIXuQJV7T3M%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee8fef74b6bbaf8dd143abbc8aa6c14a928b8aacc56ff8aabf87b74193b6ad8cb32af0fea7c3b92aaf919bccfb40afb3b9b3c65d828da4a9ee649cadbcb8b17995adadade93cf6908388d16eb49c8b91e56683abac95ca33a1b988d0f847bcec8d85d33f97ab8186f547aeef98bad74e908e82a6b753ace7bfb1b14fa8eb88b9e973b3b798add662abbafc83ea4aae929e99ee7d9287b9a3e87481e8c085c47eac979896d44296e99cd4d037e2a3; JSESSIONID-WYYY=y%5CKq%5CbR%5CpBpYZ%2FCf7CCUHsRokWgjMQxf%2B3YRMNGkGcwaSkRf0qsBtBa8RZ4CsmlQT84tSEn%5Cgc8rEorxXRdTa4%5CK09y3u%2BpM87fBxznae4jnUdq9%2FrmJ2eTXV793EytI7xWzsKUnQjN2xTPyms9a7rO6V3c558aUj%5CJV%2Fk6%5CJ0liJg8j%3A1682558167158; _iuqxldmzr_=33; NMTID=00OJGNhBGCcWfEhakTwsddMVE9MkxYAAAGHt7HJyA',
      'nm-gcore-status': '1',
      'origin': 'https://music.163.com',
      'pragma': 'no-cache',
      'referer': 'https://music.163.com/song?id=1974443815',
      'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload).text
    data = json.loads(response)['data']['hotComments']
    for rp in data:
        content = rp['content']#评语
        timeStr = rp['timeStr']#发布时间
        likedCount = rp['likedCount']#点赞数
        nickname = rp['user']['nickname']#发布者名称
        avatarUrl = rp['user']['avatarUrl']#发布者头像
        db.insert_one(f'insert into 网易云_{id} (歌曲id,评语,发布时间,点赞数,发布者名称,发布者头像) values("{str(id)}","{str(content)}","{str(timeStr)}","{str(likedCount)}","{str(nickname)}","{str(avatarUrl)}");')
        print('插入成功')
lopp()