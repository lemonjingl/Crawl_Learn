# 导入模块分为相对路径和绝对路径

# import test
# test.demo.func([1])
# print(test.func([1]))

# from .test import func
# from ..test import demo
from test.demo import func
print(func([1]))


# 外部的文件引入内部文件 可以正常使用相对路径和绝对路径
# 内部文件引入外部的数据 只能使用绝对路径,尽量不要使用相对路径导入






