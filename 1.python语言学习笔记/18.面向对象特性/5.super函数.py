#super函数    单指父类
class F():
    money = 100000
    __designation = '原子弹之父'

    def love(self):
        print('爱好刷手机')
        print('爱好游泳')

class S(F):
    def love(self):
        super().love()#隐式写法
        #super(S,self).love() #显示写法
        print('爱好轮滑')

s=S()
s.love()



