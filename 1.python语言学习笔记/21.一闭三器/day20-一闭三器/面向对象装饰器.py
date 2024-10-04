# 静态方法
# 类方法
class S:
    def __init__(self):
        pass

    @staticmethod  # 将方法变成静态方法
    def speak():  # 没有使用关于对象的方法
        print('你好')

    def speak1(self):  # 没有使用关于对象的方法
        print('你好')


class D:
    def __init__(self, x, m):
        self.x = x
        self.m = m

    def speak(self):
        print(f'{self.x}{self.m}')

    @classmethod  # 类方法
    def text(cls):  # cls???
        return cls('王','小明')


# d = D.text()
# d.speak()

# d = D('王','小明')  # 经常使用某个名称 或者需要测试数据
# d.speak()


class WashingMachine:
    h = 850
    w = 460
    c = 595
    brand = '海尔'

    # self 自己 具体的一个对象

    def __init__(self):
        self.__color = 'red'  # 设置属性或者方法为私有方法
        # 在属性或者方法前加两根下划线

    @property  # 将方法伪装成一个属性  让方法像属性一样使用
    def color(self):
        """获取颜色"""
        return self.__color

    @color.setter
    def color(self, color):
        """设置颜色"""
        if color in ['red', 'blue', 'yellow']:
            self.__color = color
        else:
            print('违规的颜色')

    def start(self):
        print('启动洗衣机，开始洗衣服')

    def stop(self):
        print('关闭洗衣机')


# 类通过加括号来进行使用 生成一个具体的对象
haier1 = WashingMachine()
# haier1.set_color('blue')  # 通过给予的修改方法，去修改对象里面的颜色
haier1.color = '200'
print(haier1.color)  # 通过get方法获取当前的颜色
