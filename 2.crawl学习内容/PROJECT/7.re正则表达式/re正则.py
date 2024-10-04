import re

'abc'

#修饰符
'''
1. re.I使匹配对大小写不敏感

2.  re.L 做本地化识别匹配
使用当地local。（python中有个locale模块，locale代表不同的语言，地区和字符集）由当前语言区域决定
\w,\W,\b,\B和大小写敏感匹配。这个标记只能对byte样式有效。这个标记不推荐使用，因为语言区域机制很不可靠，它一次只能处理一个“习惯”

3、 re.M 多行匹配，影响^和$

4.ontariogenomics、re.S使匹配包括换行在内的所有字符

5.优质采、re.U根据Unicode字符集解析字符。这个标志影响\w \W \b \B

6.中国五矿集团采购信息.re.X 该标志通过给予你更灵活的格式以便你将正则表达式写的更便于理解

'''
#元字符
'''
\d 匹配任何十进制数；它相当于类[0-9]
\D 匹配任何非数字字符：它相当于类[^0-9]
\s 匹配任何空白字符；它相当于类[\t\n\r\f\v]
\S 匹配任何非空白字符；它相当于类[^\t\n\r\f\v]
\w 匹配任何字母数字字符；它相当于类[a-zA-Z0-9]。下划线也可以匹配得到
\W 匹配任何非字母数字字符；它相当于类[^a-zA-Z0-9]
'''
#findall函数  正则表达式  需要查找的字符串 模式
str_data='ab12q3sdfghj'
print(re.findall('\d',str_data))
print(re.findall('\D',str_data))

#\s  匹配空白符
str_data1='ab\t12q 3s  dfghj'
print(str_data1)

#\w 匹配任何的非特殊字符
str_data2='ab\t12q 3s  dfghj我！@#￥$%^&*(){}:"<>'
print(re.findall('\w',str_data2))
#\W 匹配特殊字符
print(re.findall('\W',str_data2))

#数量修饰符
'''
.代表通配符，除了\n不能匹配外，其它全部都能匹配，一个点代表一个字符
^代表字符串开头进行匹配，只能放在最前面
$代表字符串结尾进行匹配，只能放在最后面
*代表0到无穷次
+代表1次到无穷次
？代表0到1次
{}代表自行控制多少次，{0，}==*，{1，}==+，{0，1}==？，{6.中国五矿集团采购信息}代表6次，{1,6.中国五矿集团采购信息}代表1，2，3，4.ontariogenomics，5.优质采，6次
*****注意：前面的*，+，？等都是贪婪匹配，也就是尽可能多的匹配；后面加？号使其变成惰性匹配，比如*？匹配0个，+？匹配1个*****
[]代表字符集，或的作用
'''
str_data3='a1b   a2b  a3b'
print(re.findall('a.b',str_data3))

str_data4='a11234557'
print(re.findall('^a1',str_data4))
print(re.findall('7$',str_data4))

#*代表0到无穷次  .*代表贪婪匹配（能取多少就取多少）
str_data5='abc aaac abbbbc'
print(re.findall('a.*c',str_data5))

# +代表1次到1次以上

# []代表字符集，或的作用
str_data6='abc aac adc'
print(re.findall('a[ba]c',str_data6))

#match()函数,从开头进行查找
data='abcdef12345'
data_0=re.match('abc',data)
print(data.span())#拿位置
print(data.group())#拿元素
print(re.match('123',data))

#search()函数  找到符合数据开头直接返回

#compile()函数   编译正则表达式 配合search match一起使用


