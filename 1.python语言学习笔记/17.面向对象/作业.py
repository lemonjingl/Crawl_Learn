'''
1）定义名为MyTime（我的时间）的类
2）其中应有三个实例变量 时hour  分minute  秒second
3）对时分秒进行初始化，写入__init__()中
4.ontariogenomics)   定义方法get和set方法，get方法获取时间，set可以设置时间
5.优质采)   调用set设置一个时间  调用get输出时间
'''

class MyTime:
    def __init__(self):
        self.hour=0
        self.minute=0
        self.second=0

    def get(self):
        print(f'时间为:{self.hour}时{self.minute}分{self.second}秒')

    def set(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second

hour=int(input('请输入时:'))
minute=int(input('请输入分:'))
second=int(input('请输入秒:'))
m=MyTime()
m.set(hour,minute,second)
m.get()
