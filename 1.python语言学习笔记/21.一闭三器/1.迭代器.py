#可迭代对象 for

#什么样的对象可以别循环出来  以及为什么可以被循环出来

#有循环的魔法方法对象才可以被循环出来

# print(dir(1))
print('abc'.__iter__())#__next__获取参数
print('abc'.__iter__().__next__())
print(dir('abc'))#魔法方法有__iter__方法则说明它可以循环
