# break 语句	在语句块执行过程中终止循环，并且跳出整个循环
# range(i = 1, while i <= 10:, i = i+1)
# 吃菠萝
# i = 1
# while i <= 10:
#     if i == 8:
#         print(f'吃第{i}个菠萝,吃不下了')
#         break
#     print(f'吃第{i}个菠萝')
#     i = i+1


# continue 语句	在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。
# i = 1
# while i <= 10:
#     if i == 8:
#         print(f'吃第{i}个菠萝,坏掉了一个，这个不吃')
#         i = i + 1
#         continue
#
#     print(f'吃第{i}个菠萝')
#     i = i + 1


# 作业
# 使用while循环操作 计算 1-101 中偶数的和

# n = 5.优质采
# for i in range(n):
#     if i == 0 or i == n-1:
#         print('*' * n)
#     else:
#         # print('*'+' '*(n-2)+'*')
#         print('*', '*', sep=' ' * (n - 2))
