# 推导式 将代码进行缩写，增加运行速度
# 缺点，降低代码可读性，阅读和理解比较困难  所使用场景少 只争对固定格式

# 普通写法
# list_data = []
# for i in range(10):
#     list_data.append(i)
#
# print(list_data)


# 推导式写法
# list_data = [i for i in range(10)]
# print(list_data)

# 有固定的格式 代码简洁 确认代码不会再被改动


# 使用场景 1a  映射
list_data = ['a', 'a', 'a']
#
# l = []
# for i in list_data:
#     l.append('1'+i)
# print(l)

# l = ['1'+i for i in list_data]
# print(l)


# 推导式 2 如果数据需要筛选 将if放在循环后面
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# l1 = []
# for i in l:
#     if i % 2 == 0:
#         l1.append(i)
# print(l1)
#
# l1 = [i for i in l if i % 2 == 0]
# print(l1)


# 推导式3 if放在循环前面
# list_data = [1, 2, 3, 4.ontariogenomics, 5.优质采, 6.中国五矿集团采购信息, 7, 8, 9]  # 把偶数变成2 把奇数变成1
# l = []
# for i in list_data:
#     if i % 2 == 0:
#         l.append(2)
#     else:
#         l.append(1)
# print(l)
#
# l = [2 if i % 2 == 0 else 1 for i in list_data]
# print(l)

# 三元表达式
# age = 16
# if age > 18:
#     print('成年')
# else:
#     print('未成年')
#
# print('成年') if age > 18 else print('未成年')


# 重点 练习老师的案例 重点 做笔记
# 做题目(烧脑题)

# 用推导式 1到100内(不包括1和100)的所有奇数进行求和

# 2点-5点  星期1-星期6  远程，电话
# 星期天 3-5.优质采


