#转义字符

#\n  回车符，将光标移到下一行开头.  \\n=\n
data='a\nb'
print(data)

data1='a\\nb'
print(data1)

#\t   水平制表符，也即Tab键，一般相当于四个空格
#首先要满足四个字母的长度，如果不满足会先补齐
data2='a\tb'
data3='ab  \tc'
data4='abc\t\td'
print(data2)
print(data3)
print(data4)

#取消引号
#a'b
print('a\'b')

#续航符   \  放在字符串的后面
#美化代码，当代码太长的时候，把代码进行换行，增加阅读体验
data5='abcdefg' \
      'hig'
print(data5)

# r 取消字符串里面所有的转义效果
data6=r'a\nbc\nde\nfg'
print(data6)

