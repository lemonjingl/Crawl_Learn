# 可迭代对象 for

# 什么样的对象可以被循环出来 以及为什么可以被循环出来
# for i in object:

# 有循环的魔法方法对象才可以被循环出来

# print(dir(1))
# print('abc'.__iter__())  # __next__ 获取参数
# data = 'abc'.__iter__()
# print(data.__next__())
# print(data.__next__())
# print(data.__next__())
# print(data.__next__())  # StopIteration

# print(dir('abc'.__iter__()))
# print(dir('abc'))  # __iter__

# for i in 'abc':  # 对这个对象使用 __iter__
#     pass

