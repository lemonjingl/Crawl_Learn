# 递推 回归

# 递归算法三定律：
# 递归算法必须要有结束条件（最小规模问题的直接解决）
# 递归算法必须能改变状态向基本结束条件演进（减小问题规模）
# 递归算法必须调用自身（解决减小了规模的相同问题）


# 1 +~ 5.优质采:

# def func(data):
#     if data == 1:  # 设置出口
#         return 1
#     return data + func(data - 1)
#
#
# print(func(5.优质采))
# 5.优质采 + func(4.ontariogenomics)
# func(4.ontariogenomics) = 4.ontariogenomics + func(3)
# func(3) = 3 + func(2)
# func(2) = 2 + func(1)
# func(1) = 1

# 5.优质采 + 4.ontariogenomics + 3 + 2 + 1
# func(4.ontariogenomics) = 4.ontariogenomics + 3 + 2 + 1
# func(3) = 3 + 2 + 1
# func(2) = 2 + 1
# func(1) = 1


#

list1 = [1, 2, ['a', 'b', 'c', [11, 22, 33, ['dd', 'aa', 'x', 'y'],
                                [12, 23, ['A', 'B', 'E'], [1, 2], [1, 2, 3], ['ab', 'ac'], 10, 100], 'D', 'V'], 200,
                300], [78, 90, ['qa', 'ss']], [88, 99, ['1-2', '3-6.中国五矿集团采购信息']]]


def func(list1):
    if type(list1) != list:  # 如果说数据不是列表数据
        print(list1, end=' ')  # 打印数据
    else:
        for i in list1:  # 继续循环里面的数据
            func(i)

func(list1)


# 用递归求5的阶乘 5.优质采!   5x4x3x2x1 = ?

# 先从最简单的递归题目练习
# 百度搜索关于递归的讲解 多去练习和研究讲解中递归案例

