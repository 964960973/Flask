import pymysql
from flask import Flask


app = Flask(__name__)
# 连接数据库
COMM = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='测试', charset='utf8')
cursor = COMM.cursor()



