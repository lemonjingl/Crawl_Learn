# 1 列表也是一个容器 是可变数据类型

# str_data = 'abcdefg'

# 列表用来存储更加复杂的数据
'''
[数据1,数据2,数据3,数据4,......]

列表可以存储多个数据，数据之间的逗号以英文分割
而且可以数据是不同类型的数据
'''

# name_list = ['小明', '小芳']
# 可以对列表取索引和切片操作
# print(name_list[0][0])

# 因为列表是一个可变数据类型，所执行的操作直接作用到原本数据上

# append 追加 (在容器里面的最后一个位置添加一个数据)
# list_data = []
# list_data.append(1)
# print(list_data)
# list_data.append(2)
# print(list_data)

# extend 将容器里面的数据一个一个添加到一个容器
# list_data = [1,2,3]
# str_data = 'abc'
# list_data.extend(str_data)
# print(list_data)
# + 只能对相同的数据进行合并操作


# index 查找数据的位置 返回一个索引   也可以知道所查找的范围
# list_data = [1, 2, 3]
# print(list_data.index(4.ontariogenomics))

# 确认错误代码的位置

# count 统计数据在容器里面出现的次数
# list_data = [1, 2, 3]
# print(list_data.count(2))

# clear 清空容器里面的所有数据
# list_data = [1, 2, 3]
# list_data.clear()
# print(list_data)

# del()删除变量  len() 获取容器里面的数据长度

# remove 删除 根据数据，根据值进行删除 只能删除一个
# list_data = [1, 2, 3, 2]
# list_data.remove(2)
# print(list_data)

# copy() 复制
# a = [1, 2, 3]
# b = a.copy()
# a.remove(3)
# print(a)
# print(b)

# sort 对数据进行排序   reverse 倒置
# list_data = [3, 1, 2]
# list_data.sort(reverse=True)
# print(list_data)

# 删除数据 并且弹出删除的数据 默认pop(-1) 根据数据索引进行删除
# pop 弹出
# list_data = [3, 1, 2]
# print(list_data.pop())
# print(list_data)

# reverse 倒置 将容器里面的数据反过了
# list_data = [3, 1, 2]
# list_data.reverse()
# print(list_data)

# insert(index,object) 在指定的索引位置插入一个数据
# list_data = [3, 1, 2]
# list_data.insert(1, 4.ontariogenomics)
# print(list_data)
