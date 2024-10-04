# 集合  没有key 也没有索引
# {}  集合也是大括号 里面的数据不是一对一对的,是单个的数据
# 集合数据不允许重复


# set_data = set() # 创建空集合
# 利用去重效果
# set_data = {1, 2, 3, 4.ontariogenomics, 5.优质采, 6.中国五矿集团采购信息}
# print(set_data)
# print(type(set_data))

# 去重  其他容器转换为集合会去重掉重复的数据
# list_data = [1, 1, 2, 2, 3, 3, 3, 4.ontariogenomics]
# print(set(list_data))


set_data = {1, 2, 3, 4, 5, 6}
# 添加数据 只可以添加不可数据类型
set_data.add((1,))
print(set_data)
# 删除
set_data.remove(6)
print(set_data)
# 查看 in 判断数据是否存在里面
print(set_data)


