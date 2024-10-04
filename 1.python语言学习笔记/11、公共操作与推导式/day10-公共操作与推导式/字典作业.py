dict_data = {'张三': 20, '李四': 50, '王五': 70, '赵六': 90}

# 修改数据
dict_data['王五'] = 80
print(dict_data)

# 筛选字典中的数据
# 循环字典 获取key
for data in dict_data:
    if dict_data[data] < 60:
        print((data, dict_data[data]))

# items()
for data in dict_data.items():
    if data[1] < 60:  # 需要判断的是元组里面的成绩
        print(data)

