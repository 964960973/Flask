import requests
import time
import subprocess
import execjs

import execjs
def getpwd_():
    with open(r"./网易云音乐.js", encoding="utf-8") as f:
        ctx = execjs.compile(f.read())
    info= ctx.call('d','{"rid":"A_PL_0_3865036","threadId":"A_PL_0_3865036","pageNo":"3","pageSize":"20","cursor":"1668086351515","offset":"0","orderType":"1","csrf_token":""}','010001','00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7','0CoJUm6Qyw8W8jud')
    return info


headers = {
    'Proxy-Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://match.yuanrenxue.com/match/16',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
getpwd_()
for page in range(1,6):
    t = str(int(time.time())* 1000)
    # p = subprocess.Popen(['node','./16_webpack初体验.js'], stdout=subprocess.PIPE)
    # encrypt_time = p.stdout.read().replace('\n', '')

    params = (
        ('page',str(page)),
        ('m', getpwd_(t)),
        ('t', t),

    )

    # print(params)3

    response = requests.get('http://match.yuanrenxue.com/api/match/16', headers=headers, params=params)
    print(response.json())
# d('{"rid":"A_PL_0_3865036","threadId":"A_PL_0_3865036","pageNo":"3","pageSize":"20","cursor":"1668086351515","offset":"0","orderType":"1","csrf_token":""}','010001','00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7','0CoJUm6Qyw8W8jud'))
