#线程，进程
#进程是一个资源单位，线程是执行单位，每一个进程至少有一个线程

#启动每一个程序默认都会有一个主线程
from threading import  Thread

# def func():
#     for i in range(100):
#         print('func',i)
# if __name__=='__main__':
#     t=Thread(target=func)
#     t.start()
#     for i in range(100):
#         print('main',i)


#类继承写法
class MyThread(Thread):
    def run(self):#固定的
        for i in range(100):
            print('子线程',i)
if __name__=='__main__':
    t=MyThread()
    t.start()
    for i in range(100):
        print('主线程',i)






