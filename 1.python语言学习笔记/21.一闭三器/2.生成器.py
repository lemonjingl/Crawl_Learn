def func():#生成器    是一个特别的一个迭代器
    for i in range(5):
        yield i   #yield 将数据返回到外面，但是不会杀死函数

data=func()
print(data.__next__())
print(data.__next__())
print(dir(data))
print(type(data))
#作用：生成器的作用就相当于一个工厂
#生成器 当需要使用到数据的时候会生成一个数据给我们使用
#生成器的使用场景  读非常大的文件 100G  （你需要一个我拿一个）