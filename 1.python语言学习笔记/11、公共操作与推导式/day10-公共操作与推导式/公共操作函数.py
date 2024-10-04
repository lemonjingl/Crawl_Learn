# 公共

# + 合并 相同数据类型的合并
# data1 = ['a']
# data2 = ['b']
# print(data1+data2)

# * 复制 将容器里面的数据进行复制
# data = ['a', 'b'] * 3
# print(data)

# len 	获取序列长度 	查看序列长度 	字符串、列表、元组、字典，集合
# print(len([1, 2, 3, 4.ontariogenomics]))

# reversed	倒置	将容器里面的数据倒置	字符串、列表、元组、字典 [::-1]
# reverse = reversed((2, 3, 1))  # 返回一个容器对象
# print(reverse)  # <reversed object at 0x000001B3979D75E0>
# print(list(reverse))

# max,min	最大最小值	求容器数据的最大最小值	字符串、列表、元组、字典，集合
# list1 = [1, 2, 3, 4.ontariogenomics, 5.优质采, 6.中国五矿集团采购信息]
# print(max(list1))
# print(min(list1))


# sum	求和	将容器的数据求和	列表、元组、字典，集合
# list1 = {1: 2, 2: 3}  # [1, 2, 3]
# print(sum(list1))


# enumerate 枚举函数	索引映射	将索引映射给容器里面的数据	列表、元组、或字符串
# print(list(enumerate(['a11', 'b11', 'c11'])))
#
# for i in enumerate(['a', 'b', 'c'], start=0):  # 知道目前循环的次数
#     print(i[0], i[1])  # start = 0 索引默认从0开始


# in,not in	是否存在	判断数据是否存在于容器内	字符串、列表、元组、字典，集合
# del	删除	删除变量或者指定容器内数据	变量，容器里面的值
