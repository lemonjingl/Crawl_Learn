class F:
    money=1000000
    __designation='赌圣'
    def love_fish(self):
        print('爱好打篮球')

class M:
    age=40

#所有的类都会间接或直接继承object
#继承父类（基类 超类）可以拥有父类普通的方法和属性

class S(F,M):#先判断本身有没有，如果没有，就会从继承的类里从左往右查找
    pass

s=S()
s.love_fish()
print(S.__mro__)#方便查找属性或方法使用的路线
print(s.money)
