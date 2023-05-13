import time
import jieba
import functools
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
from ..templates.recruit.sql_help import db
from flask import Blueprint, session, redirect, url_for, render_template, request

Recruit = Blueprint('recruit', __name__)


def drecruit_a(region, pos):
    list = []
    info_1 = db.fetchall(f'select 工资信息 from boss_{region}_{pos}')
    for aa in info_1:
        if 'K' in str(aa):
            money = str(aa).split('K')[0][2:]
            a1 = int(str(money.split('-')[0]))
            a2 = int(str(money.split('-')[1]))
            a3 = int((a1 + a2) / 2)
            list.append(a3)
    # 平均值
    mean = int(float(np.mean(list)))
    # 中位数
    median = int(np.median(list))
    info = {}
    dataList = []
    info[">3k"] = info["3-5k"] = info["5-8k"] = info["8-10k"] = info["10-12k"] = info['12-15k'] = \
        info['15-18k'] = info["18-22k"] = info["22-28k"] = info["28-32k"] = info[">32k"] = 0
    for money in list:
        if int(money) < 3:
            info[">3k"] = int(info[">3k"] + 1)
        elif 3 < int(money) <= 5:
            info["3-5k"] = int(info["3-5k"] + 1)
        elif 5 < int(money) <= 8:
            info["5-8k"] = int(info["5-8k"] + 1)
        elif 8 < int(money) <= 10:
            info["8-10k"] = int(info["8-10k"] + 1)
        elif 10 < int(money) <= 12:
            info["10-12k"] = int(info["10-12k"] + 1)
        elif 12 < int(money) <= 15:
            info["12-15k"] = int(info["12-15k"] + 1)
        elif 15 < int(money) <= 18:
            info["15-18k"] = int(info["15-18k"] + 1)
        elif 18 < int(money) <= 22:
            info["18-22k"] = int(info["18-22k"] + 1)
        elif 22 < int(money) <= 28:
            info["22-28k"] = int(info["22-28k"] + 1)
        elif 28 < int(money) <= 32:
            info["28-32k"] = int(info["28-32k"] + 1)
        else:
            info[">32k"] = int(info[">32k"] + 1)
    for item in info.items():
        dataList.append({"value": item[1], "name": item[0]})
    return dataList, mean, median
    # for data in dataList:
    #     data = data


def drecruit_histogram_average_salary_1(list):
    data_mean = []
    data_median = []
    pose = []
    max_2 = []
    min_2 = []
    for i in list:
        pose.append(str(i).split('_')[1])
        data = i[0]
        mean = []
        jobs = db.fetchall(f'select 工资信息 from {data}')
        oser = []
        for aa in jobs:
            if 'K' in str(aa):
                money = str(aa).split('K')[0][2:]
                a1 = int(str(money.split('-')[0]))
                a2 = int(str(money.split('-')[1]))
                a3 = int(float((a1 + a2) / 2))
                mean.append(a3)
        # 平均值
        opp = int(np.mean(mean))
        data_mean.append(opp)
        # 中位数
        data_median.append(int(np.median(mean)))
        max_1 = max(mean)
        if max_1 >= 70:
            max_1 = 70
        min_1 = min(mean)
        max_2.append(max_1)
        min_2.append(min_1)
    return data_mean, data_median, pose, max_2, min_2


def drecruit_histogram_average_salary_2(list):
    data_mean = []
    data_median = []
    pose = []
    max_2 = []
    min_2 = []
    for i in list:
        pose.append(str(i).split("_")[-1].split("'")[0])
        mean = []
        data = i[0]
        jobs = db.fetchall(f'select 工资信息 from {data}')
        oser = []
        for aa in jobs:
            if 'K' in str(aa):
                money = str(aa).split('K')[0][2:]
                a1 = int(str(money.split('-')[0]))
                a2 = int(str(money.split('-')[1]))
                a3 = int(float((a1 + a2) / 2))
                mean.append(a3)
        # 平均值
        opp = int(float(str(float(np.mean(mean))).split('.')[0]))
        data_mean.append(opp)
        # 中位数
        data_median.append(int(np.median(mean)))
        max_1 = max(mean)
        if max_1 >= 70:
            max_1 = 70
        min_1 = min(mean)
        max_2.append(max_1)
        min_2.append(min_1)
    return data_mean, data_median, pose, max_2, min_2


