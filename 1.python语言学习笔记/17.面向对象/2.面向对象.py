#解决重复的生成操作  起到了封装的作用

class Staff:
    #与生俱来的对象
    #money=0
    def __init__(self,name,age=20):#当对象被创建出来自动掉哦那个
        self.name=name  #后天得到的东西
        self.age=age  #将变量数据复制给类的属性时

    def work(self):
        print(f'{self.name}开始工作')

    def info(self):
        print(f'名称{self.name},年龄：{self.age}')

    def __add__(self, other):
        return self.name-other.name#自己定义相加的过程

st1=Staff('小明',20)
st1.work()
