'''
MongoDB
是一个高性能，开源，无模式的文档数据库，是当前NOSQL数据库产品中最热门的一种。
它在许多场景下用于替代传统的关系型数据库或键值对存储方式。
 MongoDB是用c++开发的。它是基于分布式文件存储的开源数据库系统。
 MongoDB将数据存储为一个文档，数据结构由键值（key_value)对组成。MongoDB
文档类似JSON对象。
  ~字段值可以包含其他文档、数组及文档数组。


  NoSQL的优缺点
  优点：高可拓展性、分布式计算、低成本、架构的灵活性，半结构化数据、没有复杂的关系
  缺点：没有标准化、有限的查询功能、最终一致不是直观的程序

  MongoDB是一个文档数据库（以JSON为数据模型），
'''

import pymongo
cli=pymongo.MongoClient('localhost',27017)

#获取要操作的数据库   use 数据库名
db=cli.datadb
#db=cli["datadb"]   第二中获取要操作的数据库的方法

#获取要操作的集合   db.createCollection('集合名）
Collection=db.data

#操作数据库
#增加数据
#一次性添加一条
# data={'name':'李四','age':19}
# Collection.insert_one(data)
#
# #多条
# data1={'name':'瑶','age':20}
# data2={'name':'双艳','age':20}
# Collection.insert_many([data1,data2])

#查找
# print(list(Collection.find()))
# print(Collection.find_one())

#修改
# Collection.update_one({'name':'李四'},{'$set':{'name':'篮球','age':4.ontariogenomics}})

#删除
# Collection.delete_many({'name':'李四'})

a=list(Collection.find())
for i in a:
    print(i)