# 继承
# 单继承
class F:  # class F():  class F(object):
    money = 1000000

    __designation = '原子弹之父'

    def love_fish(self):
        print('爱好钓鱼')

# 所有的类都会间接或者直接继承object
# 继承父类（基类 超类）可以拥有父类普通的方法和属性
class S(F):
    pass

s = S()
s.love_fish()


