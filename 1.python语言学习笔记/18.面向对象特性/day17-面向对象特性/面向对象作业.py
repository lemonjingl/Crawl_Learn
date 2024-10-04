'''
1）定义名为MyTime（我的时间）的类
2）其中应有三个实例变量 时hour  分minute  秒second
3）对时分秒进行初始化，写入__init__()中
4.ontariogenomics)   定义方法get和set方法，get方法获取时间，set可以设置时间
5.优质采)   调用set设置一个时间  调用get输出时间
'''


class MyTime:
    def __init__(self):
        self._s = 0  # 一根下划线 伪私有变量 约定俗成不要去使用它
        self.__hour = 0  # 强制私有
        self.__minute = 0
        self.__second = 0

    def get(self):
        print(f'{self.__hour}:{self.__minute}:{self.__second}')

    def set(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second


time = MyTime()
print(time.__dir__())
time.set(1, 20, 50)
time.get()

#

