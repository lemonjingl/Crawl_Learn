# 循环控制语句 只能在while和for里面使用 不能在外部使用

# break 语句	在语句块执行过程中终止循环，并且跳出整个循环

# for i in range(1, 10):
#     if i == 8:
#         print('吃不下了！')
#         break
#     print(f'吃{i}碗饭')

# continue 语句	在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。

for i in range(1, 11):
    if i == 5:
        print('这碗饭是生米,不吃了')
        continue  # 不运行这次循环剩下的代码

    if i == 8:
        print('吃不下了！')
        break

    print(f'吃{i}碗饭')


