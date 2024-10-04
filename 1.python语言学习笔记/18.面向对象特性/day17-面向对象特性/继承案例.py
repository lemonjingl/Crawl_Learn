class Cup:  # 颜色 容量 材料
    def __init__(self, color, capacity, materials):
        self.color = color
        self.capacity = capacity
        self.materials = materials

    def get_info(self):
        return f'这个杯子的颜色是:{self.color},' \
               f'容量:{self.capacity}，' \
               f'材质:{self.materials}'


# cup1 = Cup('red','2000ml','玻璃')
# cup1.get_info()
#
# cup2 = Cup('blue','1000ml','陶瓷')
# cup2.get_info()

# 保温杯
# class VacuumCup(Cup):
#     def keep_warm(self):
#         print('开始保温')
#
#
# v1 = VacuumCup('blue', '1000ml', '不锈钢')
# v1.get_info()
# v1.keep_warm()


# 夜光杯(晚上可以看到的杯子 晚上会发光)
# 需要设定杯子发光的亮度 获取信息的时候也需要获取亮度的信息

class LuminousCup(Cup):
    def __init__(self, color, capacity, materials, light):
        super().__init__(color, capacity, materials)
        self.light = light

    # def get_info(self):
    #     return f'这个杯子的颜色是:{self.color},' \
    #            f'容量:{self.capacity}，' \
    #            f'材质:{self.materials}，' \
    #            f'亮度:{self.light}'

    def get_info(self):
        return super().get_info() + f',亮度:{self.light}'


l1 = LuminousCup('blue', '1000ml', '不锈钢', 1000)
print(l1.get_info())
