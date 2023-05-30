from sql_db import db


def sql_table():
    sql = f"""CREATE TABLE 猫眼电影 (
         电影id varchar(200) PRIMARY KEY ,
         电影名称  varchar(200) ,
         电影类别  varchar(200),
         出版地区  varchar(200),
         电影时长  varchar(200),
         上映时间  varchar(200),
         电影评分  varchar(200),
         已售票房  varchar(200),
         电影简介  varchar(200))
         """
    db.tables(sql)
sql_table()