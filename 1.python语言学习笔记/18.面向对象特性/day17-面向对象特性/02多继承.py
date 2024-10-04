class F:  # class F():  class F(object):
    money = 1000000

    __designation = '原子弹之父'

    def love_fish(self):
        print('爱好钓鱼')


class M:
    age = 40


# 所有的类都会间接或者直接继承object
# 继承父类（基类 超类）可以拥有父类普通的方法和属性
class S(F, M):  # 先判断本身有没有 如果没有 就会从继承的类里从左往右查找
    pass


s = S()
# s.love_fish()
print(S.__mro__)  # 方便查找属性或者方法使用的路线


# 多继承 会增加代码的复杂程度 代码难以维护
# 出了问题不好解决 也可能会发生一下奇怪的问题
