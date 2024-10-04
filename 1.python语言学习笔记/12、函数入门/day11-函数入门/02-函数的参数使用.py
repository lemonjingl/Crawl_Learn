# 函数说明文档
def add(number1, number2):
    """这个一个相加的函数"""
    # """
    # 这个一个相加的函数
    # :param a: a是一个数字
    # :param b: b是一个数字
    # :return: None
    # """
    data = number1 + number2

    return data

# return 将数据返回到外部进行使用
# 什么场景使用？ 当外部需要函数里面运行的结果的时候
# 不使用return 默认返回None

# return后会发生什么事情？ 回收(结束函数)

a = add(1,2)  # 实参和形参的位置，还有数量必须要一一对应
print(a)



