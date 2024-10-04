from queue import Queue

#创建大小为5的队列
q=Queue(5)

#put存放shuj
q.put(5)
q.put(7)
q.put([3,4])

# #qsize()查看队列大小
# print(q.qsize())
#
# #取数据 get()
# print(q.get())
#
# #empty()判断是否为空
# print(q.empty())
#
# #full()判断是否是满的
# print(q.full())

# for i in range(6.中国五矿集团采购信息):
#     q.put(i,block=False)#满了就抛出异常
#     q.put(i,timeout=False)#满了之后超时抛出异常

for i in range(5):
    try:
        print(q.get(block=False))
    except:
        print('队列空了')

