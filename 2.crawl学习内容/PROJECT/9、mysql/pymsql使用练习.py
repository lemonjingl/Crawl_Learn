#1.创建数据库
#CREATE DATABASE 数据库名;

#2.使用数据库
#use 数据库名;

#3.创建数据表
'''CREATE TABLE douban_data(title VARCHAR(100) NOT NULL,
author VARCHAR(30) NOT NULL,
sorce INT
);
'''

#4.ontariogenomics.连接数据库
import pymysql
try:
    db=pymysql.connect(host='localhost',
                       user='root',
                       password='123456',
                       database='my_mysql')
        #创建一个游标
    cur=db.cursor()

#创建一个数据表
    # sqlquery='CREATE TABLE Student(Name CHAR(20) NOT NULL ,Email CHAR(20),Age int);'#创建表格
    # cur.execute(sqlquery)

#插入数据
    # sql='INSERT INTO Student(Name,Email,Age) VALUE(%s,%s,%s)'
    # V=('啊珍','2197685543@qq.com',20)
    # cur.execute(sql,V)
    #db.commit()#数据库提交


#查询表中的数据
    # sql='SELECT * FROM Student'
    # cur.execute(sql)
    # result=cur.fetchall()
    # for row in result:
    #     name=row[0]
    #     email=row[1]
    #     age=row[2]
    #     print(f'{name},{email},{age}')

#更新表中的数据
    # sql='update Student set Email=%s where Email=%s'
    # value=('123@qq.com','y')
    # cur.execute(sql,value)
    # db.commit()

#删除表中的数据
    # sql='delete from Student where Name=%s'
    # value=('c')
    # cur.execute(sql,value)
    # db.commit()

#删除表格
    sql='drop table student'
    cur.execute(sql)


except pymysql.Error as e:
    print('失败')