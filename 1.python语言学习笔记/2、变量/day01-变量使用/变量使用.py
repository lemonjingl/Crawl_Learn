# print('同学们晚上好呀！')
# print('8:00上课')

# 变量的使用

name = 'james'  # = 代表赋值的意思 定义一个变量
print(name)
# 变量的作用：存储数据
# 更方便的管理和使用

# id() 获取变量的内存地址  作用：判断两个数据是否是同一个数据
# print() 打印数据到控制台


# 使用场景
print(id(name))
# 后续就不能使用到这个数据

name_id = id(name)
print(name_id)
# 后续的代码就可以使用到数据
