import requests


url = 'https://www.baidu.com/'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71'
}


resp = requests.get(url=url,headers=headers).text
print(resp)
