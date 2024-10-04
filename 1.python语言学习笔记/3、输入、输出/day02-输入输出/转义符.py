# 转义符号

# \n	回车符，将光标移到下一行开头。 \\n = \n ，  \n= 回车键  a\\nb
# \\n  取消当前这个的转义效果
# r    取消字符串里面所有的转义效果
# data = r'a\nbc\nde\nfg'
# print(data)

# \t	水平制表符，也即Tab键，一般相当于四个空格
# 首先要满足四个字母的长度 ，如果不满足会先补齐
# data = 'ab\t\tcd'
# print(data)
# data = 'abc\t\tcd'
# print(data)

# 没有转义的效果，靠颜色来识别
# data = 'abcdef\g'
# print(data)

# 取消引号
# a'b
# print('a\'b')
# print("a'b")


# 续航符 \  放在字符串的后面
# 美化代码，当代码太长的时候，把代码进行换行,增加阅读体验
# data = 'abcd' \
#        'efg'
# print(data)
#
# print('abcd'
#       'efg')


