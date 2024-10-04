# 一、I/O密集型任务
'''
密集型任务指的硬盘I/O占主要任务，程序计算量很小，大部分时间都用在请求网页和读写文件上，这种情况，CPU经常等待I/O
操作完成，所以可以利用这些时间去完成其它事务。
基于上述内容，I/O密集型任务，采用多线程就可以提高程序执行效率，当然采用多进程也是可以的，但是多进程会出现共享资源
和通讯问题，因此，I/O密集型任务，采用多线程即可。
'''

# 二、计算密集型任务
'''
也叫做CPU密集型任务，在这种情况下，CPU注意满负荷状态，例如大数据查找，大字符串处理。
计算密集型任务在python中一般采用多进程处理，因为python中的多线程有同步锁安全机制，并且
采用的是全局锁，所以即便使用多核CPU，同一时间，也只有一个线程在执行。
'''

# 三、阻塞和非阻塞
'''
阻塞状态指程序未得到所需资源时，被挂起的状态，在这个状态下，程序必须等待某个操作完成，自身无法继续运行。

引起阻塞的常见原因：
    1.网络I/O阻塞
    2.硬盘I/O阻塞
    3.用户输入阻塞

非阻塞是因阻塞而存在，我们的目标就是实现程序在等待某个操作的过程中，自身不被阻塞，可以继续运行。非阻塞是为了
提高程序整体执行效率。
'''

# 四、同步和异步
'''
初学阶段，同步可以理解为，不同程序之间为了保证数据的一致性，必须依赖某种通信机制，实现程序单元之间的数据同步性，
同步是有序的，例如大家同时去秒杀10件商品，不管你在手机端，网页端，平板端，商品只有10件。

异步表示在不同程序之间，不需要保证数据的一致性，可以分别执行，异步是无序的，例如咱们之前写的爬虫程序，一堆图片，分别下载即可
谁先下载谁后下载没有区别，异步是高效组织非阻塞任务。
'''

# 五、并发与并行
'''
并发：描述的是程序的组织结构，程序要被设计程多个可独立执行的子任务，从而可以利用有限的计算机资源使多个任务可以
被实时或者近实时的执行，核心是为了让独立的子任务尽快运行，但整体进度不一定有变化。

并行：描述的是程序的执行状态，指多个任务同时被执行，从而可以利用富余的计算机资源（多核CPU）加速完成多个任务，核心是利用多核。
'''

# 六、协程基本知识
'''
协程不是python专属概念，它仅仅是一个普通的计算机概念，任何语言都有自己的实现。协程是单线程下的并发。

协程：也叫作微线程，纤程。
协程的作用：在执行函数A时，随时中断去执行函数B，然后再中断函数B，返回来执行函数A，该操作类似多线程，但协程中只有一个线程再执行。

协程的优势：
    1.非常适用于I/O密集型任务
    2.执行效率高（切换函数，而不切换线程，没有多余开销）
    3.不需要锁机制
    
协程的劣势：
    1.无法利用多核资源
    2.进行阻塞操作会阻塞掉整个程序
'''