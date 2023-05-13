import json

from sql_help1 import db
import pyecharts.options as opts
from pyecharts.charts import Pie


# 饼图
def save_html(data):
    info = json.loads(data)
    x_data = []
    y_data = []
    for key in info.keys():
        x_data.append(key)
        y_data.append(info[key])
    data_pair = [list(z) for z in zip(x_data, y_data)]
    data_pair.sort(key=lambda x: x[1])

    (
        Pie(init_opts=opts.InitOpts(bg_color="#2c343c"))
        .add(
            series_name="安居客",
            data_pair=data_pair,
            rosetype="radius",
            radius="55%",
            center=["50%", "50%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="梅州租房直观图",
                pos_left="center",
                pos_top="20",
                title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
        .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            ),
            label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
        )
        .render("mz.html")
    )





from pyecharts import options as opts
from pyecharts.charts import Bar
def loo(list,list_1):
    c = (
        Bar()
        .add_xaxis(
            [
                ">1000",
                "1000-1500",
                "1500-2000",
                "2000-2500",
                "2500-3000",
                '3000-3500',
                '3500-4000',
                '4000-4500',
                '4500-5000',
                '5000-7000',
                '<7000',
            ]
        )
        .add_yaxis("广州房各价位数量", list)
        # .add_yaxis("杭州房各价位数量", list_1)
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
            title_opts=opts.TitleOpts(title="Bar-旋转X轴标签", subtitle="解决标签名字过长的问题"),
        )
        .render("demo.html")
    )


def pader():
    info = {}
    info_2 = {}
    list = []
    list_1 = []
    info[">1000"] = info["1000-1500"]= info["1500-2000"]=info["2000-2500"]=info["2500-3000"]=info['3000-3500']=info['3500-4000']=info["4000-4500"]=info["4500-5000"]=info["5000-7000"]=info[">7000"]=0
    info_1 = db.fetchall('select 租金 from 安居客_gz_租房')
    for aa in info_1:
        money = aa[0].split("_")[0]
        if int(money)<1000:
            info[">1000"] = int(info[">1000"]+1)
        elif 1000<int(money)<=1500:
            info["1000-1500"] = int(info["1000-1500"]+1)
        elif 1500<int(money)<=2000:
            info["1500-2000"] =int(info["1500-2000"]+1)
        elif 2000<int(money)<=2500:
            info["2000-2500"] =int(info["2000-2500"]+1)
        elif 2500<int(money)<=3000:
            info["2500-3000"] =int(info["2500-3000"]+1)
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
            info[">7000"] = int(info[">7000"]+1)

    info_2[">1000"] = info_2["1000-1500"]= info_2["1500-2000"]=info_2["2000-2500"]=info_2["2500-3000"]=info_2['3000-3500']=info_2['3500-4000']=info_2["4000-4500"]=info_2["4500-5000"]=info_2["5000-7000"]=info_2[">7000"]=0
    info_3 = db.fetchall('select 租金 from 安居客_hz_租房')
    for aa in info_3:
        money = aa[0].split("_")[0]
        if int(money)<1000:
            info_2[">1000"] = int(info_2[">1000"]+1)
        elif 1000<int(money)<=1500:
            info_2["1000-1500"] = int(info_2["1000-1500"]+1)
        elif 1500<int(money)<=2000:
            info_2["1500-2000"] =int(info_2["1500-2000"]+1)
        elif 2000<int(money)<=2500:
            info_2["2000-2500"] =int(info_2["2000-2500"]+1)
        elif 2500<int(money)<=3000:
            info_2["2500-3000"] =int(info_2["2500-3000"]+1)
        elif 3000 < int(money) <= 3500:
            info_2["3000-3500"] = int(info_2["3000-3500"] + 1)
        elif 3500 < int(money) <= 4000:
            info_2["3500-4000"] = int(info_2["3500-4000"] + 1)
        elif 4000 < int(money) <= 4500:
            info_2["4000-4500"] = int(info_2["3000-3500"] + 1)
        elif 4500 < int(money) <= 5000:
            info_2["4500-5000"] = int(info_2["3500-4000"] + 1)
        elif 5000 < int(money) <= 7000:
            info_2["5000-7000"] = int(info_2["5000-7000"] + 1)
        else:
            info_2[">7000"] = int(info_2[">7000"]+1)
    for data in info.values():
        list.append(data)
    for orse in info_2.values():
        list_1.append(orse)
    loo(list,list_1)
    save_html(json.dumps(info))
# pader()

def mz():
    info = {}
    info[">1000"] = info["1000-1500"]= info["1500-2000"]=info["2000-2500"]=info["2500-3000"]=info['3000-3500']=info['3500-4000']=info["4000-4500"]=info["4500-5000"]=info["5000-7000"]=info[">7000"]=0
    info_1 = db.fetchall('select 租金 from 安居客_mz_租房')
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
    save_html(json.dumps(info))
mz()