class F:
    money=1000000

    __designation='赌圣'

    def love(self):
        print('爱好打篮球')

class S(F):
    money=999999
    #重写方法或属性
    #重写 当父类的功能不满足使用的要求 对这个方法进行重写
    def love(self):#当属性或方法名称相同的时候进行重写
        F().love()#增加或修改父类的方法和属性
        print('爱好轮滑')
        print('向往诗与远方')

s=S()
s.love()
print(S.__mro__)