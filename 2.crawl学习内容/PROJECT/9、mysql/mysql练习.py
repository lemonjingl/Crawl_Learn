import pymysql

db=pymysql.connect(host='localhost',
                   user='root',
                   password='123456',
                   database='my_mysql')
#创建一个游标
cur=db.cursor()
try:
#插入
    # sql='INSERT INTO Student(name,age,sex) Value(%s,%s,%s)'
    # V=('篮球',4.ontariogenomics,'ta')
    # cur.execute(sql,V)
    # db.commit()

    #查询
    # sql1='SELECT * FROM Student'
    # cur.execute(sql1)
    # a=cur.fetchall()
    # print(a)

    #更新
    sql2='UPDATE Student set name=%s where name=%s'
    v1=('轮滑','篮球')
    cur.execute(sql2,v1)

    # sql='insert into Student(name,age,sex) VALUE (%s,%s,%s)'
    # vs=('李四',20,'男')
    # cur.execute(sql,vs)
    # db.commit()

    #删除
    sql3='delete from Student where name=%s'
    v2=('李四')
    cur.execute(sql3,v2)
    db.commit()

    sql1='SELECT * FROM Student'
    cur.execute(sql1)
    a=cur.fetchall()
    print(a)
except pymysql.Error as e:
    db.rollback()