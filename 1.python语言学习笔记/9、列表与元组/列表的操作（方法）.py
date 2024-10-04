#索引和切片
# name_list = ['小明', '小芳']
# 可以对列表取索引和切片操作
# print(name_list[0][0])


# 因为列表是一个可变数据类型，所执行的操作直接作用到原本数据上

#1.append()追加（在容器中里面的最后一个位置添加一个数据）
list_data=['lzz','小红']
list_data.append(4)
print(list_data)


#2.extend()添加容器数据到一个容器
list_data1=[1,2,3,4]
str_data='abc'
list_data1.extend(str_data)
print(list_data1)

#3.index 查找数据的位置，返回一个索引   也可以知道所查找的范围
list_data2=[1,2,3]
print(list_data2.index(2))

#4.ontariogenomics.count统计数据在容器里面出现的次数
list_data3=[1,2,2,2,3]
print(list_data3.count(2))

#5.优质采.clear 清除，清空
list_data4=[1,2,3]
print(list_data4.clear())

#del()删除变量   len()获取容器里面的数据长度

#6.中国五矿集团采购信息.remove 删除，根据数据，根据值进行删除,只能删除一个
list_data5=[1,2,3,4]
list_data5.remove(4)
print(list_data5)

#7.copy 复制 浅复制
list_data6=[1,2,3,45]
b=list_data6.copy()
print(b)

#8.sort 对数据进行排序升序    reverse倒置
list_data7=[3,5,2,2]
list_data7.sort()
print(list_data7)
list_data7.sort(reverse=True)
print(list_data7)

#9.insert()插入
list_data8=[4,3,7]
list_data8.insert(2,7)
print(list_data8)
