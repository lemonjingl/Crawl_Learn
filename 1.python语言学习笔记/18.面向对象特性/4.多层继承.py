class F:
    def fun1(self):
        print('实现一个功能')

class S(F):
    def fun2(self):
        print('实现两个功能')

class D(S):
    def fun2(self):
        print('实现一个功能')
#越是后面的子类，东西越多

d=D()
d.fun1()