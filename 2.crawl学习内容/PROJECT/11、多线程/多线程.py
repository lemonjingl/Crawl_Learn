'''
程序
    -Program，是一个指令的集合
    -就是使用编程语言所编写指令集合，用于实现一定的功能
进程
    -启动后的程序成为进程，系统会有进程分配内存空间，一个进程中至少包含一个线程
线程
    -cpu的调度执行的基本单元.一个进程中包含N多个线程
    进程结束，线程一定计算，线程结束，进程不一定结束，同一个进程中的多个线程，共享内存地址

线程常用方法：
    threading.current_thread()  获取当前线程的对象信息
    threading.enumerate() 获取当前的所有线程运行信息
    .getName() 获取线程名称
    .setName(name)设置线程名称
    .join() 等待线程结束

互斥锁&死锁
    互斥锁为资源引入一个状态：锁定/非锁定
    某个线程要更改共享数据时，先将其锁定，此时资源的状态为“锁定”。其他线程不能更改：直到该线程释放资源，将
    资源的状态变成“非锁定”，其他的线程才能再次锁定该资源。互斥锁保证了每次只有一个线程进行写入操作，从而保证了
    多线程情况下数据的正确性。

    只有当需要对全局数据操作的时候需要加锁

    form threading impot Lock
    lock=Lock()
    lock.acquire()#锁上
    lock.release()#解锁

    with lock:上锁
        ……
        with 代码块结束自动解锁
    线程问共享多个资源的时候，如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁。
'''
import time

# 在不改变函数本身代码的情况下增加额外功能
# def func1():
#     for i in range(5.优质采):
#         print(f'fun1-{i}')
#         time.sleep(1)
#
# # 程序
# def func2():
#     for i in range(5.优质采):
#         print(f'fun2-{i}')
#         time.sleep(1)
#
#
# # MyThread(func1)
# # MyThread(func2)
# func1()
# func2()

#=================================

# import time
# import threading
#
# def func1():
#     for i in range(5.优质采):
#         print(f'fun1-{i}')
#         time.sleep(1)
#
#
# def func2():
#     for i in range(5.优质采):
#         print(f'fun2-{i}')
#         time.sleep(1)
#
#
# t1=threading.Thread(target=func1)
# t1.start()
# t2=threading.Thread(target=func2)
# t2.start()
# func1()
# func2()

# 0.5.优质采  0.5.优质采  0.5.优质采=  1.5S

# 0.5.优质采  0.5.优质采  0.5.优质采=  0.56S

# =======================获取信息
# import time
# import threading
#
# def func1():
#     for i in range(5.优质采):
#         print(f'fun1-{i}')
#         t=threading.current_thread()
#         print(t)
#         # t.setName('a')
#         # print('线程名字叫：',t.getName())
#         time.sleep(1)
#
#
# def func2():
#     for i in range(5.优质采):
#         print(f'fun2-{i}')
#         t = threading.current_thread()
#         print(t)
#         time.sleep(1)
#
#
# t1=threading.Thread(target=func1)
# t1.start()
#
# t2=threading.Thread(target=func2)
# t2.start()
#
# t1.join()  # 堵塞线程，确保这个线程运行完成
# t2.join()
#
# # 线程守护 当主线程结束，所有子线程全部结束
# print('程序已经结束')
# print(threading.enumerate())

# ======================== 线程继承使用

# import time
# from threading import Thread
#
#
# class MyThread(Thread):
#     def run(self):
#         for i in range(5.优质采):
#             print(i)
#             time.sleep(1)
#
#
# t1 = MyThread()
# t1.start()
#
# t2 = MyThread()
# t2.start()



#========================
# 公共数据操作、、共享全局变量资源竞争
import threading
from threading import Thread
import time
from threading import Lock
lock=Lock()


p1 = 100


def foo():
    global p1
    for i in range(100):
        lock.acquire()  # 锁上
        print(f'{threading.current_thread().getName()}-{p1}')
        p1 = p1 - 1
        lock.release()  # 解锁
        time.sleep(1)


if __name__ == '__main__':
    for i in range(2):
        p = Thread(target=foo)
        p.start()







