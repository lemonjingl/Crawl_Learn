class A:
    # 当你有了这个魔法方法，就相对于有了这个功能
    def __len__(self):
        return 0

    def __init__(self):  # 初始化魔法方法  当函数被生成的时候自动调用
        # 作为类的参数传入
        pass


a = A()
print(a.__dir__())
print(len(a))

# int_data = 10
# str_data = '10'
# # print(len(str_data))
# print(int_data.__dir__())