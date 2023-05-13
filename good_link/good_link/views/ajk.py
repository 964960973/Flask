import functools
import jieba
import json
from PIL import Image
import numpy as np
from ..sql_help import db
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from flask import Blueprint, session, redirect, url_for, render_template, request

from pyecharts import options as opts
from pyecharts.charts import Bar

Ajk = Blueprint('ajk',__name__)



def Histogram(sql):
    info = {}
    list = []
    info["0-800"] = info["800-1500"] = info["1500-2000"] = info["2000-2500"] = info["2500-3000"] = info['3000-3500'] = info['3500-4000'] = info["4000-4500"] = info["4500-5000"] = info["5000-7000"] = info[">7000"] = 0
    info_1 = db.fetchall(f'select 租金 from 安居客_{sql}_租房')
    for aa in info_1:
        try:
            money = int(aa[0].split("_")[0])
        except:
            continue
        if type(money) != int:
            continue
        if int(money) <= 800:
            info["0-800"] = int(info["0-800"] + 1)
        elif 800 < int(money) <= 1500:
            info["800-1500"] = int(info["800-1500"] + 1)
        elif 1500 < int(money) <= 2000:
            info["1500-2000"] = int(info["1500-2000"] + 1)
        elif 2000 < int(money) <= 2500:
            info["2000-2500"] = int(info["2000-2500"] + 1)
        elif 2500 < int(money) <= 3000:
            info["2500-3000"] = int(info["2500-3000"] + 1)
        elif 3000 < int(money) <= 3500:
            info["3000-3500"] = int(info["3000-3500"] + 1)
        elif 3500 < int(money) <= 4000:
            info["3500-4000"] = int(info["3500-4000"] + 1)
        elif 4000 < int(money) <= 4500:
            info["4000-4500"] = int(info["3000-3500"] + 1)
        elif 4500 < int(money) <= 5000:
            info["4500-5000"] = int(info["3500-4000"] + 1)
        elif 5000 < int(money) <= 7000:
            info["5000-7000"] = int(info["5000-7000"] + 1)
        else:
            info[">7000"] = int(info[">7000"] + 1)
    return json.dumps(info),str(sql)


def Histogram_1(sql):
    info = {}
    list = []
    info["1室0厅"] = info["2室0厅"] = info["3室0厅"] = info["4室0厅"] = info["5室0厅"] = \
        info["1室1厅"] = info["2室1厅"] = info["3室1厅"] = info["4室1厅"] = info["5室1厅"] = \
        info["3室2厅"] = info["4室2厅"] = info["5室2厅"] = \
        info["4室3厅"] = info["5室3厅"] = 0
    info_1 = db.fetchall(f'select 房屋大小 from 安居客_{sql}_租房')
    for aa in info_1:
        cary = aa[0].split('厅')[0] + '厅'
        if cary == '1室0厅':
            info["1室0厅"] = int(info["1室0厅"] + 1)
        elif cary == '2室0厅':
            info["2室0厅"] = int(info["2室0厅"] + 1)
        elif cary == '3室0厅':
            info["3室0厅"] = int(info["3室0厅"] + 1)
        elif cary == '4室0厅':
            info["4室0厅"] = int(info["4室0厅"] + 1)
        elif cary == '5室0厅':
            info["5室0厅"] = int(info["5室0厅"] + 1)
        elif cary == '1室1厅':
            info["1室1厅"] = int(info["1室1厅"] + 1)
        elif cary == '2室1厅':
            info["2室1厅"] = int(info["2室1厅"] + 1)
        elif cary == '3室1厅':
            info["3室1厅"] = int(info["3室1厅"] + 1)
        elif cary == '4室1厅':
            info["4室1厅"] = int(info["4室1厅"] + 1)
        elif cary == '5室1厅':
            info["5室1厅"] = int(info["5室1厅"] + 1)
        elif cary == '3室2厅':
            info["3室2厅"] = int(info["3室2厅"] + 1)
        elif cary == '4室2厅':
            info["4室2厅"] = int(info["4室2厅"] + 1)
        elif cary == '5室2厅':
            info["5室2厅"] = int(info["5室2厅"] + 1)
        elif cary == '4室3厅':
            info["4室3厅"] = int(info["4室3厅"] + 1)
        elif cary == '5室3厅':
            info["5室3厅"] = int(info["5室3厅"] + 1)
    return json.dumps(info),str(sql)


