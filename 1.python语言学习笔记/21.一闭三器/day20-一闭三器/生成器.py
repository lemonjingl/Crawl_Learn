def func():  # 生成器  是一个特别一点的迭代器
    for i in range(5):
        yield i  # yield 讲数据返回到外面，但是不会杀死函数

# 生成器的作用就相当于一个工厂


data = func()


for i in data:
    print(i)


# print(dir(data))
# print(type(data))
# print(data)


# 生成器 当需要使用到数据的时候会生成一个数据给我们使用
# 生成器的使用场景  读非常大的文件 100G

# def func():
#     f = open()
#     yield f.readline()

