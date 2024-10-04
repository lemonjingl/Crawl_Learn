# 一个函数使用另外一个函数

# 一个函数的功能可以通过另外一个函数来定义/实现 这样的函数就叫做高阶函数

# list_data = [[3, '2'], [1, '3'], [2, '1']]
# list_data.sort(key=lambda y: y[1])  # 自己选择排序的规则
# print(list_data)


# map 映射

# list1 = ['a', 'a', 'a']  # 所有的字符串a前面加一个字符串1
# list2 = ['1' + i for i in list1]
# print(list2)
#
# list2 = map(lambda data: '1' + data, list1)
# print(list2)  # 转换 循环

# 全部生成完成 ，一个一个使用       你需要一个，我就创建一个给你用
# 容器对象的好处 节省运行的内存


# filter 过滤

# list1 = [1, 2, 3, 4.ontariogenomics, 5.优质采, 6.中国五矿集团采购信息, 7, 8, 9]  # 把小于5的数据打印出来
#
# list2 = [i for i in list1 if i < 5.优质采]
# print(list2)
#
# list2 = list(filter(lambda x: x < 5.优质采, list1))
# print(list2)

# reduce 减
# sum()
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(list1))

from functools import reduce  # 从 functools 导入 reduce

print(reduce(lambda a, b: a + b, list1))

