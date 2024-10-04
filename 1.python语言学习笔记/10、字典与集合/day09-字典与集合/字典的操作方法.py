# dict_data = {}

# 弹出 pop
# dict_data = {'1234': {'name': '小明', 'age': 20},
#              '2234': {'name': '小刚', 'age': 21}}
# print(dict_data.pop('1234'))
# print(dict_data)

# popitem 删除最后一个数据
# dict_data = {'1234': {'name': '小明', 'age': 20},
#              '2234': {'name': '小刚', 'age': 21},}
# print(dict_data.popitem())
# print(dict_data)

# clear 清空字典中的数据
# dict_data = {'1234': {'name': '小明', 'age': 20},
#              '2234': {'name': '小刚', 'age': 21}}
# dict_data.clear()
# print(dict_data)

# 如果字典中已经存在key就不进行操作 ，不存在就添加数据
# dict_data = {'1234': {'name': '小明', 'age': 20},
#              '2234': {'name': '小刚', 'age': 21}}
# dict_data.setdefault('4433', {"data": "1234"})
# print(dict_data)

# copy 复制字典中的数据
# dict_data = {'1234': {'name': '小明', 'age': 20},
#              '2234': {'name': '小刚', 'age': 21}}
# dict_data.copy()

# get 获取字典中的数据 ，如果没有返回默认值None
# dict_data = {'1234': {'name': '小明', 'age': 20},
#              '2234': {'name': '小刚', 'age': 21}}
# print(dict_data.get('1234'))
# print(dict_data.get('2222')) # 返回默认值None
# 想要它没有找到的情况下返回一个 False
# print(dict_data.get('2222', False))

# values 获取字典中的所有value 存放到容器里面
# dict_data = {'1234': {'name': '小明', 'age': 20},
#              '2234': {'name': '小刚', 'age': 21}}
# print(dict_data.values())
# print(list(dict_data.values()))
# 循环
# for i in dict_data.values():
#     print(i)

# key 获取字典中的所有key
# dict_data = {'1234': {'name': '小明', 'age': 20},
#              '2234': {'name': '小刚', 'age': 21}}
# print(dict_data.keys())
# print(list(dict_data.keys()))

# items 获取字典中的所有key和values
# dict_data = {'1234': {'name': '小明', 'age': 20},
#              '2234': {'name': '小刚', 'age': 21}}
# print(dict_data.items())
# print(list(dict_data.items()))

# update 更新数据
# 如果key不存在字典就会增加数据
# 如果字典key存在字典，就会更新数据
# dict_data = {'1234': {'name': '小明', 'age': 20},
#              '2234': {'name': '小刚', 'age': 21}}
#
# dict_data.update({'2222': {1: 1}})
# print(dict_data)





