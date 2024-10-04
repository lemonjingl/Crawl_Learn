#io   密集计算

# import multiprocessing
# import threading
# import time
# import threading
# lock=threading.Lock()
'''
lock                                      rlocks
lock对象无法再被其他线程获取，除非持有线程释放  rlock对象可以被其他线程多次获取
lock对象可被任何线程释放                     rlock对象只能被持有的线程释放
lock对象不可以被任何线程拥有                  rlock对象可以被多个线程拥有
对一个对象锁定是很快的                        对一个对象加rlock比加lock慢

线程与进程的比较

进程                            线程
进程时正在运行中的程序             线程是进程的一个程序段
创建进程耗费的时间多一些           创建线程耗费的时间少一些
退出进程耗费的时间多一些           退出线程耗费的时间少一些
进程间切换耗费时间多一些           线程间切换耗费时间少一些
进程间的通信效率低一些             线程间的通信效率高一些
进程需要耗费更多的系统资源          线程消耗的系统资源相对少
进程拥有独立内存空间                线程间可共享进程内存
进程可基于操作系统应有接口切换       线程基于CPU时间片调度切换
一个进程被阻塞后其他进程需要等待     一个线程被阻塞后，其他线程可以继续运行
进程拥有独立进程控制块              线程共享控制块并有独立堆栈和寄存器
'''

# def func():
#     print('函数正在运行')
#     time.sleep(3)
#     print('函数运行完成')
#
# if __name__ == '__main__':
#     p=multiprocessing.Process(target=func)
#     lock.acquire()
#     print(lock)
#     p.start()
#     print(lock)
#     print('我是主程序')
#     lock.release()
#     print(lock)


#进程通信
import multiprocessing
from queue import Queue
q=Queue()
def func():
    print('函数正在运行')
    q.put(14)
    print('函数运行结束')

def func1():
    print('函数正在运行')
    q.get()
    print('函数运行结束')

if __name__=="__main__":
    p=multiprocessing.Process(target=func)
    p.start()
    p1=multiprocessing.Process(target=func1)
    p1.start()