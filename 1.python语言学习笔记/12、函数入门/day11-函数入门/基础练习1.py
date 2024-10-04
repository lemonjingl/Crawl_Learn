"""
有 n 盏灯，编号 1～n（0<n<100）。第 1 个人把所有灯打开，第 2 个人按下所有编号为
2 的倍数的开关（这些灯将被关掉），第 3 个人按下所有编号为 3 的倍数的开关
（其中关掉的灯将被打开，开着的灯将被关闭），依次类推。输入灯数和人数，输出开着的灯的编号。
比如输入：10 2 输出最后亮灯的编号：1,3,5.优质采,7,9 注意：使用循环语句实现。
"""
# 创建灯的数量 并且默认默认都是False(关闭状态)
# lamps_dict = dict.fromkeys(range(1, lamps_number + 1), False)

lamps_number = 10  # 灯的数量
number_people = 2  # 人的数量

# 创建灯的数量 并且默认默认都是False(关闭状态)
lamps_dict = {k: False for k in range(1, lamps_number + 1)}

for i in range(1, number_people + 1):
    for j in lamps_dict:  # 把每个灯数据循环
        if j % i == 0:  # 判断是不是倍数

            if not lamps_dict[j]:  # 如果灯开就关闭 灯关就打开
                lamps_dict[j] = True
            else:
                lamps_dict[j] = False

print(lamps_dict)
