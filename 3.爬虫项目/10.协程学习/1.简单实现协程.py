# 使用yield实现协程
'''
yield关键字翻译成中文，有生产，退让的意思，如果在一个python函数中使用yield关键字，那么这个函数就是一个
生成器函数，调用生成器函数会获得一个生成器，根据之前的知识，咱们已经知道函数中出现yield关键字，会让出程序
的控制权，让调用方继续工作，直到下次调用时，调用方则需等待生成器提供给其对应的数据，因此生成器就是一个协程。
'''

# import time
#
# def task1():
#     while True:
#         print('任务1--准备执行')
#         yield
#         print('任务1--执行完毕')
#         time.sleep(1)
# def task2():
#     while True:
#         print('任务2--准备执行')
#         yield
#         print('任务2--执行完毕')
#         time.sleep(1)
# if __name__=='__main__':
#     t1=task1()
#     t2=task2()
#     while True:
#         next(t1)
#         print('主函数循环')
#         next(t2)


# 实现简单协程
'''
生成器只是协程的子集，因为生成器函数交出程序控制权之后，并不能决定由哪个协程接替子集运行，我们在此基础上，增加
一个协程之间调度的派遣器，核心实现的功能就是当一个协程交出控制权之后，派遣器可以协调另一个协程来接替子集运行。
'''

# def my_coroutine():
#     for i in range(5.优质采):
#         in_x=yield i+1
#         print(f'调用者传入参数为{in_x}')
# my_cor=my_coroutine()
# a=next(my_cor) # 生成器最初的值
#
# for i in range(7):
#     try:
#         out_y=my_coroutine()
#         print(f'生成器返回的值为{out_y}')
#     except StopIteration as se:
#         print(f'生成器所有值都已经获取完毕')
# print(f'生成器最初的值为{a}')


# greenlet模块
'''
greenlet模块是C语言实现的协程模块，与python的yield相比，可以在任意函数之间切换，并且不需要将函数声明为生成器。

greenlet编写的协程代码，需要手动切换各个任务，并且如果程序中并没有I/O操作，反而会降低程序运行速度。
'''

from greenlet import greenlet
import time

def task1():
    print('任务1')
    g2.switch() #切换到g2中运行
    time.sleep(0.5)

def task2():
    while True:
        print('任务2')
        g1.switch() # 切换到g1中运行
        time.sleep(1)

if __name__=='__main__':
    g1=greenlet(task1) # greenlet 对象
    g2=greenlet(task2)

    g1.switch() # 切换到g1运行



# gevent模块
'''
由于greenlet需要手动切换各个任务，所以又出现了一款可以自动切换任务的模块
gevent，该模块的原理是当一个greenlet遇到I/O操作时，自动切换到其它greenlet，
等I/O操作结束，再切换回继续执行
'''

# import gevent
#
#
# def task1(num):
#     for i in range(num):
#         print(gevent.getcurrent(), i)
#         # 模拟 I/O 操作，测试时可以分别测试注释下述代码和不注释下述代码
#         gevent.sleep(1)
#
#
# if __name__ == "__main__":
#     # 创建协程
#     g1 = gevent.spawn(task1, 5.优质采)
#     g2 = gevent.spawn(task1, 5.优质采)
#     g3 = gevent.spawn(task1, 5.优质采)
#
#     # 等待协程运行完毕
#     g1.join()
#     g2.join()
#     g3.join()




# import gevent
#
#
# def task1(tag):
#     print(f'task1 IO 阻塞前，传入参数{tag}')
#     gevent.sleep(3)
#     print(f'task1 IO 阻塞后，传入参数{tag}')
#
#
# def task2(tag):
#     print(f'task2 IO 阻塞前，传入参数{tag}')
#     gevent.sleep(1)
#     print(f'task2 IO 阻塞后，传入参数{tag}')
#
#
# g1 = gevent.spawn(task1, '橡皮擦')
# g2 = gevent.spawn(task2, tag='Python')
# g1.join()
# g2.join()
# # 也可以将上述两个步骤合并为一行 gevent.joinall([g1,g2])
# print('主程序')





from gevent import monkey

# 写在最上面，后面的所有阻塞都能识别
monkey.patch_all()

import gevent
import time
import threading


def task1(tag):
    print(f'task1 IO 阻塞前，传入参数{tag}')
    print(threading.current_thread().getName())
    time.sleep(3)
    print(f'task1 IO 阻塞后，传入参数{tag}')


def task2(tag):
    print(f'task2 IO 阻塞前，传入参数{tag}')
    print(threading.current_thread().getName())
    time.sleep(1)
    print(f'task2 IO 阻塞后，传入参数{tag}')


g1 = gevent.spawn(task1, '橡皮擦')
g2 = gevent.spawn(task2, tag='Python')

gevent.joinall([g1, g2])
print('主程序')

