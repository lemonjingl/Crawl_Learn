# 函数的作用域  全局变量  局部变量

# 全局变量 定义在函数外部的变量
# 局部变量 定义在函数里面的变量

# data = 100
#
#
# def func():
#     loacl = 50
#
#     pass

# 不可变数据类型在函数里面使用
# 不可变数据类型是可读不可写
# data = 100
#
# def func():
#     global data  # 正常的使用外部的变量  声明变量为全局变量
#     # print(data)
#     data = data + 1
#
# func()

# 可变数据类型
# data = [1, 2, 3]
#
# def func():
#     data.pop()
#     print(data)
#
# func()
# print(data)
