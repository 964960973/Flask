import json
import random
import re
import threading
import time

import requests
import redis

redis_client = redis.Redis(host='127.0.0.1', port=6379)

def get_ip():
  proxy = ['http://5D1OsnsQ6JUZ:q5afKCYcs6ru@36.133.104.63:32080', 'http://wSszPfanZ5eW:641qnuJTJNSz@36.133.104.26:32080','http://MGv3HmBHv7Yb:AU4ZVU5DVkDx@36.133.103.174:32080','http://nC5D16KxZ5NA:4KkAOSHqEAFg@36.133.209.53:32080', 'http://YENEBBM7ZTSa:b60RKbb69w4P@36.138.63.10:32080','http://Jqg8E8FQEvP3:nXMmX7h5zKyT@36.133.103.186:32080']
  proxy = random.choice(proxy)
  return proxy



def get_goods_info():
    while True:
        key = redis_client.lpop("shein_work_8_19_list")
        data_info = redis_client.hget("shein_work_8_19",key).decode("utf-8")
        item = json.loads(data_info)
        url = "https://us.shein.com"+item["detail_url"]
        headers = {
            'authority': 'us.shein.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image1/avif,image1/webp,image1/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': 'language=en; cookieId=000BF5FC_FBAA_9EF4_6DE1_DE554A486AB2; cdn_key=uslang%3Dus; cate_channel_type=2; sessionID_shein=s%3ArC_D5G8KLm55-RS0kBIUni-AYuovFIaF.ZUwnYtEH%2Bwmm5%2Fy2JxjRdA16ibhtptF5PtkznZ4BVJk; bm_sz=CE37F08B6DFA68CDCC24B42B964FAE1F~YAAQBHDWF7HRp12BAQAA3JMfZhB6PIdhm/QoEqMWRzM9JzXrPA3I3O4PT3kEKpEQzmHUHUJXHUfMTV0yS+J3AFl02XMfAkMvTbzDWHotST+cy5RXQyryyzsFZ1ALfwLuhnRoULX8ntHyk0wGJZacbhbGOBZIDeYvf9ekr0morI63vP8D0J2C4NDsDJhIYPwQq2qTJ/75wS65V9h1vMnE4xUSSjKnjK4/Z5TMnGho2MyaRZeyljFRYJsu38u9fr7rVhQUdTdfi5hixvIlkL+ryltZZCMR2wWogaZR2zbHHzz5Fw==~3618869~4536385; sijssdk_2015_cross_new_user=1; sheindata2015jssdkcross=%7B%22distinct_id%22%3A%22181661f9fa6376-04499ab94671a34-613f5653-2073600-181661f9fa7982%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22181661f9fa6376-04499ab94671a34-613f5653-2073600-181661f9fa7982%22%7D; default_currency_expire=1; bi_session_id=bi_1655275760048_96162; app_country=CN; country=CN; countryId=44; ak_bmsc=5C6650C2487F8B511124773AEDCC7425~000000000000000000000000000000~YAAQBHDWF8vRp12BAQAAYacfZhCeOPoBLAScXYEtM/RbXiTClkYt7oWMVnd3VWFO3UOawOYt2+RIMaYzza29hzoWTfIoXxfcv56QmVU0uQbv4S8nkvqQxHNY+sdlzA66JynR53kZX36aRGHUerZkvuK3b0Gvfpx8IpV3p40VXnm/T9XkF9j1c+ThuCu9SAeYOJXQvKXHX24PoSLv2+AEgV0+8FO9eMNe5bWGJ7iLpTnaaQ1AiXHSqFZwc9PeZhipuBzbFX+ai5AsanHd/3USAB9XFwaGa6rpBucEPRqvwKZkc7+92EZqWiPRTQRvSAz8R0LRGsPLhuBkeOjIpsSneXnw+9QMi2uitfhdGQX/pHAkbmLTojSoy/jRbFnqxbPXE211a7s7V/KQD/tvds7ZYnrIS6/Cb+67c5jz8gD+rvWPrDwIovWiBDknL3476T4ojt8wPGRUQ437aZUpNomFZxjuREnQukTbbgXln/PLlk5aUzUi; _abck=98167658A70C934073ADAD735710CBF5~0~YAAQBHDWF9jRp12BAQAAFrAfZgiS8WgAcVYw5sRALLqEvqV2sJcixAOKG7x1H/TITO0g1N/UmEOY/231jiD3w2H0qbB2U/MGy/E0UEM5OMOiEBuc8VsaC8W3BINNm3jvfTAqVRioWFSE0AVYyoblwsKmkduJsjzk2a1kjbQpmBSaPd5pEtnVtmk9KbILYZsy2Qc5mB/m+jAg/kf4HScLhKDGUeQ+m/zTC3GL7x5zmpu5JaOGk+hwDJM+nA6fExad8Xp5EtKYhrSIxl+rxpkZW75ueCFYYhNngc0+Cdb4Jrbso/yfhmI3Ll83NvqpqjcQwaXERrxlZCs0zkOYlfDxghOTlxivTHw7lZm/K8vNKgYVCJ6RaLi1mqVX4eZdFolspA+RV3yfZiFYJAGewxIwzCkBW2gJS3s=~-1~||-1||~-1; smidV2=2022061514492179f881a61f52c0678ed41696f5c33cb100fbcf96609edd340; scarab.visitor=%22FC70CD3D763C5D1%22; hideCoupon=1; hideCouponWithRequest=1; hideCouponId_time=8533_1; have_show=1; SWITCH_LANGUAGE_GUIDE_ID=000BF5FC_FBAA_9EF4_6DE1_DE554A486AB2; ssrAbt=SellOutShow_type%3DB%23%23CccGoodsdetail_%23%23SellingPoint_type%3Dsellingpoint; fita.sid.shein=huTplT5Z7w7LYAusOV84a16ymtxHpmmc; scarab.profile=%2210785396%7C1655275848%22; _scid=3069424a-e503-4af6-8b72-fcb2f4bf06ed; __atuvs=62a9815b73791040000; __atuvc=1%7C24; _sctr=1|1655222400000; default_currency=USD; us_double_lang=us; currency=USD; banner_crowds_id=; bm_sv=8AD062CFCFCC981C115238F90FDE0D2D~YAAQBHDWF1lvqF2BAQAA97A3ZhCn/k1XQ374HTa+KTJseCsyZVP7ilScuRYdG/vL/Dhoo/JZ0nKD3L472Hz0efydwTjEHD5C3LPxDEF8s4ucdfSep6XwbJ3LRZlWS2YyzTqS1o33w51L2yNBC7HElwljCG4bvYEk5LksI/bPpUfBRtDG1PmamYDXRSCjhjm896i2YmkezBoLNKYz8EvOJPhhoehWbo66nan08eDwbRRbjHJP4HpvvS9OPCuPgQwd~1; RT="z=1&dm=shein.com&si=91bbaf90-c6b1-422b-8d5f-f26554a87391&ss=l4f8g2mi&sl=2&tt=2x29&rl=1&ld=y98b&r=etq3pkfb&ul=y98c"; _abck=98167658A70C934073ADAD735710CBF5~-1~YAAQhxAjFwTPhk+BAQAAvXAdawgXTY0WMGOfYHC5u84obr/Cf5CobFvaLoAFkEe366uedXc+kNfkTF3y+iWqEYf18w451yrcRkAIGL3Wxar/syEQ9kbnoVMEm7xomArfF5Y6Gu5TxzNBvOSsTgmNqugJ6Vut/ly1ocAvaBbs8EtGWPXga5P2gC4tBsBj8IGmhzmDVuDCx9ajko4mV9O0TSp1YYLBiEE7g4lbHj5jItxaRAOsfckQs2L1L+pVJv3CAF2LBaJxylkor1g24eb6tdFiX4lsTqctaTfMoq/yv/tHZeqD9EmjZy9o5fiPxKq/StFyGhvSjTNssMkYhOkYpaj19lCcF7Xh7I0mxNYZq78z52YZ/CNNz23qhk9W3tc104UIgvbOy3zdGRGCi/SVPnKjJ7G4TdM=~0~-1~-1; language=en',
            'if-none-match': 'W/"515cd-Jxbww3pa1mgOdXBXyX86l08QH3Q"',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36'
        }
        payload = {}
        proxy = get_ip()
        proxies = {"http":proxy,"https":proxy}
        try:
            # response = requests.get(url, headers=headers, data=payload,proxies = proxies,timeout=10)
            response = requests.get(url, headers=headers, data=payload,timeout=10)
            if response.status_code == 404:
                print("出错了")
                return
            if "productIntroData: " in response.text:
                data = response.text.split("productIntroData: ")[1]
                data_info = data.split('abt: ')[0]
                data_1 = data_info.strip()
                data_1 = data_1.strip(",")
                data_end = json.loads(data_1)
                commentInfo = data_end.get("commentInfo", "")
                item["comment"] = ""
                if commentInfo != {} and commentInfo != "":
                    item["comment"] = commentInfo["comment_num"]
                    item["comment"] = commentInfo["comment_rank_average"]
                redis_client.hset("shein_work_hash", item["goods_name"], json.dumps(item))
                print(f"保存商品信息成功 goods_name == {item['goods_name']}")
        except:
            redis_client.rpush("shein_work_8_19_list",key.decode("utf-8"))
            print("获取评论失败")
            continue

