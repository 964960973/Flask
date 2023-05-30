import json

import requests
id = []
def index():
  key = input('输入歌手，或者歌名')
  url = "http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key="+key+"&pn=1&rn=30&httpsStatus=1&reqId=d27bb150-2069-11ed-a364-09967789ed51"
  payload={}
  headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1660987420; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1660987420; _ga=GA1.2.723502094.1660987420; _gid=GA1.2.911366984.1660987420; _gat=1; kw_token=5TL9DRWXHQ5; kw_token=NYOXD81R1IN',
    'Referer': 'http://www.kuwo.cn/search/list?key=%E6%9E%97%E4%BF%8A%E6%9D%B0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'csrf': '5TL9DRWXHQ5'
  }

  response = requests.request("GET", url, headers=headers, data=payload).text
  data_json = json.loads(response)
  list_json = data_json['data']['list']
  rid = []
  list = []
  for i in list_json:
    artist = i['artist']
    id.append(i['rid'])
    name = i['name']
    data = {
      '歌手名称':artist,
      '歌曲名称':name
    }
    list.append(data)
  # print(list)
  return rid
def login():
  for i in id:
    try:
     url = 'http://www.kuwo.cn/api/v1/www/music/playUrl?mid={}&type=music&httpsStatus=1&reqId=1cd6cf31-206c-11ed-b81d-97a458cfc238'.format(str(i))
     headers = {
       'Accept': 'application/json, text/plain, */*',
       'Accept-Language': 'zh-CN,zh;q=0.9',
       'Connection': 'keep-alive',
       'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1660987420; _ga=GA1.2.723502094.1660987420; _gid=GA1.2.911366984.1660987420; _gat=1; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1660988372; kw_token=505P85SDIY3; kw_token=I8MXGYO6LJI',
       'Referer': 'http://www.kuwo.cn/play_detail/234403971',
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
     }
     response = requests.request("GET", url, headers=headers).text
     s = json.loads(response)
     l = s['data']['url']
     print(l)
    except:
      continue

def penlen():
  for i in id:
    url = "https://kuwo.cn/comment?type=get_rec_comment&f=web&page=1&rows=20&digest=15&sid={}&uid=0&prod=newWeb&httpsStatus=1&reqId=d7b61841-206e-11ed-b884-93c8e992a57a".format(i)
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1660987420; _ga=GA1.2.723502094.1660987420; _gid=GA1.2.911366984.1660987420; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1660989216; kw_token=CWSI7U8QCV; kw_token=V0VPJXWXY4',
    'Referer': 'https://kuwo.cn/play_detail/93157',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
  }
    try:
      response = requests.request("GET", url, headers=headers).text
      s = json.loads(response)
      k = s['rows']
      for i in k:
        s = i['msg']
        print(s)
    except:
      s = '*'*20+'无评论信息'+'*'*20
      print(s)
      continue


if __name__ == '__main__':
    index()
    login()
    penlen()

