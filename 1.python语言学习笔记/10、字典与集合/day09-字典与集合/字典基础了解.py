# 中文字典 成语字典 英汉字典

# a-z   key
# 中文 我 w  ?????  ？？

# list_data = [['小明', 20, '男', 60], ['小芳', 18, '女', 40]]
# 1000

# 如何在列表中快速提取数据
# for i in list_data:
#     if i[0] == '小明':
#         print(i)
# 循环+if

# 字典查找数据的速度比列表高很多
# 字典存储的信息会更加明白直接，可以存储更加复杂的数据


"""
dict_data = {   key  :  value  , key1  :  value1 }

1，符号以大括号表示
2，数据是以键值对出现的 键值中间用冒号连接
3，key的数据必须是不可变类型，key是不重复的
"""
# key不能和其他的key重复,必须要是唯一的
dict_data = {123: {'name': '小明', 'age': 20}}
# dict_data ={} 创建一个空字典

# 80% 会忘记字典的知识点  字典知识点非常重要的
# 字典属于可变数据类型
# 特性：字典没有索引  通过key来取值
print(dict_data[123]['name'])


# list dict set        可变
# int float str tuple  不可变
# 自定义







