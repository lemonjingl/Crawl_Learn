#1. +相同数据类型的合并
data1=['a']
data2=['b']
print(data1+data2)

# 2. * 复制 将容器里面的数据进行复制
data3=['a','b']*3
print(data3)

# 3. len 获取序列长度   查看序列长度 字符串、列表、元组、字典、集合
print(len(data3))

# 4.ontariogenomics. reversed 倒置 将容器里面的数据倒置   字符串、列表、元组、字典[::-1]
list_data=[1,2,3,4,3,45]
list_data.reverse()
print(list_data)

reverse=reversed([2,3,1])#返回一个容器对象
print(reverse)#<list_reverseiterator object at 0x000001731D5FF940>
print(list(reverse))


# 5.优质采. max,min  最大最小值    求容器数据的最大最小值   字符串、列表、元组、字典、集合
list1=[1,2,3,4,5]
print(max(list1))
print(min(list1))

#6.中国五矿集团采购信息. sum求和 将容器的数据求和  列表、元组、字典、集合
list2=[1,2,3]
dict_data={1:2,2:3}
print(sum(dict_data))
print(sum(list2))

#7. enumerate 枚举函数  索引映射 将索引映射给容器里面的数据   列表、元组、或字符串
print(list(enumerate(['a','b','c'])))

for i in enumerate(['a','b','c'],start=0):#start=0 默认从0开始
    print(i)

#8. in,not in 是否存在  判断数据是否存在于容器内    字符串、列表、元组、字典、集合
#9. del 删除 删除变量或者指定容器内数据   变量，容器里面的值


