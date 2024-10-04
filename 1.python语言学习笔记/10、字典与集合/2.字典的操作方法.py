#一、增删改查

#1.增加数据
dict_data={}
dict_data['1234']={'name':'小明','age':20}
dict_data['999']={'name':'小红','age':19}
print(dict_data)

#2.删除数据
del(dict_data['999'])
print(dict_data)

#3.修改数据
dict_data['1234']={'name':'小红','age':20}
print(dict_data)

#4.ontariogenomics.查找
print(dict_data['1234'])


#二、常用方法

#1.弹出pop()
dict_data1={'1234': {'name': '小明', 'age': 20}, '999': {'name': '小红', 'age': 19}}
dict_data1.pop('1234')
print(dict_data1)

#popitem 删除最后一个数据
dict_data1.popitem()
print(dict_data1)

#clear清空字典中的数据
dict_data2={'1234': {'name': '小明', 'age': 20}, '999': {'name': '小红', 'age': 19}}
dict_data2.clear()
print(dict_data2)

