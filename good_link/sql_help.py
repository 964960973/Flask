import pymysql

from DBUtils.PooledDB import PooledDB


class SqlHelp(object):
    def __init__(self):
        self.pool = PooledDB(
        creator=pymysql,
        maxconnections=6,  # 可以链接的最大次数
        mincached=1,  # 初始化链接数
        blocking=True,  # 练级池中如果没有连接，是否阻塞等待,True等待，Flase报错可捕获.
        ping=0,  # 检测mysql是否可用

        host='127.0.0.1',  # 默认端口号
        port=3306,  # 默认端口号
        user='root',
        password='123456',  # 密码
        database='测试',  # 数据库名
        charset='utf8'  # 格式
        )

    def open_sql(self):
        conn = self.pool.connection()#去连接池拿一个
        cursor = conn.cursor()  # 创建游标
        return conn,cursor

    def colse(self,cursor,conn):
        cursor.close()
        conn.close()

    # def use_msq(self,sql, *args):
    #     '''获取单条数据'''
    #     # 去连接池中获取一个链接
    #     conn, cursor = self.open_sql()  # 执行操作
    #     cursor.execute(sql, *args)
    #     # self.colse(conn, cursor)
    #     return conn,cursor


    def fetchall(self, sql,*args):
        '''获取所有数据'''
        # 去连接池中获取一个链接
        conn,cursor = self.open_sql()  # 拿到一个链接并创建油标
        cursor.execute(sql,args)
        result = cursor.fetchall()
        self.colse(conn,cursor)
        return result
    #
    def fetchone(self,sql, *args):
        '''获取单条数据'''
        # 去连接池中获取一个链接
        conn, cursor = self.open_sql()  # 执行操作
        cursor.execute(sql, *args)
        result = cursor.fetchone()
        self.colse(conn, cursor)
        return result

    def insert_one(self,sql,*args):
        '''插入单挑数据'''
        conn,cursor = self.open_sql()  # 拿到一个链接并创建油标
        cursor.execute(sql,*args)
        result = conn.commit()
        self.colse(conn,cursor)
        return result




    def update(self,sql,*args):
        '''编辑更新sql'''
        conn,cursor = self.open_sql()  # 拿到一个链接并创建油标
        cursor.execute(sql,*args)
        conn.commit()
        self.colse(conn,cursor)
        return '更新成功'

    def delete(self,sql,*args):
        '''删除更新sql'''
        conn,cursor = self.open_sql()  # 拿到一个链接并创建油标
        cursor.execute(sql,*args)
        conn.commit()
        self.colse(conn,cursor)
        return '删除成功'


    def tables(self,sql,*args):
        '''删除更新sql'''
        conn,cursor = self.open_sql()  # 拿到一个链接并创建油标
        cursor.execute(sql,*args)
        result = cursor.fetchall()
        self.colse(conn,cursor)
        return result




    def __enter__(self):
        return self.open_sql()[1]

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type,exc_val,exc_tb)

db = SqlHelp()
