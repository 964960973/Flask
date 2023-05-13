import pymysql
from threading import Thread
from DBUtils.PooledDB import PooledDB

POOL = PooledDB(
    creator=pymysql,
    maxconnections=6,#可以链接的最大次数
    mincached=1,#初始化链接数
    blocking=True,#练级池中如果没有连接，是否阻塞等待,True等待，Flase报错可捕获.
    ping=0,#检测mysql是否可用

    host='127.0.0.1',#默认端口号
    port=3306,#默认端口号
    user='root',
    password='123456',#密码
    database='测试',#数据库名
    charset='utf8'#格式
)


def fetchall(sql,*args):
    '''获取所有数据'''
    # 去连接池中获取一个链接
    conn = POOL.connection()
    cursor = conn.cursor()  # 创建游标
    cursor.execute(sql,*args)  # 执行sql语句
    cursor.execute('select * from 爬虫')  # 执行sql语句
    result = cursor.fetchall()  # 执行操作
    cursor.close()  # 关闭油标
    conn.close()  # 返回连接给连接池
    return result

def fetchone(sql,*args):
    '''获取单条数据'''
    # 去连接池中获取一个链接
    conn = POOL.connection()
    cursor = conn.cursor()  # 创建游标
    cursor.execute(sql,*args)  # 执行sql语句
    # cursor.execute('select * from 爬虫')  # 执行sql语句
    result = cursor.fetchone()  # 执行操作
    cursor.close()  # 关闭油标
    conn.close()  # 返回连接给连接池
    return result