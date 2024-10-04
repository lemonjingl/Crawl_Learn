# 装饰器  在原有的函数上新加一些东西
# 在不改变函数原本代码的前提下为其增加新的功能
import time


def func1():
    start = time.time()  # 记录开始时间

    print(1 + 1)
    time.sleep(2)  # 休眠两秒  模拟函数运行的时间

    stop = time.time()
    print(stop-start)  # 打印代码运行的时间


# func1()

def func2():

    print(2 + 2)



func2()

# 需要这个功能的代码很多 统一管理和维护
# 使用场景
# 计算代码所需要运行的时间
