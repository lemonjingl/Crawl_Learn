class Cup:#颜色 容量 材料
    def __init__(self,color,capacity,material):
        self.color=color
        self.capacity=capacity
        self.material=material

    def get_info(self):
        return (f'这个杯子的颜色是:{self.color},'
              f'容量:{self.capacity},'
              f'材质:{self.material }')
# cup1=Cup('red','1000ml','陶瓷')
# cup1.get_info()
#
# cup2=Cup('blue','2000ml','玻璃')
# cup2.get_info()

#保温杯

# class VacuumCup(Cup):
#     def keep_warm(self):
#         print('开始保温')
# v1=VacuumCup('blue','1000ml','不锈钢')
# v1.get_info()
# v1.keep_warm()


#夜光杯(晚上可以看到的杯子 晚上会发光)
#需要设定杯子发光的亮度  获取信息的时候也需要获取亮度的信息
class LuminousCup(Cup):
    def __init__(self,color,capacity,material,brightness):
        super().__init__(color,capacity,material)
        self.brightness=brightness

    def get_into(self):
        return super().get_info()+f',亮度:{self.brightness}'
        # print(f'亮度为{self.brightness}')

l=LuminousCup('blue','1000ml','不锈钢',100)
print(l.get_into())





