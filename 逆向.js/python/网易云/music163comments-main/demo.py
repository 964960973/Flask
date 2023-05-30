import requests
import time
import execjs
from lxml import etree
from fake_useragent import UserAgent

headers = {
    'cookie': '__bid_n=18599d34aab4ea8bc94207; FPTOKEN=L5ESJUznIvsKBXZi7OIhA0u59OEoZBcKvq0sZZ3umnx1ba8j5mCX3cnYDXFNx2gI7Kq4KDl0KWUq0GUE6QTn4syVpH2t+96I9VEzKpy/U1A6yP9NWO0bCsWcNdmIHQb0A1XDJRvyjBORhU/Gz/D9jTftoYUoDEkPiT3CZMeqnjJ8Dq+LzGYEyPfIthD7c5h/Xcu26hzSj/cpyv1HVsmp9eEC9jpcWz5ko//bcLYRsyfx+oOqpNq2ExdBT6+KHae61FQ1fv3DcWw+bGuDPH+2qeFtoE1W9pFa6CtEDmRZjYWi9bLeAwQm/P92ZpGXXfXFAmeimA6/V3oe6Y/EpvTLa2h24ONrGVqHb9qpmGd7MZldFEorJDEn1WV12/pWpxJgy3LzVcKxlIDfQi8JoDUW/Q==|1w3Ognz5OnQreTGtnEVhqVn6VJhI1CV+quj4TqMoExk=|10|e73252c40e75e60256045bd37e2b149c; _ntes_nnid=e317165257b3c5f764769cf5950924b1,1675753104383; _ntes_nuid=e317165257b3c5f764769cf5950924b1; NMTID=00OOq6CP-EJUXbfKUuyuj36tOFYZ2QAAAGGKqskAQ; WEVNSM=1.0.0; WNMCID=qxqtqm.1675753104670.01.0; WM_NI=K3sFQptNmnLWnYvDq57lIfSeWGB%2FljisBZGJ8M1yMpjZbaOYb1JOSFF47MUlwHW6j%2FoK2%2FqzFB%2Bnu%2FwlzMEKYtq9PPfROGRQ6GsNjTyuy5F%2B9A1rz5%2FwMlF2N0CMu2GnMU4%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeadd05291bb8583d77df2b88fa3c55e969a8a83d14593ee868ee27c8b95a8ccf22af0fea7c3b92a89edbda7d47cb892a38fcf5dae87baa5f43ff5b48787d26f95998ed0ef62abad8ebbc642fc93ff9ad07caa86ae82ce53a2ef86b0d24e86ecf9aed868b59899d7e925ad95fed0f472869ee58ff825b5b4b6aec8419bacbfdad35ca68e81a8d15bf699bdafe960bbabb7d6c521fb9fff93f93feda9838dc53a8ef08daef83a85b283b6b737e2a3; WM_TID=P2COx%2FCUUkhEAVEEBUOALByYid4Nal%2Bp; JSESSIONID-WYYY=%2FqTijH1kJlBHXpY1vIFb90%5C%2FlkluCTe1MyTwAfrXerT0wI41xB47WF0okIJJonRIVM8mDK5kKnIDrPA6wQ5HUVeZx%2By%5CvgPkE3FCqGceUalPd%2BMz04T0VqTvHuzBve8de2tId1y%2BEeYPIwoZBA0A7aY6oqgWKfWng%2BRSm0Fs4YaebUu%2F%3A1675757210056; _iuqxldmzr_=33; __snaker__id=10vkLcBvW4yQKiSb; gdxidpyhxdE=xxbD2T4mH8KROH%5COMDb728HAO9u46cCb3pXPvMhJ06hrezM5YpX0%2FAKui%5CGRkO2Sl74Yb3ezwulmvZ0TREquBWgJRb95ePw5qsa%2BmCts%2BwCVeBa%2BUwqJjttAmeZ5lQOBkdixctpm%5CzOXM9XQStz%5C3UPvcBLba0XWyDJzD9S%2FAlh03WNk%3A1675757300230; YD00000558929251%3AWM_NI=NLKo8BcpAlZJBHfY%2BRSOkMtPxKkxBV9AzADQYZscdeFbdCLMU3Y2RYVi12Jfn6nCf1hD0o%2B7WrtApiQgptGlezoT7iTNQ0yHmn%2FXqkA4eZ0Muu15OVo3qDG8qdJnfR6wd0M%3D; YD00000558929251%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee9ad647ab929a82d56681b88ab7c15a869a8bb1d54883a782d5ae46b8af89d9bc2af0fea7c3b92a8e948590bb4aa1b08f8dd9428298aabaaa5a9191a5aef75cbc95a599c15efb9fb6a2c75b9b86bd84e76f86beaca4cf4797ed97d3d15396b7ffd3c96eaeeaa2a4e53bac9c0090aa3d95aebca2f36393b9c095c668a7a6a1b5b66398929fd1fc44afb2e1b9f46183ecabbbb347b7abffd6ce5eadedbfa5c634b3bc868fe55af6a9acd1d037e2a3; YD00000558929251%3AWM_TID=8JF7VsBi0TVEVRVVAALFbQ3Yt%2FM4%2BX4o; __remember_me=true; NTES_YD_SESS=f_4gkk9xjP05azo5KOsWajmO.qw0w0NiCkxQHKErHawBeypJekSXAhNt93KpsWdenKDBAXFFaNqCgTVc0s6S2V.HjMmMJ_tpbV0jGLc.0HR_xUw3hpti0CibXEkwMgJ80.zK.jLAdBbRB4UP89JRrajOZWIG2B07xeYWcLjaV95EU7GdAmJsNK.hfbtAMo2e.ThkiynuqTwxtECnr1Hmx6bby7vl8sn5QMLFoyDXqQ00R; S_INFO=1675756508|0|0&60##|18038573677; P_INFO=18038573677|1675756508|1|music|00&99|null&null&null#gud&440100#10#0|&0||18038573677; MUSIC_U=007CC115DDAB6E4E047F67F6181566D05061C0776851CA8CD5EA2F13BB7AB6CF3BDE15019C91FBF64631092B3F7C631E9726D665863559407D3F617DC524FF1DA662A7583D0B37395B79C81FC4846D5CEE86573DE4D7449B57B7956963821CE1B889F75FF16F779694B085F14F2E09D56135C53E93295A06579A01AC9BA6027B030DBE69A6B156E39C27ACC15992E49E8C4C8E1C1F34BA2B695F7DD0E4C999848B6CF798D50CEE833D3DF4B47C0311EEC63298E9CCC7F8D0627F37000DE62D8F97E5E7BC8ABEC3A7AB3009BCD1CBBD5E1EBE89466946C95A796798DAD17D0BE88E63B977B494CFFD8055C3C4F0BE1143ED829107FB706533E793C3D10C232908BFA30A95BA53A635F1C318A8B2ED54C2FD544738523BCC3CD9FF245BDE204846DEA1807CD97158D02F6488B5156B44C186F0C0EC71F3A7F06BFA2B9EE58D6DFB537CF09D563599AB9F6BDE959FA810D71D; __csrf=62aac4bde064780603a347d58ad80872',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'referer': 'https://music.163.com/',
    'user-agent': UserAgent().random,
}



