class F:  # object 隐试的 显示的
    def fun1(self):
        print('实现一个功能')


class S(F):
    def fun2(self):
        print('实现一个功能')


class D(S):
    def fun3(self):
        print('实现一个功能')


# 越是后面的子类，继承的东西就越多
d = D()
#  9:17 上课