def pie_chart_function(region, pos):
    info = {}
    dataList = []
    info["小学学历"] = info["初中学历"] = info["高中学历"] = info["中专学历"] = info["大专学历"] = info['本科学历'] = \
        info['硕士学历'] = info["博士学历"] = 0
    info_1 = db.fetchall(f'select 工资信息 from boss_{region}_{pos}')
    for education in info_1:
        if '小学' in str(education):
            info["小学学历"] = int(info["小学学历"] + 1)
        elif '初中' in str(education):
            info["初中学历"] = int(info["初中学历"] + 1)
        elif '高中' in str(education):
            info["高中学历"] = int(info["高中学历"] + 1)
        elif '中专' in str(education):
            info["中专学历"] = int(info["中专学历"] + 1)
        elif '大专' in str(education):
            info["大专学历"] = int(info["大专学历"] + 1)
        elif '本科' in str(education):
            info["本科学历"] = int(info["本科学历"] + 1)
        elif '硕士' in str(education):
            info["硕士学历"] = int(info["硕士学历"] + 1)
        elif '博士' in str(education):
            info["博士学历"] = int(info["博士学历"] + 1)
    for item in info.items():
        dataList.append({"value": item[1], "name": item[0]})
    return dataList


def Work_Experience(region, pos):
    info = {}
    Experience = []
    info["1-3年"] = info["3-5年"] = info["5-10年"] = info["经验不限"] = info["在校"] = info['应届'] = \
        info['1年以内'] = info['10年以上'] = 0
    info_1 = db.fetchall(f'select 工资信息 from boss_{region}_{pos}')
    for education in info_1:
        if '1-3年' in str(education):
            info["1-3年"] = int(info["1-3年"] + 1)
        elif '3-5年' in str(education):
            info["3-5年"] = int(info["3-5年"] + 1)
        elif '5-10年' in str(education):
            info["5-10年"] = int(info["5-10年"] + 1)
        elif '经验不限' in str(education):
            info["经验不限"] = int(info["经验不限"] + 1)
        elif '在校' in str(education):
            info["在校"] = int(info["在校"] + 1)
        elif '应届' in str(education):
            info["应届"] = int(info["应届"] + 1)
        elif '1年以内' in str(education):
            info["1年以内"] = int(info["1年以内"] + 1)
        elif '10年以上' in str(education):
            info["10年以上"] = int(info["10年以上"] + 1)
    for item in info.items():
        Experience.append({"value": item[1], "name": item[0]})
    return Experience


def Information(region, pos):
    info = {}
    information = []
    info["0-20人"] = info["20-99人"] = info["100-499人"] = info["1000-9999人"] = info["10000人以上"] = 0
    info_1 = db.fetchall(f'select 企业信息 from boss_{region}_{pos}')
    for education in info_1:
        if '0-20人' in str(education):
            info["0-20人"] = int(info["0-20人"] + 1)
        elif '20-99人' in str(education):
            info["20-99人"] = int(info["20-99人"] + 1)
        elif '100-499人' in str(education):
            info["100-499人"] = int(info["100-499人"] + 1)
        elif '1000-9999人' in str(education):
            info["1000-9999人"] = int(info["1000-9999人"] + 1)
        elif '10000人以上' in str(education):
            info["10000人以上"] = int(info["10000人以上"] + 1)
    for item in info.items():
        information.append({"value": item[1], "name": item[0]})
    return information


def regional_proportion(region, pos):
    mansge_list = []
    info = {}
    regional = []
    regional_proportion_list = []
    info_1 = db.fetchall(f'select 所在地区 from boss_{region}_{pos}')
    for education in info_1:
        try:
            proportion = str(education).split('·')[1]
        except:
            proportion = str(region) + '暂无明确表明地区'
        if proportion not in mansge_list:
            mansge_list.append(proportion)
        regional.append(proportion)
    for name in mansge_list:
        info[name] = regional.count(name)
    for item in info.items():
        regional_proportion_list.append({"value": item[1], "name": item[0]})
    return regional_proportion_list


