import time


def outer(func):
    def inner(a, b):
        start = time.time()  # 记录开始时间

        data = func(a, b)

        stop = time.time()
        print(stop - start)  # 打印代码运行的时间
        return data

    return inner


# @outer
# def func2():
#     print(2 + 2)
# func2()

@outer
def func1(a, b):
    return a + b
    # print(1 + 1)
    # time.sleep(2)  # 休眠两秒  模拟函数运行的时间


print(func1(1, 2))

# 传入的是一个字符串，能不能传入一个函数到里面去呢？
# func2 = outer(func2)  # 数据从外部函数进入 从内部函数使用
# @outer == func2 = outer(func2)


def outer(func):
    def inner(*args):
        # 代码运行前加功能
        data = func(*args)
        # 代码运行后加功能
        return data
    return inner