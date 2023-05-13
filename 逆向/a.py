import requests
import time
import subprocess
import execjs

import execjs

def getpwd_(t):
    with open(r"./16.js", encoding="utf-8") as f:
        ctx = execjs.compile(f.read())
    jiami= ctx.call('aa',t)
    return jiami


headers = {
    'Proxy-Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://match.yuanrenxue.com/match/16',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

for page in range(1,6):
    t = str(int(time.time())* 1000)
    # p = subprocess.Popen(['node','./16_webpack初体验.js'], stdout=subprocess.PIPE)
    # encrypt_time = p.stdout.read().replace('\n', '')

    params = (
        ('page',str(page)),
        ('m', encrypt_time),
        ('t', t),

    )

    # print(params)3

    response = requests.get('http://match.yuanrenxue.com/api/match/16', headers=headers, params=params)
    print(response.json())
