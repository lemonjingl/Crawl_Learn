#生产者与消费着

#2个大人  3个小孩

#两个线程
import random
import threading
g_money=100000
lock=threading.Lock()

def add(i):#挣钱操作
    m=random.randint(1000,10000)#大人挣的钱
    global g_money
    lock.acquire()
    g_money+=m
    lock.release()
    print(f'第{i}挣得钱{m},还剩{g_money}')

def reduce(it):
    global g_money
    r=random.randint(100,1000)
    if g_money-r<0:
        print(f'家里小孩花的钱超了停止消费')
        return
    lock.acquire()
    g_money-=r
    lock.release()
    print(f'家里面小孩花的钱{r},还剩{g_money}')

for i in range(30):
    for i in range(2):
        t=threading.Thread(target=add,args=(i,))
        t.start()

    for it in range(3):
        t1=threading.Thread(target=reduce,args=(it,))
        t1.start()

