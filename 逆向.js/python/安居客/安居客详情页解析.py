from lxml import etree
import requests
from fake_useragent import UserAgent
import random
import time
import csv
import re
 
 
## 创建文件对象
with open('安居客测试.csv','w') as csvfile:
    fieldnames=['小区名称','价格','物业类型','权属类别','竣工时间','产权年限','总户数','总建面积','容积率','绿化率','建筑类型','所属商圈','统一供暖','供水供电','停车位','物业费','停车费','车位管理费','物业公司','小区地址','开发商','商圈均价']
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
#二手房源小区详情页爬取
    url='https://yt.anjuke.com/community/view/793375'
    headers={
        'cookie': 'SECKEY_ABVK=uY3Yij4RZwxyZ6u+a6PQRRxYbQvALpWRrtvCfsDmtj4%3D; BMAP_SECKEY=GbSWmU9wvNA7MiUWzXwalfC0rye43gfl_sNUQ_DusdTlvpUmZhPdlU7bsxC0djOVMQlc-s9x7AYPNvPBePZDdYnuq9JG0EGs1s-30t9jPx7XrJJ2UgHvchouy-d42IEeA0_Gk7wQtZYfr6fMBt_4gnk9-n9RifirTBba05LoO_lkYF6D81w_qSc97WhaYnTD; aQQ_ajkguid=94CEA707-AE51-1E30-B1C7-C63E24CDCA6F; ajk-appVersion=; seo_source_type=0; id58=CroD4GMm1MM5vsivbVwwAg==; wmda_uuid=f1b5b397af7cdde2605a725a9ae91dd4; wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; 58tj_uuid=9ee833cf-f280-4a44-a9e4-5c141bd182d1; als=0; _ga=GA1.2.808255216.1663492352; _gid=GA1.2.1932705920.1663492352; isp=true; sessid=6C070F52-0D4C-49B8-A900-95A916722A8E; ctid=47; fzq_h=b1dcc1022189bd9fda1bf9f65879d995_1663673987062_3a0818323e6945d6a418644d88350986_3747688837; xxzl_cid=ccd9cfc7462340a99b704f26a7669d83; xzuid=4db3ea76-bd29-4a64-a2a5-0d6898e2d356; new_uv=16; twe=2; fzq_js_anjuke_ershoufang_pc=99fd376318e699b0095742d972a9f7ea_1663686309412_24; obtain_by=2; fzq_js_anjuke_xiaoqu_pc=87fb3e457bed45372295aa3f9af6cdc4_1663686341588_25; xxzl_cid=ccd9cfc7462340a99b704f26a7669d83; xxzl_deviceid=g9kJo9Jl3n0pmVhzfljdGh0sC5fbKBR46lOS0ZrE14piIN8W7JRI4Be0Vvd4kajN',
        'user-agent': str(UserAgent().random)
        }
    response=requests.get(url,headers=headers)
    result=response.text
    #拿到小区详情页html代码
    data_info = []
    data_list = []
    #对代码进行xpath提取,提取过程中需要将/n去除掉
    rp= etree.HTML(result)
    dict_result = {'小区名称': '-','价格': '-','物业类型': '-','权属类别': '-',
                       '竣工时间': '-','产权年限': '-','总户数': '-','总建面积': '-',
                       '容积率': '-','绿化率': '-','建筑类型': '-',
                       '所属商圈': '-','统一供暖':'-','供水供电':'-',
                       '停车位': '-','物业费': '-','停车费': '-',
                       '车位管理费': '-','物业公司': '-','小区地址':'-','开发商':'-',
                       '商圈均价':'-'}
                       #'在售房源': '-','在租房源': '-','小区问答':'-',
    dict_result['小区名称'] = rp.xpath('//h1[@class="title" and @data-v-4b6e9cfc=""]/text()')
    dict_result['价格'] = rp.xpath('//span[@class="average" and @data-v-8fb690fe=""]/text()')
    dict_result['物业类型'] = rp.xpath('//div[@class="value value_0" and @data-v-d35e765c=""]/text()')
    dict_result['权属类别'] = rp.xpath('//div[@class="value value_1" and @data-v-d35e765c=""]/text()')
    dict_result['竣工时间'] = rp.xpath('/html/body/div[1]/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div[2]/div[1]/text()')
    dict_result['产权年限'] = rp.xpath('//div[@class="value value_3" and @data-v-d35e765c=""]/text()')
    dict_result['总户数'] = rp.xpath('//div[@class="value value_4"  and @data-v-d35e765c=""]/text()')
    dict_result['总建面积'] = rp.xpath('//div[@class="value value_5" and @data-v-d35e765c=""]/text()')
    dict_result['容积率'] = rp.xpath('//div[@class="value value_6"  and @data-v-d35e765c=""]/text()')
    dict_result['绿化率'] = rp.xpath('//div[@class="value value_7" and @data-v-d35e765c=""]/text()')
    dict_result['建筑类型'] = rp.xpath('//div[@class="value value_8" and @data-v-d35e765c=""]/text()')
    dict_result['所属商圈'] = rp.xpath('//div[@class="value value_9" and @data-v-d35e765c=""]/text()')
    dict_result['统一供暖'] = rp.xpath('//div[@class="value value_10" and @data-v-d35e765c=""]/text()')
    dict_result['供水供电'] = rp.xpath('//div[@class="value value_11" and @data-v-d35e765c=""]/text()')
    dict_result['停车位'] = rp.xpath('//div[@class="value value_12" and @data-v-d35e765c=""]/text()')
    dict_result['物业费'] = rp.xpath('//div[@class="value value_13" and @data-v-d35e765c=""]/text()')
    dict_result['停车费'] = rp.xpath('//div[@class="value" and @data-v-8fb690fe=""]/text()')
    dict_result['车位管理费'] = rp.xpath('/html/body/div[1]/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[16]/div[2]/text()')
    dict_result['物业公司'] = rp.xpath('/html/body/div[1]/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[17]/div[2]/text()')
    dict_result['小区地址'] = rp.xpath('//p[@class="sub-title" and @data-v-4b6e9cfc=""]/text()')
    dict_result['开发商'] = rp.xpath('/html/body/div[1]/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[19]/div[2]/text()')
    #dict_result['在售房源'] = rp.xpath(
    #dict_result['在租房源'] = rp.xpath(
    #dict_result['小区问答'] = rp.xpath('//li[]/text()')
    dict_result['商圈均价'] = rp.xpath('//*[@id="fangjia"]/div[2]/div[2]/div/div[1]/div[1]/span[1]/text()')

    for key,value in dict_result.items():
            value = list(map(lambda item: re.sub('\s+', '', item), value))  # 去掉换行符制表符,这里一定要是\s就是要橙色方块突出
            dict_result[key] = list(filter(None, value)) # 去掉上一步产生的空元素
            if len(dict_result[key]) == 0:
                dict_result[key] = ''
                data_info.append(dict_result)
            else:
                dict_result[key] = dict_result[key][0]#去除方括号
                data_info.append(dict_result)
    print(dict_result)
    print(type(dict_result))
    writer.writerow(dict_result)
    # for i in data_info:
    #     writer.writerow(i)
    print('插入成功')
    t=random.uniform(6,14)
    time.sleep(t)
    print('全部插入完毕')



