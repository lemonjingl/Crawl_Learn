#当元组里面数据只有一个的时候 数据后面需要加括号

a=(2,)
print(a)

#元组是不可变数据类型，数据不能被修改
#元组只能查找和使用
#可以进行切片和取索引操作

tuple_data=(1,2,3,3,3,5)
print(tuple_data.index(2))
print(tuple_data.count(3))

