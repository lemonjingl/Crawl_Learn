# 解决重复的生成操作 起到了封装的作用
class Staff:
    # 与生俱来的对象
    # money = 0
    def __init__(self, name, age=20):  # 当对象被创建出来自动调用
        self.name = name  # 后天得到的东西
        self.age = age  # 将变量数据赋值给类的属性时，
        # 其他的方法可以直接使用类的所有属性

    # def __str__(self):
    #     return f'Staff [({self.name},{self.age})]'

    def work(self):
        print(f'{self.name}开始工作')

    def info(self):
        print(f'名称:{self.name}，年龄:{self.age}')

    def __add__(self, other):
        return self.name - other.name  # 自己定义相加的过程


st1 = Staff('小明', 20)
# st1.info()
# st1.color = 'yellow'
# print(st1.color)


st2 = Staff('小刚', 25)
# st2.info()
# st2.work1()



# [1,2,3] * 2

# class File:
#
#     def open(self):
#         pass
#
#     def close(self):
#         pass
#
#     def read(self):
#         pass
#
# f1 = File()
# f1.read()
# f1.close()
#
# f1 = File()
# f1.read()
# f1.close()

# f = open('data7')
# f.read()
# f.close()


# 使用场景
# dict_data1 = {'id': Staff('小刚', 25)}
#
# dict_data2 = {'id': {'name': '??', 'age': 20},
#               'id2': {'name': '??', 'age': 20},
#               'id3': {'name': '??', 'age': 20}}


