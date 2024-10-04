import pymongo

cli=pymongo.MongoClient('localhost',27017)

#要操作的数据库
db=cli.my_mongo

#要操作的集合
C=db.data1

#插入
data1={'author':'李明','title':'你好'}
data2={'author':'啊珍','title':'ok'}
C.insert_many([data1,data2])

#更新
C.update_one({'author':'李明'},{'$set':{'author':'李四','title':'ni'}})

#删除
C.delete_one({'author':'李四'})
print(list(C.find()))
print(C.find_one())