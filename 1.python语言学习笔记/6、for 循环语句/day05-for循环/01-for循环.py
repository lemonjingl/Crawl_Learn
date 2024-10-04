# while  无限循环 完全不确定循环次数
# for    指定循环的次数 大概的知道要循环多少次

# range(start,stop,步长) 区间1~100  创建一个range对象
# print(range(1, 1000))

'''
for 零时变量 in 可迭代对象:
	重复执行的代码1
	重复执行的代码2
	.......
'''

str_data = 'abcd'
# for 提取容器里面的所有数据输出  循环做某个事情

# 循环的运行次数和字符串里面的数据个数有关
for i in str_data:  # 在容器里面从左往右获取数据
    if i == 'b':
        pass  # 不做任何操作
    else:
        print(i)
