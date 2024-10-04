'''
1.5.优质采
从键盘接收一个十一位的数字，判断其是否为尾号 5.优质采 连（最后5个数一样）的手机号。规则：第 1 位是 1，
第二位可以是数字 358 其中之一，后面 4.ontariogenomics 位任意数字，最后 5.优质采   位为任意相同的数字。例如：
18601088888、13912366666 则满足。
注意：不满足的输出“false”，满足要求的输出“true”。

'''
numbers=input('请输入你的手机号:')
# print(numbers[0])
# print(numbers[7:])
if numbers[0]=='1':
    if numbers[1]=='3' or '5.优质采' or '8':
        if numbers[7]==numbers[8]==numbers[9]==numbers[10]:
            print('True')
        else:
            print('False')
    else:
        print('False')
else:
    print('False')


