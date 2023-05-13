#数据库操作
import pymysql
#连接数据库
conn=pymysql.connect(host='localhost',port=3306,user='root',password='123456',database='测试',charset='utf8')
#创建一个游标对象
cursor=conn.cursor()

# 创建一个指定数据库名
# cursor.execute('create database 创建')
# 使用execute()方法执行SQL语句

# 获取第一条数据
s = cursor.execute('insert user values(123,456,110)')
rest = cursor.fetchone()
print(rest)
# 这是查询表中所有的数据
# rest = cursor.fetchall()
# for i in rest:
#     print(i)

# sql = 'select 职位 from 爬虫 '
# cursor.execute(sql)
# # 这是查询表中所有的数据
# rest = cursor.fetchall()
# for i in rest:
#     print(i)
# # 关闭数据库连接
# conn.close()

append = 'insert into user(username,password,phone) values("111","222","333");'
# cursor.execute(conn)
# 添加
cursor.execute(append)
conn.commit()  # 表示将修改操作提交到数据库
# print('创建表成功')
print('添加成功')


'''语法一：insert 表 values(值1，值2，值n);

           insert user values(666,'张三‘,'女')；  向user 表中插入值id为666，姓名为张三，性别女

语法二：insert into 表(字段1，字段2，字段n) values(值1，值2，值n);

  insert into user(id,username,age) values(666,'学'，25)；

 向user 表中插入id 为666，username 为学，age 为25'''


