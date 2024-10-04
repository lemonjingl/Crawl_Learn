# super 函数  单指父类

# 单继承
class F:  # class F():  class F(object):
    money = 1000000

    __designation = '原子弹之父'

    def love(self):
        print('爱好钓鱼')
        print('爱好打牌')


class S(F):
    def love(self):
        # F().love()

        super().love()
        # super(S, self).love() 显示的写法

        print('爱好游戏')
        print('爱好游泳')

s = S()
s.love()

