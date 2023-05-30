import requests
from lxml import etree
import random
# from xpinyin import Pinyin

def get_image(name,srcs):
    for i,o in zip(srcs,name):
        url = i
        name = o
        headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"
        }
        print('保存中'+name)
        response = requests.get(url, headers=headers).content
        with open(f"E://汽车之家/{name}.jpg", "wb") as f:
            f.write(response)
        print('保存完毕'+name)

def get_ip():
  proxy = ['http://Ltubta3tn09n:g2pu4CvTTGXg@36.133.212.69:32080', 'http://xgvuZFHRzJO4:FUSZJSXHydPa@36.133.103.151:32080', 'http://6Wbu08qvbu5E:GQejcjCTw49N@36.138.61.22:32080', 'http://BCIGhZPvz8Ew:Vw9n1hcwBK3P@36.133.212.107:32080', 'http://98f0c6PjU55v:GTLhQc7U59A9@36.133.103.101:32080', 'http://cNfKgSZfjxG4:PeK7IQRwjQxk@36.133.213.153:32080', 'http://fa4EzZFY97TR:AbTMZ8Kgzyug@36.133.104.93:32080', 'http://DEB8WnQwJBbu:OevMXFTLSCdP@36.133.210.49:32080', 'http://cqPNEnUcFbYh:EAZaqMVJ8S1x@36.133.103.11:32080', 'http://RsKTrHx4QFDO:h513U7TTgEfx@36.138.61.119:32080', 'http://yFvN4Y4Za7G6:xWX4r5aWgFjf@36.133.212.81:32080', 'http://UTdzOK6YkTzh:bVfErhPP1jtm@36.133.104.79:32080', 'http://RzXpawB9UZX3:9w5bTk09rWgd@36.133.102.208:32080', 'http://PnHLH3eewpw8:dUWL2S7bIxeZ@36.133.102.189:32080', 'http://Pzn2q3shOWaj:0vu59O0p07YR@36.133.101.151:32080', 'http://DGDFgWBgQk3p:8aHzWJNIhHD2@36.133.102.12:32080', 'http://CcB3PPIeeLBS:nYuJBXuFg6Nm@36.133.213.220:32080', 'http://Zy3RVhnZkA5s:Er5asCIq9pA6@36.138.61.123:32080', 'http://VvkOG4eBFDg6:Mka9hh1sK3Vy@36.133.104.116:32080', 'http://5D1OsnsQ6JUZ:q5afKCYcs6ru@36.133.104.63:32080', 'http://wSszPfanZ5eW:641qnuJTJNSz@36.133.104.26:32080', 'http://MGv3HmBHv7Yb:AU4ZVU5DVkDx@36.133.103.174:32080', 'http://nYRtYNcOHZ1y:JNw5wSyWwICm@36.133.102.220:32080', 'http://nC5D16KxZ5NA:4KkAOSHqEAFg@36.133.209.53:32080', 'http://YENEBBM7ZTSa:b60RKbb69w4P@36.138.63.10:32080', 'http://Jqg8E8FQEvP3:nXMmX7h5zKyT@36.133.103.186:32080', 'http://jwD6qpbJ1fHQ:spW6xP3u6XRP@36.138.61.190:32080', 'http://7v07bYwncuFF:4WcgXcbBm2PS@36.133.103.118:32080', 'http://Zx8JPQCrEkbg:ISByGzOqK4ab@36.133.103.249:32080', 'http://8SfH8QqGHYPx:rvMOSEXhuG4j@36.133.212.144:32080', 'http://5tNPqNUspfdv:bW3IRFWVxO7d@36.138.61.15:32080', 'http://j6zUBwcmLwJN:rD9NnvjAfUyC@36.133.101.24:32080', 'http://SReyxPR8M8dE:ATBwZk4smpPC@36.133.104.120:32080', 'http://CR0IIpcqKFvh:6he3RMcfYKyM@36.133.214.90:32080', 'http://Q5dh0tkcb1vr:susV1aVY2yzU@36.133.100.222:32080', 'http://g38RQvc6y2rQ:x5APaCbILNM7@36.133.212.169:32080', 'http://GWHfubGMN6aU:xuIEG2GwZ1XP@36.133.101.174:32080', 'http://BxIGWS8fE9J8:IBuTgs1U0CZO@36.133.103.206:32080', 'http://m9REDKE1pWXJ:zFfP3fGMQ7N8@36.138.63.94:32080', 'http://VkvajTFdK3PL:XU1vuYLPT8rK@36.133.209.86:32080', 'http://EmjFLW4p9MnG:xLDY235hr6Vc@36.133.103.252:32080', 'http://4ENacpQ5v0Hh:X9r4z5jdarph@36.133.214.115:32080', 'http://1UUJ3rnq9HwX:QpfSaDurD1p3@36.133.103.160:32080', 'http://HQ9zYBSc4jBQ:D8O6kLbrKrBB@36.138.61.98:32080', 'http://rFe3OCNWY5Y3:B47rNf9EUcwY@36.133.103.230:32080', 'http://IcggEuxjndGz:xWsfSQWwm1rG@36.133.101.60:32080', 'http://5ct1mcCTAsL0:WzIh3kvyxPFx@36.133.103.226:32080', 'http://tNExtUv0s7ut:vtvmXOFsKuOW@36.133.213.67:32080', 'http://pD2Nakdxt6yb:yv6f3CTbzMWv@36.138.63.58:32080', 'http://7v07bYwncuFF:4WcgXcbBm2PS@36.133.103.118:32080', 'http://3TwTG3Spfqhh:xIXcEIDYWIR3@36.133.209.75:32080', 'http://p3rRrLEezh67:NBuOvA8wP75E@36.133.103.227:32080', 'http://SgdYFSO3sNrv:fIDnTvGbXby9@36.133.214.239:32080', 'http://1etPSnDdHGNB:vh6bVCkPjn1K@36.133.100.238:32080', 'http://EnHnQuGwP19Z:7dLySGZ2J2Jx@36.133.103.251:32080', 'http://IHhps3rB56tQ:ysJXv9U4j1At@36.133.214.121:32080', 'http://xgvuZFHRzJO4:FUSZJSXHydPa@36.133.103.151:32080', 'http://OJVqIpuKCagG:yGRWZWLUWrL8@36.133.103.207:32080', 'http://z1AceOzpYLMV:2XDKFQaICu7Z@36.133.214.119:32080', 'http://wqLquXe1T73K:JEaErmukrKPb@36.133.103.140:32080', 'http://stK09IvEB5GH:63C6uDNGtLv0@36.133.212.66:32080', 'http://PZfAKYLZhUS3:RRtU3pmG9v5y@36.133.101.167:32080', 'http://9SuExMR0PteG:40cV53639O7G@36.133.103.112:32080', 'http://pJm8zSmA5neu:9UykJmsYSstb@36.133.104.109:32080', 'http://LhnJx6Vrfa0P:tR1xGDybrXeS@36.133.103.205:32080', 'http://KkK3ZYcQWhdR:fZa9AkZV5neN@36.133.210.48:32080', 'http://OZK3XHTOD68Y:zSMUbMFdgCNq@36.133.104.102:32080', 'http://smFkyAGTM3Yj:uzVd99Gb7cqW@36.133.214.53:32080', 'http://z1aRVkafbLzR:dXa4w6QEYVem@36.133.104.40:32080', 'http://7jrRmpwhVXM5:8EQaW6Znr81m@36.133.210.92:32080', 'http://tr1KAEswE5PQ:GObF5DUw3ut3@36.133.212.80:32080', 'http://ALjyZjTWZrXK:bwJyLcxfUFgN@36.138.61.103:32080', 'http://MTVPgX2CtL28:HFDVxBRVpIwu@36.138.61.35:32080', 'http://E0saa57pD0Uz:zURVC097Cr7d@36.133.103.139:32080', 'http://sccBs32SF7FW:mVsZpjNC3eW4@36.133.213.76:32080', 'http://AYWOnqWtubKy:ffX1WT5pZHb9@36.133.101.110:32080', 'http://jnuvhTc9mnqS:pNWBznnqr20M@36.133.210.64:32080', 'http://Ac0jFDf03dms:rUnJ1V11HXsw@36.133.212.250:32080', 'http://CXLjcD5bYHDy:fe5AcIB8O9zU@36.138.61.134:32080', 'http://nYRtYNcOHZ1y:JNw5wSyWwICm@36.133.102.220:32080', 'http://qyW5wmJOgS9E:z01F1HmQLnvO@36.133.102.164:32080', 'http://Osh0r8htRE1g:FM28h9dshFzz@36.133.101.56:32080', 'http://XXbaxe2Mk6kI:96DzXm60RYWs@36.133.101.190:32080', 'http://rS0H0ftxUuKE:ChuhtzWKF5HV@36.133.212.174:32080', 'http://jJp6Q61wersJ:YMIDEuBgLmGC@36.133.214.185:32080', 'http://WDYZB8tRK3d7:8kGzrfNejLt4@36.133.212.67:32080', 'http://AFg407ZLcmxE:zS0eQtNRxcaV@36.138.63.52:32080', 'http://gPyUC1uIZrLz:ye1348DFaCAS@36.133.102.178:32080', 'http://T0VuzTXtejsq:XIjI95rNf3JW@36.133.54.232:32080', 'http://MLbWZsr0JFKn:5NVWZbU0ZM1b@36.138.63.4:32080', 'http://aK03zrR3B75J:9Q2Wy8gBQzMt@36.133.213.190:32080', 'http://qadN1vd7BpZQ:wPqKvtz74e3t@36.138.61.63:32080', 'http://I7zb6u2VIW7x:w1DFev4HcPXK@36.133.101.180:32080', 'http://YVWOTUOyL3zW:gFhIg8Odzycf@36.133.212.33:32080', 'http://3CrxXNQ69ZVn:zkHHOffHU0ra@36.138.61.16:32080', 'http://XxjvJyY0syCa:XbGVAPc44C0u@36.133.214.29:32080', 'http://9Kwm10hOjJJ7:aPm0UkvDOxYT@36.133.209.3:32080', 'http://PX6SvyPYeKup:ssK6pDGVsspe@36.138.61.197:32080', 'http://jjA9INnqngnG:mKZW61q0PaZq@36.133.102.207:32080', 'http://168kPKv5dvXO:Y6gYeJeAuJOu@36.138.61.44:32080', 'http://Gbnx7ak1SXzF:OgzJ0GwSLSmT@36.133.210.68:32080', 'http://bcNhFxN2BsMp:XtG3p2EG5I0p@36.138.63.146:32080', 'http://WXUjbCfeIeTE:1FjqQxmvM5Ex@36.133.213.148:32080', 'http://2KmOLSu7vXRn:IfwEjnX2EJmE@36.138.63.116:32080', 'http://JJpacb6V9VrY:D14skH9pm0zO@36.133.101.70:32080', 'http://uU03x4zZurjM:V9yAugF0xO6I@36.133.212.215:32080', 'http://p4NWYNb6RH6I:5Ez5Cv7aYeCL@36.138.61.114:32080', 'http://wY6GZSmVr0ZF:qqKqsPbPOM4n@36.133.102.186:32080', 'http://nJ4VyeEjxdmR:LScccKOpM0Hd@36.133.214.8:32080', 'http://zmcBHAdmZDh6:NMUDaYzYwWr8@36.133.212.20:32080', 'http://1gKvHy3cPMNR:X7a9dx9MxtGp@36.133.214.34:32080', 'http://5fvf8tFDhquO:K2w3TSLgnstA@36.133.212.130:32080', 'http://Y8eL84rh6sKD:EQzaxtBYPAPn@36.133.103.253:32080', 'http://MCZqR6X35Cut:Lp5sNFn1POQ6@36.133.103.166:32080', 'http://E5FgCYzFdIzS:0QVVsp6HqIny@36.133.213.17:32080', 'http://sIFOrAGpT8ug:2Uw4b8NmDtap@36.133.104.50:32080', 'http://bDSenrQDnDma:MLX32XqUxLrO@36.133.213.38:32080', 'http://PhCbymsRKqrC:4xcFZ7hmk8M8@36.133.103.148:32080', 'http://1NELUsY6tk2S:VbABMw1sdAXF@36.133.212.98:32080', 'http://PqKMfadCWUbe:MhEmtuA4BJkt@36.133.102.17:32080', 'http://68ZQwu4RYw3W:8eBaA0g1tUgT@36.133.102.193:32080', 'http://UVTWhf8JFmaq:b64a1vyupGKW@36.133.209.42:32080', 'http://MgmMh0vcU375:QJdeY2R7mQxf@36.133.212.216:32080', 'http://E0hsgCbsk8sx:0FSeJb01Ap5n@36.133.212.5:32080', 'http://V8XEERn0QSzy:3Fy6qZ4DkTbO@36.133.210.60:32080', 'http://XWjnG1ykvp2e:RzD25wqZE6bj@36.138.61.176:32080', 'http://5Gc6aqhDp8qL:VfYGg6vP4A5D@36.133.212.116:32080', 'http://SBZ2f0HhDBnB:rH2qr5D18SyU@36.133.103.236:32080', 'http://Wbr7GdLDDXp1:hNksCTD9zzfC@36.138.61.247:32080', 'http://PC8trMhKXvd3:udVrW18AeCHr@36.133.212.182:32080', 'http://aWmwrtYgwzuF:44pOJvxtDKJW@36.133.102.5:32080', 'http://BJ1pJzCWTZ7q:5yXaMjMSBPXa@36.133.103.39:32080', 'http://bYFWxTXTvxzN:nHcV4d8dUdSq@36.133.210.29:32080', 'http://kYJfDvaaEkPB:zSvnJGIB2yNJ@36.133.212.75:32080', 'http://8KJGW4nFMzXE:Mc4Khv1sEdfD@36.133.214.45:32080', 'http://cFbPIGbpJsvP:5ykJXUZvJQLC@36.133.212.128:32080', 'http://PSneNaU2kydC:CvBs6b6XUTwA@36.133.209.27:32080', 'http://0vh90XNL93Xp:ktTARedQtPQd@36.133.101.86:32080', 'http://wqLquXe1T73K:JEaErmukrKPb@36.133.103.140:32080', 'http://RzXpawB9UZX3:9w5bTk09rWgd@36.133.102.208:32080', 'http://zRILAyeQS6q5:k5e3C13rAFNz@36.133.104.64:32080', 'http://EPpBAIasTNFX:Z5s81zTqe9pH@36.133.102.212:32080', 'http://LsnCWjuFILdx:PMF3dIvN7sKe@36.133.213.130:32080', 'http://YARvNqBhWfT8:ar7RptnH0sIO@36.133.103.134:32080', 'http://SFdzusY0f8Pf:psYMCWNfgT21@36.133.212.212:32080', 'http://DewKvDC1C47W:mSJD39xA78ya@36.133.102.169:32080', 'http://6OSYK8mqq7BM:1mBUm4DH6EBK@36.133.44.230:32080', 'http://kZQgjxKBuX6I:2ITke5rOLxJc@36.133.212.140:32080', 'http://Hjg7ZH8fRUjA:CukdWTDBM4hf@36.138.63.47:32080', 'http://WMhAbU3DEN2q:N6M39GBeztQK@36.133.104.16:32080', 'http://Jqg8E8FQEvP3:nXMmX7h5zKyT@36.133.103.186:32080', 'http://2d4TEYJ9ZzZx:q2aQxN1zNmgB@36.133.209.35:32080', 'http://YFahL7ydnZtV:GCPZsYGs8369@36.133.103.135:32080', 'http://Z9BKmQRcTIDn:BQzrPtMm3ky6@36.133.209.51:32080', 'http://D2rNGcFVjsuL:ju6HMHZtCKLC@36.133.210.79:32080', 'http://4ztpwMVrjddx:ZOKpQtKXTe7t@36.133.103.208:32080', 'http://7q9QWOXW9BMZ:3hBgUTAn2STP@36.133.103.215:32080', 'http://sbeq7gXbGMrP:I1jku0yR1Wjm@36.133.104.68:32080', 'http://1etPSnDdHGNB:vh6bVCkPjn1K@36.133.100.238:32080', 'http://2GuXWMKhzNzC:Byc54CPBzL26@36.133.210.56:32080', 'http://QHLVebWA0UaA:WxAqAvWHAayq@36.133.103.152:32080', 'http://BJ1pJzCWTZ7q:5yXaMjMSBPXa@36.133.103.39:32080', 'http://LTReTPabh2yy:A7EHe6hD45Dw@36.133.209.98:32080', 'http://NHUqQnseSADN:paVF5usyqIXM@36.133.214.144:32080', 'http://qQSGpEcwpMmO:hzcT0dONxUIU@36.138.63.120:32080', 'http://cHNEp46HsTP9:FB0Egdsn4OKz@36.133.101.58:32080', 'http://7I54F2mNIPPU:wcCI03nmVDWP@36.133.214.7:32080', 'http://4GQVGHy0nt3q:OctzSCPGtMHm@36.133.104.115:32080', 'http://MGv3HmBHv7Yb:AU4ZVU5DVkDx@36.133.103.174:32080', 'http://EaWBKqZwP76p:EYmvGskpIxJF@36.133.214.32:32080', 'http://NRKvedASdt6E:xapfSeBIssu9@36.138.61.211:32080', 'http://gWRhLO8bnysm:d7Lq9RJYjcTW@36.133.101.117:32080', 'http://KFepQkwap6za:9FuakaItW8Qx@36.133.212.154:32080', 'http://wcrZNV3J0cdg:DYUeBQQVY7XC@36.133.102.7:32080', 'http://jXE0XkeXVms9:7Ee2bpCKHCaM@36.133.212.46:32080', 'http://Kpnr7wtK1kdA:gsELpK41fBTQ@36.138.63.101:32080', 'http://FB2z5cqJ04Ih:NkrjFRtRAGFT@36.133.214.25:32080', 'http://MXIf3cB4HtnE:rbjKRfxfFpqB@36.133.212.231:32080', 'http://WDfTWUr4zyOC:stm1KmChEKDI@36.133.103.102:32080', 'http://8S2JEPPFTLJ9:6Y1ZsgJeJtKn@36.138.61.37:32080', 'http://9DHWTHVkEeDk:dmG90BuHkXBR@36.133.212.79:32080', 'http://evtOwpQTC8zJ:KhWXEbOx7gut@36.133.104.78:32080', 'http://70WvRvmH1A6c:4p9ke3LCrqnu@36.133.212.163:32080', 'http://ROASOfbw35r7:VJgerP1fExXd@36.138.61.80:32080', 'http://dIjrBZLKnqaI:yePJ1644BN09@36.133.210.173:32080', 'http://AgLczqUqYWfC:WsGHex3C563c@36.133.214.151:32080', 'http://JRQkY50tAJbf:DjSJWFgVZRSP@36.133.101.39:32080', 'http://wEKmRkW7749J:qaTqafXdHIM0@36.133.103.122:32080', 'http://Nrj36rSJRtJf:PwOzmfyHZG1M@36.133.104.69:32080', 'http://zjDn65ET2wvx:zOfAcLrDJYGP@36.133.102.213:32080', 'http://UT6RKq1k5M5O:YWCB2Jrb4mXa@36.133.214.21:32080', 'http://OJVqIpuKCagG:yGRWZWLUWrL8@36.133.103.207:32080', 'http://gNgtJen56SG2:K0gDqLvPTk0W@36.133.101.169:32080', 'http://GgSzecd0j4Rd:VGDvKsyXzUU2@36.133.209.143:32080', 'http://YkJ0XJ5KZLz7:5NcW6vYR4dC2@36.133.213.8:32080', 'http://d8BqDIkRbsHV:dMhtJS6CPvqc@36.133.214.68:32080', 'http://SwuPaTsaZFdf:LD31DRImmErG@36.133.213.47:32080', 'http://zQztVAvZAGzO:dquyBRXRRLLM@36.133.210.50:32080', 'http://OSXB6KsWNX4I:5SWQd53MgACY@36.133.213.24:32080']
  proxy = random.choice(proxy)
  return proxy


