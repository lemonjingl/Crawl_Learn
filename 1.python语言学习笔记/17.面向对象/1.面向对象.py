#面向对象 是一种编程的思维模式

# 类 对象
#类继承于对象  类创建对象

#类是抽象的，不存在的事物

# 特征即属性
# 行为是方法
#
# 一个类可以创建多个对象
#类：类具有同一特征的事物，是抽象的，不是真实存在的事物
# 面向对象中 变量叫做属性  函数叫做方法
'''
实例属性和类属性
私有属性被私有化后，即使是继承它的子类也不能访问。

方法：实例方法、类方法、静态方法
类方法：方法上面带有装饰器@classmethod  类方法只能修改类属性，不能修改实例属性
'''
class WashingMachine:
    h=900
    w=800
    c=589
    brand='海尔'

    #self 自己 具体的一个对象

    def __init__(self):
        self.__color='red'#设置属性或者方法为私有方法
        #在属性或者方法前加两根下划线

    def get_color(self):
        '''获取颜色'''
        return self.__color

    def set_color(self,color):
        '''设置颜色'''
        if color in ['red','blue','yellow']:
            self.__color=color
        else:
            print('违规的颜色')

    def start(self):
        print('启动洗衣机，开始洗衣服')

    def stop(self):
        print('关闭洗衣机')

#类通过加括号来进行使用  生成一个具体的对象
haier1=WashingMachine()
haier1.set_color('blue')

print(haier1.get_color())  # 通过get方法获取当前的颜色


# haier1.h = 600  # 修改对象的属性
# haier1.start()  # 通过.方法调用对应的功能
# print(f'洗衣机高度：',haier1.h)  # 获取对象的属性


# haier2 = WashingMachine()
# haier2.start()