def bar_base(data_li,sql) -> Bar:
    info = json.loads(data_li)
    y_key = []
    x_keys = []
    for key,value in info.items():
        y_key.append(key)
        x_keys.append(value)
    c = (
        Bar()
        .add_xaxis(y_key)
        .add_yaxis(sql, x_keys)
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle=f'当前城市为{sql}'))
    )
    return c


def pie_chart_function(key):
    info = {}
    dataList = []
    info[">1000"] = info["1000-1500"] = info["1500-2000"] = info["2000-2500"] = info["2500-3000"] = info['3000-3500'] = \
    info['3500-4000'] = info["4000-4500"] = info["4500-5000"] = info["5000-7000"] = info[">7000"] = 0
    info_1 = db.fetchall(f'select 租金 from 安居客_{key}_租房')
    for aa in info_1:
        money = int(float(aa[0].split("_")[0]))
        if int(money) < 1000:
            info[">1000"] = int(info[">1000"] + 1)
        elif 1000 < int(money) <= 1500:
            info["1000-1500"] = int(info["1000-1500"] + 1)
        elif 1500 < int(money) <= 2000:
            info["1500-2000"] = int(info["1500-2000"] + 1)
        elif 2000 < int(money) <= 2500:
            info["2000-2500"] = int(info["2000-2500"] + 1)
        elif 2500 < int(money) <= 3000:
            info["2500-3000"] = int(info["2500-3000"] + 1)
        elif 3000 < int(money) <= 3500:
            info["3000-3500"] = int(info["3000-3500"] + 1)
        elif 3500 < int(money) <= 4000:
            info["3500-4000"] = int(info["3500-4000"] + 1)
        elif 4000 < int(money) <= 4500:
            info["4000-4500"] = int(info["3000-3500"] + 1)
        elif 4500 < int(money) <= 5000:
            info["4500-5000"] = int(info["3500-4000"] + 1)
        elif 5000 < int(money) <= 7000:
            info["5000-7000"] = int(info["5000-7000"] + 1)
        else:
            info[">7000"] = int(info[">7000"] + 1)

    for item in info.items():
        dataList.append({"value": item[1], "name": item[0]})
    return dataList

def pie_chart_function_opp(key):
    info = {}
    dataList = []
    info["1室0厅"] = info["2室0厅"] = info["3室0厅"] = info["4室0厅"] = info["5室0厅"] = \
        info["1室1厅"] = info["2室1厅"] = info["3室1厅"] = info["4室1厅"] = info["5室1厅"] = \
        info["3室2厅"] = info["4室2厅"] = info["5室2厅"] = \
        info["4室3厅"] = info["5室3厅"] = 0
    info_1 = db.fetchall(f'select 房屋大小 from 安居客_{key}_租房')
    for aa in info_1:
        cary = aa[0].split('厅')[0] + '厅'
        if cary == '1室0厅':
            info["1室0厅"] = int(info["1室0厅"] + 1)
        elif cary == '2室0厅':
            info["2室0厅"] = int(info["2室0厅"] + 1)
        elif cary == '3室0厅':
            info["3室0厅"] = int(info["3室0厅"] + 1)
        elif cary == '4室0厅':
            info["4室0厅"] = int(info["4室0厅"] + 1)
        elif cary == '5室0厅':
            info["5室0厅"] = int(info["5室0厅"] + 1)
        elif cary == '1室1厅':
            info["1室1厅"] = int(info["1室1厅"] + 1)
        elif cary == '2室1厅':
            info["2室1厅"] = int(info["2室1厅"] + 1)
        elif cary == '3室1厅':
            info["3室1厅"] = int(info["3室1厅"] + 1)
        elif cary == '4室1厅':
            info["4室1厅"] = int(info["4室1厅"] + 1)
        elif cary == '5室1厅':
            info["5室1厅"] = int(info["5室1厅"] + 1)
        elif cary == '3室2厅':
            info["3室2厅"] = int(info["3室2厅"] + 1)
        elif cary == '4室2厅':
            info["4室2厅"] = int(info["4室2厅"] + 1)
        elif cary == '5室2厅':
            info["5室2厅"] = int(info["5室2厅"] + 1)
        elif cary == '4室3厅':
            info["4室3厅"] = int(info["4室3厅"] + 1)
        elif cary == '5室3厅':
            info["5室3厅"] = int(info["5室3厅"] + 1)
    for item in info.items():
        dataList.append({"value": item[1], "name": item[0]})
    return dataList