def login():
    name = input('请你输入想要获取的图片类型')
    # p = Pinyin()  # 使输入的中文变成字母    北京（beijing）
    # result1 = ''.join(p.get_pinyin(name).split('-'))  # 分割字母以’-‘为拆分，去除空格
    for page in range(2,10):
        url = 'https://www.igdcc.com/4K{}/index_{}.html'.format(page,name)
        payload={}
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4621.0 Safari/537.36'
        }
        urls = []
        response = requests.request("GET", url, headers=headers, data=payload)
        response.encoding = 'utf-8'
        tree = etree.HTML(response.text)
        href = tree.xpath('//li[@class="cell"]/a/@href')
        for i in href:
            url ='https://www.igdcc.com' + i
            # print(url)
            urls.append(url)
        return urls
def index():
    name = []
    srcs = []
    urls = login()
    for url in urls:
        payload = {}
        headers = {
            'authority': 'www.igdcc.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': 'Hm_lvt_de192693edffe8e7a6a252da6479b563=1661242418; egjtlmlusername=18038573677; egjtlmluserid=963995; egjtlmlgroupid=1; egjtlmlrnd=Nf1wgMYOwoRKPTfhw9fT; egjtlmlauth=142400ecfc4f00bd0c105496e68626ab; egjtlecookieinforecord=%2C2-32578%2C2-32580%2C2-32544%2C2-32530%2C2-32531%2C2-32540%2C2-32510%2C; Hm_lpvt_de192693edffe8e7a6a252da6479b563=1661244254',
            'if-modified-since': 'Wed, 17 Aug 2022 01:52:45 GMT',
            'if-none-match': 'W/"62fc49ed-72c5"',
            'referer': 'https://www.igdcc.com/4Kmeinv/index_3.html',
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
        proxy = get_ip()
        proxies = {"http": proxy, "https": proxy}
        response = requests.request("GET", url, headers=headers, data=payload, proxies=proxies)
        response.encoding = 'utf-8'
        tree = etree.HTML(response.text)
        page_urls = tree.xpath('//div[@class="photo-pic"]/a/img/@src')[0]
        page_name = tree.xpath('//div[@class="photo-pic"]/a/img/@alt')[0]
        name.append(page_name)
        srcs.append(page_urls)
    get_image(name=name,srcs=srcs)
if __name__ == '__main__':
    index()