def Word_cloud_image(region, pos):
    info_1 = db.fetchall(f'select 福利待遇 from boss_{region}_{pos}')
    text = ""
    for item in info_1:
        text = text + item[0]

    cut = jieba.cut(text)
    string = ' '.join(cut)
    img = Image.open(r'./good_link/static/image/word.jpg')
    img_array = np.array(img)  # 将图片转换为数组
    wc = WordCloud(
        background_color='white',
        mask=img_array,
        font_path='msyh.ttc'
    )
    wc.generate_from_text(string)

    # 绘制图片
    fig = plt.figure(1)
    plt.imshow(wc)
    plt.axis('off')  # 是否显示坐标轴

    # plt.show()  # 显示生成的词云图片

    # 输出词云图片到文件
    image = f'/static/image/boss_{region}_{pos}_福利待遇.png'
    plt.savefig(f'./good_link/static/image/boss_{region}_{pos}_福利待遇', dpi=500)
    return image


def Word_cloud_image_1(region, pos):
    info_1 = db.fetchall(f'select 所需技术 from boss_{region}_{pos}')
    text = ""
    for item in info_1:
        text = text + item[0]

    cut = jieba.cut(text)
    string = ' '.join(cut)
    img = Image.open(r'./good_link/static/image/word.jpg')
    img_array = np.array(img)  # 将图片转换为数组
    wc = WordCloud(
        background_color='white',
        mask=img_array,
        font_path='msyh.ttc'
    )
    wc.generate_from_text(string)

    # 绘制图片
    fig = plt.figure(1)
    plt.imshow(wc)
    plt.axis('off')  # 是否显示坐标轴

    # plt.show()  # 显示生成的词云图片

    # 输出词云图片到文件
    required_Technology = f'/static/image/boss_{region}_{pos}_所需技术.png'
    plt.savefig(f'./good_link/static/image/boss_{region}_{pos}_所需技术', dpi=500)
    return required_Technology


def Word_cloud_image_2(region, pos):
    info_1 = db.fetchall(f'select 职位 from boss_{region}_{pos}')
    text = ""
    for item in info_1:
        text = text + item[0]

    cut = jieba.cut(text)
    string = ' '.join(cut)
    img = Image.open(r'./good_link/static/image/word.jpg')
    img_array = np.array(img)  # 将图片转换为数组
    wc = WordCloud(
        background_color='white',
        mask=img_array,
        font_path='msyh.ttc'
    )
    wc.generate_from_text(string)

    # 绘制图片
    fig = plt.figure(1)
    plt.imshow(wc)
    plt.axis('off')  # 是否显示坐标轴

    # plt.show()  # 显示生成的词云图片

    # 输出词云图片到文件
    city = f'/static/image/boss_{region}_{pos}_职位.png'
    plt.savefig(f'./good_link/static/image/boss_{region}_{pos}_职位', dpi=500)
    return city


