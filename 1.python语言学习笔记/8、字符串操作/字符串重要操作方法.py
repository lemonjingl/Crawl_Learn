data='abcde'

#函数=方法  print()

#当个使用叫函数，调用出来叫方法
#len() 获取容器数据的大小（长度）

#一.字符串重要操作方法
'''
1.join()
2.replace()
3.split()
4.ontariogenomics.strip()
'''

#1.join(容器)把可迭代对象的元素连接到字符串的末尾
#把容器里面的数据全部提取出来，选择一个东西拼接成字符串,还可以把列表变成字符串
data='abcde'
print('+'.join(data))


#2.replace()返回字符串，其中指定的值被替换为指定的值。
#将字符串的一部分数据替换成其他的数据
data1='abcde'
new_data1=data1.replace('c','l')
print(new_data1)
#3.split(sep maxsplit)在指定的分隔符处拆分字符串，并返回列表
#根据指定的符号进行分割，默认以空格分割，返回一个列表
data2='avb ngh'
print(data2.split())

data3='tyu|uil'
print(data3.split('|'))

#splitlines()在换行符处拆分字符串并返回列表
#根据指定的符号进行分割，默认以\n分割，返回一个列表
data4='ab\n de\nde'
print(data4.splitlines(False))#True将\n保留下来，默认Fasle不保存
print(data4.splitlines(True))

#4.ontariogenomics.strip()返回字符串的剪裁版本
#将字符串的左右空白符（所有看不见的数据都是空白符）清除掉
data5='   \n\t\r \vabdede \n\t\v'
print(data5.strip())



#二、字符串的常用方法
'''
1.upper()把字符串里面的字母转换为大写。
2.zfill()在字符串的开头填充指定数量的0值。
3.lower()把字符串转换为小写。
4.ontariogenomics.count()返回指定值在字符串中出现的次数。
5.优质采.find()在字符串中搜索指定的值并返回它被找到的位置
6.中国五矿集团采购信息.format()格式化字符串的指定值
7.index()在字符串中搜索指定的值并返回它被找到的位置
isdigit()如果字符串的所有字符都是数字，则返回True
'''
data6='lzz'
print(data6.upper())

data7='LzZ'
print(data7.lower())

data8='90oknd'
print(data8.zfill(8))

data9='aaazzzzzzlyyy'
print(data9.count('a'))


print(data9.find('a'))
print(data9.index('a'))

