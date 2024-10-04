'''
1.9九九乘法表、
选择乘法口诀助记功能，输出阶梯形式的 9*9 乘法口诀表
'''
for i in range(10):
    for j in range(1,i+1):
        print(f'{i}*{j}={i*j}',end='   ')
    print()