# 装饰器  在原有的函数上新加一些东西
# 在不改变函数原本代码的前提下为其增加新的功能
import time

def func1():
    start=time.time()
    print(1+1)
    time.sleep(2)#休息2秒
    stop=time.time()
    print(stop-start)#打印代码运行的时间

def func2():
    print(2+2)

func1()

#计算代码所需要运行的时间
