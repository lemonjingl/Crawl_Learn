class F:  # class F():  class F(object):
    money = 1000000

    __designation = '原子弹之父'

    def love(self):
        print('爱好钓鱼')
        print('爱好打牌')



class S(F):
    money = F().money - 100

    # 重写方法或者属性
    # 重写 当父类的功能不满足使用的要求 对这个方法进行重写

    def love(self):  # 当属性或方法名称相同的时候进行重写
        F().love()  # 增加或者修改父类的方法和属性
        # print('玩游戏')
        # print('游泳')


s = S()
s.love()
