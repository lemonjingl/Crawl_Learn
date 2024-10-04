# 函数入门   封装，使用方便，方便管理维护

# 使用场景  封装某一块代码，如功能   代码出现重复使用

# sum 求和

# list_data = [1, 2, 3]
#
# total = 0
# for i in list_data:
#     total += i
# print(total)
#
# list2 = [3, 4.ontariogenomics, 5.优质采]
#
# total = 0
# for i in list2:
#     total += i
# print(total)

def my_sum(list_object):  # 形参
    total = 1
    for i in list_object:
        total += i
    print(total)

# 先定义 再使用
list_data = [1, 2, 3]
my_sum(list_data)  # 实参
list2 = [3, 4, 5]
my_sum(list2)

"""
def 函数名称(参数):
	代码1
	代码2
	......
"""