def get_image(url,goods_id):
      url = url
      headers={
          "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"
      }
      response = requests.get(url,headers=headers).content
      with open(f"./image1/{goods_id}.jpg","wb") as f:
          f.write(response)
      return




def get_comment_time():
    for page in range(11):
        url = f"https://us.shein.com/pdsearch/printed%20crop%20tops/?ici=s1%60EditSearch%60printed%20crop%20tops%60_fb%60d0%60PageHome&scici=Search~~EditSearch~~1~~printed_20crop_20tops~~~~0&src_identifier=st%3D2%60sc%3Dprinted%20crop%20tops%60sr%3D0%60ps%3D1&src_module=search&src_tab_page_id=page_home1660893692041&page={page}"
        payload = {}
        headers = {
            'authority': 'us.shein.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image1/avif,image1/webp,image1/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': 'language=en; cookieId=000BF5FC_FBAA_9EF4_6DE1_DE554A486AB2; cate_channel_type=2; sheindata2015jssdkcross=%7B%22distinct_id%22%3A%22181661f9fa6376-04499ab94671a34-613f5653-2073600-181661f9fa7982%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22181661f9fa6376-04499ab94671a34-613f5653-2073600-181661f9fa7982%22%7D; country=CN; countryId=44; smidV2=2022061514492179f881a61f52c0678ed41696f5c33cb100fbcf96609edd340; scarab.visitor=%22FC70CD3D763C5D1%22; SWITCH_LANGUAGE_GUIDE_ID=000BF5FC_FBAA_9EF4_6DE1_DE554A486AB2; ssrAbt=SellOutShow_type%3DB%23%23CccGoodsdetail_%23%23SellingPoint_type%3Dsellingpoint; fita.sid.shein=huTplT5Z7w7LYAusOV84a16ymtxHpmmc; scarab.profile=%2210785396%7C1655275848%22; _scid=3069424a-e503-4af6-8b72-fcb2f4bf06ed; _ga=GA1.2.131069021.1655444714; _aimtellSubscriberID=f3630239-bd3b-7cb0-8d28-a4c20d54baab; sessionID_shein=s%3Aej2f4S-qgaF7NBh59u744OWaEHKfQM97.hz%2FD7IwYlvsx9BLQgMg6baAFAq2HaFDKlDOxfcXH8B4; _gid=GA1.2.1762506458.1655706191; _pin_unauth=dWlkPU1UaGlOVGM1TW1NdE1qSmxOaTAwWmpCbExXRmlOR1F0WlRKak0yTXpOV1ZrTldRMA; hideCoupon=1; hideCouponWithRequest=1; hideCouponId_time=8538_2; REVIEW_LIKE_TIPS=1; _clck=zz0ukp|1|f2j|0; _sctr=1|1655827200000; bm_sz=4AEBF6ACD1064682C5BEFB92966CC78B~YAAQyqDVF1OfgoaBAQAAqa8DihADx2143EFzsfOrGLdGssV9DY4tLTcYM/jSWvxuj7yzQRgxIZgXkRphpoie1ImKpyukvLDKR9rZziBjjS9X4CWDsR8DS+T5klk4Kv21Rr4UlM0Iw7XTs/DMBwis8GDJ/iqczdhUHdlfPCYYSB9nfG0nktKJp0Cf/8d2g4aAE4YQmNfxltOZqabKYb33If9JOwfUPwOP3Vcpkv5384F0PrfZ1li3WrWyt6MedyezEQqRGdN5saueIKEzYACci6pdF7QybPhynpMoFPezJqittFzBdiijfdSQ14O2gujN/VsBlOto1mX0eA==~4471110~4535620; bi_session_id=bi_1655880419520_76164; bm_mi=B015E89F6DDAC02AE30DAC3BEE180315~YAAQFq08F3hunTSBAQAAwQcqihBGEsNF3fLlQvdMcQupvy3y3Oh0mjEFEIVtP9Pepmqm/EgXotKHRc/A6qPcI07L+w+gVcWCVMpX9CERqrGvMH5tIGHPF7+Auh0ZtAacgx5kdJ++8/B2wNQmXersVtJd2BCd1T5qtib0Gwezb3+WIZWoIjdhBiMrpqgR+mZzKHVtipxv6UmGksywNDJR33wnN2ju2Fm1d9uzQmbcHQsk+zjRKpxP1ehJ/2FAaDj68MhRnCfPtBHxyz+y4z7Jqafp9A5GsowKhGZRzGC1/AUjuhtslHbJ/O+Ukv0lYbyyDPfOFwLnZNCt7VcVuoX18xeXY/ftDWHr+DGv2YqyBprOttkk/wYS6pznCJcMnqRkW7vXsDM5jB8CrRigi6LOTFMmp/sq3/AIfV8WtS2uW1o=~1; us_double_lang=us; currency=USD; default_currency_expire=1; ak_bmsc=B4428B5D7F29A7F8109494E6A44CA073~000000000000000000000000000000~YAAQFq08F8NxnTSBAQAAqRkqihBKgZw4ootLRFXrqKnjOqnhlEqUxckPXWvng+qkkWw1WMHhk0Gl5RriSJxrDc3bYoU9T1644uutqe1pLEeAnwdtE7qPFxKTTOhKZo9KUVyrf9mTbonZ8aiz41m5AbgrAUrBsvyIYfGIvMmE76nZqc1QnPDJQRvK75MBU1v78Xek9SC1lkTBUUwIRM1zQczfJTjfiaUEmtR/UQLNmaHBQJ15ppMGLD0542BYoNH499ITW7Kb6hlbaz5gPz88kEbxw6KynHhn1f5qPAtxwXPN+S0UYdVhl8zdJQnw+dkIcYf7SIA6b+3qyrxTysd4nlC7F5hGDLnktrEkts1lrdLbgwGLaIWlO6bHkg06aMp+/EwuKTK6cT0TdMVUv5YUOtFdswQG4hFUY3ZGu1pfzIkfzRST3qotEchx5nxqzRl7iYuX3BMO4gnyFAdMRLFHVzlN1mRAnbIV23fLO77Ag3+x/ES+tSsGTn7DNpV5hKFLlegYGbnQ809nHIjMM+k=; have_show=1; cdn_key=uslang%3Dus; default_currency=USD; outbrain_cid_fetch=true; addressCookie=%7B%22countryId%22%3A%22226%22%2C%22createdTime%22%3A1655881082663%2C%22isUserHandle%22%3A%220%22%2C%22siteUid%22%3A%22us%22%7D; __atuvs=62b2bb546a8d2b20002; __atuvc=8%7C24%2C47%7C25; _uetsid=b473b210f06111eca1e46f4885ee48df; _uetvid=1ebada30ee0a11eca6ca3b528f0b5bfe; _clsk=1ijvecm|1655881145339|8|0|j.clarity.ms/collect; _gat_shein=1; OptanonAlertBoxClosed=2022-06-22T06:59:08.764Z; OptanonConsent=isIABGlobal=false&datestamp=Wed+Jun+22+2022+14%3A59%3A09+GMT%2B0800+(GMT%2B08%3A00)&version=6.13.0&hosts=&consentId=beee70eb-c6ea-4f07-8d98-9ac9ccabe360&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=CN%3BGD; banner_crowds_id=; cto_bundle=41RSyV94RFJtdHVBbnNaY3EwNEQlMkZWdUVyaWJ1blFvRlBsTzljaFdheTVCd2hJQXJIR3R1dXdCZ3NCRmtQSiUyQm14Z0xhWXZNTEpNalpQNjU2NWQ4QnQ5RnMlMkZYT1V4VEtlTjRiemtuSEY1VmJpaWh4QVN6T2Fsd0N0V2UzNmhLdTJNcFYwN2t2d1k5MHRIZ2ZMUmNMc0NYcVo4YlElM0QlM0Q; _abck=98167658A70C934073ADAD735710CBF5~0~YAAQZYzQFwqy7YmBAQAATDU1igh0ZTwbTPjR7rzTkoyIO4xoMvhEWo4w3P50FWQO8PmTu1zJ+hbvX79FbsMX3DqvvgyLQBjGYs1O94Qf0hxQ2uZtDEFmKx20UY8cMJRDTa4eFGjI8xx7S6/zSWcxE4lsE+3CSYoaIkzsD+74JoUFEA6YSay3PkD0dnaLXdpdVr/AqtFpjQJFiVN4a4dyldAEpC/zn2ub7p2jBvRPDmamhzoQPIDo6jqSTKgrc3gGGsRQIjN0j/KQM5IDcIGPPEm5c1RUtPyR1+dgu6aemq7CydhFcLDFE0ggsNMcU6zixIAhIwa3uxo/z0JEIEkaLej6kyOh0YTaBhn/PmaYz3/cyzj90AR0WX6dnf52~-1~-1~-1; bm_sv=E1B9E2F21ED16494B111E595DF8DF244~YAAQZYzQFwuy7YmBAQAATDU1ihDyPHhHeUBxA6oObyJPj+fUTqFnCpvOviN6a3qKyMZPPhbYpEMAI/kvxuNUU6d9GV0u1XsX6iGdwzy60gDc1BD6MJBUTSdu4vpX2C2lyzYO4WOykJk1XETNDE2HofFSEv86eclIscTkrMrZSWb+aXEiL7EOC7rOr8u1DDusjTn57sUAYAlwqIRan/FDHwH+XCLf6ZdziQSkwtpx28z0ez4MdjXpwiw4e5+BG5UkTg==~1; RT="z=1&dm=shein.com&si=91bbaf90-c6b1-422b-8d5f-f26554a87391&ss=l4p8hua4&sl=9&tt=3iwg&obo=2&rl=1&nu=hidrnm4k&cl=dyve&ld=e3sj&r=15dd21asj&ul=e3sk"; _abck=98167658A70C934073ADAD735710CBF5~-1~YAAQPHJCF1Nl8YiBAQAAUzA9pAjUWaKOok+llPNAdsiqTBu9tyZOI0acA0E3eRQQGlKwRTt+C6JsePu8lkVTscyx+1QcuIKVXK2eCRrP4l3KGy1jqbBii3ww+HpGowUAXT3/zFGYW8fzoBln5uyM3/CKTqVg2rVTU9kaXHICBQlYqtuRAJgTXx1d55p9TS6xrIdHEr4SoFo7Q0CyoKo5yFqb/N3rskKtRVEsEupghpH5Ei49Kr8fgzq8mCAQd7SDR/CEkf59kuC2viz8NixvQiNxnLo1d4sSLuSxHArCVMoya2cJsYzINSbsI6S+kxz80DgvKENAiJY3iMylaYOQKQDGX/EtcPVAWOm9se/bf3+37PbVh7ebUo7zzngF~0~-1~-1; cate_channel_type=2; cdn_key=uslang%3Dus; cookieId=2EBD7C53_B54D_2A34_298E_D585E0A2A45D; language=en; sessionID_shein=s%3AXllMQn1j3utCU0b8lmJnG1I3lVnIZ4vF.i6mBDjzL%2Bjr%2F4tbuog5c5lygcr56xbLBC1SI2SxIwTY',
            'referer': 'https://us.shein.com/Clothing-c-2030.html?ici=us_tab01navbar05&scici=navbar_WomenHomePage~~tab01navbar05~~5~~webLink~~~~0&src_module=topcat&src_tab_page_id=page_goods_group1655867750143&src_identifier=fc%3DWomen%60sc%3DCLOTHING%60tc%3D0%60oc%3D0%60ps%3Dtab01navbar05%60jc%3Durl_https%253A%252F%252Fus.shein.com%252FClothing-c-2030.html&srctype=category&userpath=category-CLOTHING&child_cat_id=1773',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36'
        }
        proxy = get_ip()
        proxies = {"http":proxy,"https":proxy}
        try:
            response = requests.get(url, headers=headers, data=payload,timeout=10,proxies = proxies)
            if "var gbProductListSsrData = " in response.text:
                data_info = json.loads(response.text.split("var gbProductListSsrData = ")[1].split("</script")[0])
                results = data_info["results"]
                goods_list = results["goods"]
                for goods_info in goods_list:
                    item = {}
                    item["productRelationID"] = goods_info["productRelationID"]
                    item["goods_id"] = goods_info["goods_id"]
                    item["goods_name"] = goods_info["goods_name"]
                    item["goods_img"] = goods_info["goods_img"]
                    item["detail_url"] = goods_info["detail_url"]
                    redis_client.hset("shein_work_8_19",item["goods_name"],json.dumps(item))
                    redis_client.lpush("shein_work_8_19_list",item["goods_name"])
                    print(f"存储商品信息成功 goods_name== {item['goods_id']}")
        except:
            print(f"失败,page == {page}")
            continue


get_comment_time()
def run():
    pass
    # get_goods_info()

#
if __name__ == "__main__":
    print(f'主线程开始时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')
    # 初始化3个线程，传递不同的参数
    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run)
    t3 = threading.Thread(target=run)
    # 开启三个线程
    t1.start()
    t2.start()
    t3.start()
    # 等待运行结束
    t1.join()
    t2.join()
    t3.join()
    print(f'主线程结束时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')