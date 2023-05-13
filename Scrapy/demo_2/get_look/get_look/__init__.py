# import requests
#
# url = "https://book.douban.com/latest"
#
# payload = {}
# headers = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#   'Accept-Language': 'zh-CN,zh;q=0.9',
#   'Cache-Control': 'no-cache',
#   'Connection': 'keep-alive',
#   'Cookie': 'bid=UcZiuGJo7Eo; __utmc=30149280; __utmz=30149280.1682646495.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=81379588; __utmz=81379588.1682646495.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _pk_ses.100001.3ac3=*; __utma=30149280.1582869532.1682646495.1682646495.1682671413.2; __utma=81379588.432135594.1682646495.1682646495.1682671413.2; ap_v=0,6.0; ll="118281"; __gads=ID=131fef2cca741d95-221682bac0df0060:T=1682671426:RT=1682671426:S=ALNI_MaI14VXuKrCNJ0QfBJGydxzoXON7g; __gpi=UID=00000bfefa22e8dc:T=1682671426:RT=1682671426:S=ALNI_MYGWsy8xx_1e0R5QzluhFvinSatKA; _vwo_uuid_v2=DC5629DC0B90F991979E450FF512C3C62|830c343acfb95b2607631686af1356b9; __yadk_uid=x7g7RBrRWUigdDdkmUnxyudbpt8vX1AZ; __utmt_douban=1; __utmb=30149280.5.10.1682671413; __utmt=1; __utmb=81379588.4.10.1682671413; _pk_id.100001.3ac3=c4d72ecd4b0ddf07.1682646494.2.1682672307.1682646494.; bid=bf__S5HwyBI',
#   'Pragma': 'no-cache',
#   'Sec-Fetch-Dest': 'document',
#   'Sec-Fetch-Mode': 'navigate',
#   'Sec-Fetch-Site': 'none',
#   'Sec-Fetch-User': '?1',
#   'Upgrade-Insecure-Requests': '1',
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
#   'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
#   'sec-ch-ua-mobile': '?0',
#   'sec-ch-ua-platform': '"Windows"'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)
