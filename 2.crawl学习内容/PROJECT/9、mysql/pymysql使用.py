'''
1.创建数据库
2.使用数据库
use 数据库名

3.创建数据表
4.ontariogenomics.打开数据库连接


创建数据库
CREATE DATABASE 数据库名;

使用数据表
CREATE TABLE url_data(
    url_id INT ,
    url_title VARCHAR(100) NOT NULL,
    url_author VARCHAR(40) NOT NULL,
    url_data DATE
    );
'''

#导入pymysql
import pymysql

#打开数据库连接
db=pymysql.connect(host='localhost',
                   user='root',
                   password='123456',
                   database='my_mysql')
#使用cursor()方法创建一个游标对象 cursor
cursor=db.cursor()

#使用 execute()方法执行SQL查询
cursor.execute('SELECT VERSION()')

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()