def auth(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        user_name = session.get('aaaaa')
        if not user_name:
            return redirect(url_for('wy.lo'))
        return func(*args, **kwargs)

    return inner


@Recruit.route('/recruit', methods=["GET", "POST"])
@auth
def recruit():
    jobs = db.fetchall('select * from boss_全国_爬虫')
    nid = db.tables('SHOW TABLES')
    regions = []
    post = []
    for id in nid:
        try:
            data = str(id).split('_')[1].split('_')[0]
            data_1 = str(id[0]).split('_')[-1]
            post.append(data_1)
            regions.append(data)
        except:
            continue
    return render_template('./recruit/demo.html', jobs=jobs, regions=set(regions), post=set(post))


@Recruit.route('/recruit_index', methods=["GET", "POST"])
@auth
def recruit_index():
    region = request.args.get('region')
    pos = request.args.get('pos')
    if region == '':
        region = '全国'
    if pos == '':
        pos = '爬虫'
    try:
        jobs = db.fetchall(f'select * from boss_{region}_{pos}')
    except:
        jobs = db.fetchall(f'select * from boss_全国_{pos}')

    nid = db.tables('SHOW TABLES')
    regions = []
    post = []
    for id in nid:
        try:
            data = str(id).split('_')[1].split('_')[0]
            data_1 = str(id[0]).split('_')[-1]
            post.append(data_1)
            regions.append(data)
        except:
            continue
    return render_template('./recruit/demo.html', regions=set(regions), post=list(set(post)), region=region, pos=pos,
                           jobs=jobs)


@Recruit.route('/drecruit_histogram', methods=["GET", "POST"])
@auth
def drecruit_histogram():
    names = []
    values = []
    region = request.args.get('region')
    pos = request.args.get('pos')
    if region == '':
        region = '全国'
    if pos == '':
        pos = '爬虫'
    try:
        jobs = db.fetchall(f'select * from boss_{region}_{pos}')
    except:
        jobs = db.fetchall(f'select * from boss_全国_{pos}')

    nid = db.tables('SHOW TABLES')
    regions = []
    post = []
    for id in nid:
        try:
            data = str(id).split('_')[1].split('_')[0]
            data_1 = str(id[0]).split('_')[-1]
            post.append(data_1)
            regions.append(data)
        except:
            continue
    if region == '':
        region = '全国'
    if pos == None or pos == '':
        pos = '爬虫'
    dataList, mean, median = drecruit_a(region, pos)
    for oser in dataList:
        name = oser['name']
        names.append(name)
        value = oser['value']
        values.append(value)
    return render_template('./recruit/histogram_money.html', names=names, values=values, regions=set(regions),
                           post=list(set(post)), region=region, pos=pos, jobs=jobs, mean=mean, median=median)


@Recruit.route('/drecruit_histogram_average_salary', methods=["GET", "POST"])
@auth
def drecruit_histogram_average_salary():
    pos = request.args.get('pos')
    post = []
    if pos == '' or pos == None:
        pos = '爬虫'
    nid = db.tables('SHOW TABLES')
    list = []
    for id in nid:
        try:
            if pos in str(id):
                list.append(id)
            elif pos not in (id):
                data_1 = str(id[0]).split('_')[-1]
                post.append(data_1)
            continue
        except:
            continue
    data_mean, data_median, pose, max, min = drecruit_histogram_average_salary_1(list)
    return render_template('./recruit/histogram_money_max_min.html', data_mean=data_mean, data_median=data_median,
                           post=set(post), max=max, min=min, pose=pose, pos=pos)


@Recruit.route('/drecruit_histogram_average_city', methods=["GET", "POST"])
@auth
def drecruit_histogram_average_city():
    region = request.args.get('region')
    regions = []
    if region == '' or region == None:
        region = '全国'
    nid = db.tables('SHOW TABLES')
    list = []
    for id in nid:
        try:
            if region in str(id):
                list.append(id)
            data_1 = str(id).split('_')[1]
            regions.append(data_1)
            continue
        except:
            continue
    data_mean, data_median, pose, max, min = drecruit_histogram_average_salary_2(list)
    return render_template('./recruit/histogram_money_max_min_city.html', data_mean=data_mean, data_median=data_median,
                           regions=set(regions), max=max, min=min, pose=pose, region=region)


@Recruit.route('/drecruit_Pie', methods=["GET", "POST"])
@auth
def drecruit_Pie():
    region = request.args.get('region')
    pos = request.args.get('pos')

    if region == '':
        region = "全国"
    if pos == '' or pos == None:
        pos = 'python'
    nid = db.tables('SHOW TABLES')
    regions = []
    post = []
    dataList = pie_chart_function(region, pos)
    Experience = Work_Experience(region, pos)
    information = Information(region, pos)
    regional_proportion_list = regional_proportion(region, pos)
    for id in nid:
        try:
            data = str(id).split('_')[1].split('_')[0]
            data_1 = str(id).split("_")[-1].split("'")[0]
            regions.append(data)
            post.append(data_1)
        except:
            continue
    return render_template('./recruit/drecruit_Pie.html', dataList=dataList, Experience=Experience,
                           information=information, regional_proportion_list=regional_proportion_list,
                           regions=set(regions), post=set(post), region=region, pos=pos)


@Recruit.route('/Word_cloud_diagram', methods=["GET", "POST"])
@auth
def Word_cloud_diagram():
    region = request.args.get('region')
    pos = request.args.get('pos')
    if region == '' or region == None:
        region = "全国"
    if pos == '' or pos == None:
        pos = 'python'
    nid = db.tables('SHOW TABLES')
    regions = []
    post = []
    image = Word_cloud_image(region, pos)
    required_Technology = Word_cloud_image_1(region, pos)
    city = Word_cloud_image_2(region, pos)
    for id in nid:
        try:
            data = str(id).split('_')[1].split('_')[0]
            data_1 = str(id).split("_")[-1].split("'")[0]
            regions.append(data)
            post.append(data_1)
        except:
            continue
    return render_template('./recruit/Word_cloud_diagram.html', image=image, required_Technology=required_Technology,
                           city=city, regions=set(regions), post=set(post), region=region, pos=pos)
