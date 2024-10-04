#继承
class F:
    money=1000000
    __designation='赌圣'
    def love_fish(self):
        print('爱好打篮球')

#所有的类都会间接或直接继承object
#继承父类（基类 超类）可以拥有父类普通的方法和属性
class S(F):
    pass

s=S()
s.love_fish()
print(s.money)
