import threading
import time

class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n=n

    def run(self):
        print('使用类的方式创建多线程',self.n)
        time.sleep(3)

r1=MyThread(1)
r2=MyThread(2)
r1.start()
r2.start()