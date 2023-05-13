import pymysql
from flask import Flask

import sql_help

from sql_help1 import db

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
    # 'select * from 用户表 where username = "%s" and password = "%s"' % ('张三', '18038573677')
    result = sql_help.fetchall('select * from 用户表 where name = %s',"张三")
    print(result)
    return 'login'

@app.route('/index')
def index():
    result = sql_help.fetchone('select * from 用户表')
    print(result)
    return 'index'

@app.route('/deltea')
def deltea():
    result = db.fetchall('select * from 爬虫')
    print(result)
    return '类的方式获取'

deltea()
@app.route('/sop')
def sop():
    result = db.fetchall('select * from 用户表 where name = %s',"张三")
    print(result)
    return '类的方式获取'
'''
    conn,cursor = db.open()
    cursor.execute('***')
    result = cursor.fetchmany(4)
    db.colse(conn,cursor)
'''

with db as cur:
    cur.excute('select sleep(1)')
    result = cur.fetchmany(4)

# if __name__ == '__main__':
#     app.run()