# is  is not
# 判断两个数据的内存地址是否一样

a = 10
b = 10
print(a is b)
print(a is not b)
print(id(a) == id(b))
