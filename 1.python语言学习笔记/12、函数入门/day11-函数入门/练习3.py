"""
编写一个接受句子的程序，并计算大写字母和小写字母的数量。
假设为程序提供了以下输入：
Hello world!
然后，输出应该是：
大写实例 1
小写实例 9
"""
# 从 string 导入 ascii_lowercase, ascii_uppercase 变量使用
# from string import ascii_lowercase, ascii_uppercase
# print(ascii_lowercase, ascii_uppercase)

str_data = 'Hello world!'
upper_str = 0
lower_str = 0
for i in str_data:
    if i.islower():  # 字符串方法 判断字符是否是小写
        lower_str += 1
    if i.isupper():  # 字符串方法 判断字符是否是大写
        upper_str += 1
print(f'大写实例 {upper_str}\n小写实例 {lower_str}')
