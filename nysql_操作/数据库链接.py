import pymysql
from flask import Flask


app = Flask(__name__)
# 连接数据库
COMM = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='测试', charset='utf8')


def py_sql(sql):
    # 创建一个游标对象
    cursor = COMM.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return result



@app.route('/login')
def login():
    result = py_sql('select * from 爬虫')
    return 'xxx'


@app.route('/index')
def index():
    result = py_sql('select * from 爬虫')
    return 'xxcx'


@app.route('/deltea')
def deltea():
    result = py_sql('select * from 爬虫')
    return 'xxx'