def Word_cloud_image(key):
    info_1 = db.fetchall(f'select 房屋描述 from 安居客_{key}_租房')
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
    image = f'/static/image/安居客_{key}_租房房屋描述.png'
    plt.savefig(f'./good_link/static/image/安居客_{key}_租房房屋描述', dpi=500)
    return image

def auth(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        user_name = session.get('aaaaa')
        if not user_name:
            return redirect(url_for('wy.lo'))
        return func(*args,**kwargs)
    return inner

@Ajk.route('/ajk',methods=["GET","POST"])
@auth
def ajk():
    jobs = db.fetchall('select * from 安居客_hz_租房')
    nid = db.tables('SHOW TABLES')
    regions = []
    for id in nid:
        try:
            data = str(id).split('_')[1].split('_')[0]
            regions.append(data)
        except:
            continue
    return render_template('./ajk/demo.html',jobs=jobs,regions=regions)

@Ajk.route('/ajk_index',methods=["GET","POST"])
@auth
def zufang():
    key = request.args.get('key')
    if key == '':
        key = 'hz'
    jobs = db.fetchall(f'select * from 安居客_{key}_租房')
    nid = db.tables('SHOW TABLES')
    regions = []
    for id in nid:
        try:
            data = str(id).split('_')[1].split('_')[0]
            regions.append(data)
        except:
            continue
    return render_template('./ajk/demo.html', jobs=jobs, regions=regions,key=key)


@Ajk.route('/histogram',methods=["GET","POST"])
@auth
def histogram():
    key = request.args.get('key')
    if key == '':
        key = "hz"
    nid = db.tables('SHOW TABLES')
    regions = []
    for id in nid:
        try:
            data = str(id).split('_')[1].split('_')[0]
            regions.append(data)
        except:
            continue
    return render_template("./ajk/histogram.html",key=key,regions=regions)

@Ajk.route("/barChart")
@auth
def get_bar_chart():
    key = request.args.get('key')
    if key == None:
        key = "hz"
    data_li,sql = Histogram(key)
    c = bar_base(data_li,sql)
    return c.dump_options_with_quotes()


@Ajk.route('/comparison_chart',methods=["GET","POST"])
@auth
def comparison_chart():
    key = request.args.get('key')
    if key == '':
        key = "hz"
    nid = db.tables('SHOW TABLES')
    regions = []
    for id in nid:
        try:
            data = str(id).split('_')[1].split('_')[0]
            regions.append(data)
        except:
            continue
    return render_template("./ajk/comparison_chart.html",key=key,regions=regions)


@Ajk.route("/comparison")
@auth
def comparison():
    key = request.args.get('key')
    if key == None:
        key = "hz"
    data_li,sql = Histogram_1(key)
    c = bar_base(data_li,sql)
    return c.dump_options_with_quotes()



@Ajk.route('/Pie',methods=["GET","POST"])
@auth
def Pie():
    key = request.args.get('key')
    if key == '':
        key = "hz"
    nid = db.tables('SHOW TABLES')
    regions = []
    for id in nid:
        try:
            data = str(id).split('_')[1].split('_')[0]
            regions.append(data)
        except:
            continue
    dataList = pie_chart_function(key)
    return render_template("./ajk/Pie_chart.html",key=key,regions=regions,dataList=dataList)

@Ajk.route('/Piehouse',methods=["GET","POST"])
@auth
def Pieopp():
    key = request.args.get('key')
    if key == '':
        key = "hz"
    nid = db.tables('SHOW TABLES')
    regions = []
    for id in nid:
        try:
            data = str(id).split('_')[1].split('_')[0]
            regions.append(data)
        except:
            continue
    dataList = pie_chart_function_opp(key)
    return render_template("./ajk/Pie_chart_house.html",key=key,regions=regions,dataList=dataList)


@Ajk.route('/Word_cloud_image',methods=["GET","POST"])
@auth
def Word_cloud_image_1():
    key = request.args.get('key')
    if key == '':
        key = "hz"
    nid = db.tables('SHOW TABLES')
    regions = []
    for id in nid:
        try:
            data = str(id).split('_')[1].split('_')[0]
            regions.append(data)
        except:
            continue
    image = Word_cloud_image(key)
    return render_template("./ajk/ajk_cyt.html", key=key, regions=regions, image=image)