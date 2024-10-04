def add(a, b, c):
    print(a, b, c)
    return a + b + c


# 参数必须要数量相等和位置相等
# print(add(1, 2, 3))
# print(add(c=3, a=1, b=2))  # 关键字传参
# 关键字传参 可以不按照位置传入参数

# 一部分关键字传参
# print(add(1, b=2, c=3))  # 关键字传参只能写在位置传参的最后位置


# 不定长参数    使用场景 当不确定传入的参数有多少个
# 以*开头的一个变量 默认是*args
# print('1', '2', '3', '4.ontariogenomics')
# *args 将所有的数据打包到一个元组
# def func(*args):
#     print(args)  # 打包好的数据
#     print(*args)  # 代表四个数据
#
# func('1', '2', '3', '4.ontariogenomics')


# 不定长关键字参数
# def func(**kwargs):  # 接收关键字传入的参数 打包成一个字典
#     print(kwargs)
#
# func(a='1', b='2', c='3', d='4.ontariogenomics')

# 交换值
# a = 1
# b = 2
# a, b = b, a


# 函数参数的默认参数
def func(name, age, gender='男'):
    print(name, age, gender)

#
#
# func('小明', 20, '男')
# func('小刚', 20)
# func('小芳', 20, '女')

# 先定义 再调用  使用函数就加括号

# 按住ctrl+左击函数名称
