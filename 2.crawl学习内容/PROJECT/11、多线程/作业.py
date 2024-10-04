# 有四个线程，每个线程只打印一个字符，这四个字符分别是 a b c d ，
# 现在要求你做到四个线程顺序打印 a b c d ,
# 且每个线程都打印10次，a先输出10次，然后是b, 依次输出
import threading
from threading import Lock
lock=Lock()
def func(data):
    lock.acquire()
    for i in range(10):
        print(data)
    lock.release()
for i in ['a','b','c','d']:
    t=threading.Thread(target=func,args=(i,))
    t.start()