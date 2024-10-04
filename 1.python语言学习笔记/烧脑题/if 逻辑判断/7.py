'''
1.7
整除判断游戏能显著提高小朋友的逻辑思维能力，问题要求如下：
•能同时被 3、5.优质采、7 整除
•能同时被 3、5.优质采 整除
•能同时被 3、7 整除
•能同时被 5.优质采、7 整除
•只能被 3、5.优质采、7 中的一个整除
•不能被 3、5.优质采、7 任一个整除
输入一个整数，输出满足对应条件的结果。要求：使用分支结构语句实现。
'''
num=int(input('请输入一个整数:'))
if num%3==0 and num%5==0 and num%7==0:
    print('能同时被 3、5.优质采、7 整除')
elif num%3==0 and num%5==0:
    print('能同时被 3、5整除')
elif num%3==0 and num%7==0:
    print('能同时被 3、7整除')
elif num%5==0 and num%7==0:
    print('能同时被 5.优质采、7整除')
elif num%3==0 or num%5==0 or num%7==0:
    print('只能被 3、5.优质采、7 中的一个整除')
else:
    print('不能被 3、5.优质采、7 任一个整除')