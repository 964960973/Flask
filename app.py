import json
from sql_help1 import db
from flask import Flask,render_template

app = Flask(__name__)

def mz():
    info = {}
    dataList = []
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

    for item in info.items():
        dataList.append({"value": item[1], "name": item[0]})
    return dataList
mz()

@app.route('/')
def login():
    dataList = mz()
    return render_template('demo1.html',dataList=dataList)

if __name__ == '__main__':
    app.run()