def parse_comment_id(song_id):
    resp = requests.get('https://music.163.com/song?id=%s' % song_id, headers=headers)
    resp.encoding = 'utf-8'
    doc = etree.HTML(resp.text)
    tid = doc.xpath('//div[@id="comment-box"]/@data-tid')[0]
    return tid


def parse_comments(tid, page_num):
    try:
        data = {
            "rid": tid,
            "threadId": tid,
            "pageNo": str(page_num),
            "pageSize": "20",
            "cursor": int(time.time()*1000),
            "offset": (page_num - 1) * 20,
            "orderType":"1",
            "csrf_token":""
        }

        with open('encrypt_comment.js', 'r', encoding='utf-8') as f:
            content = f.read()

        ctx = execjs.compile(content)
        wb_data = ctx.call('encrypt_params', str(data))
        data = {
            'params': wb_data.get('encText'),
            'encSecKey': wb_data.get('encSecKey'),
        }
        search_api = 'https://music.163.com/weapi/comment/resource/comments/get?'
        params = {
            'csrf_token': ''
        }
        resp = requests.post(search_api, params=params, headers=headers, data=data)
        if resp.status_code == 200:
            items = resp.json().get('data').get('comments')
            for item in items:
                comment = item.get('content')
                print(comment)
        else:
            print(resp.status_code)
    except:
        print(f'url==={resp}')


def start(song_id):
    tid = parse_comment_id(song_id)
    for i in range(1,11):
        print('正在抓取第%s页评论...' % i)
        parse_comments(tid, i)


if __name__ == '__main__':
    start('1974443814')