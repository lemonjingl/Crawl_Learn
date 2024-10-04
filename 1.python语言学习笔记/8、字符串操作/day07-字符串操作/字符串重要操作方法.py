# data = 'abcde'

# 函数 = 方法  print()

# 当个使用叫函数 调用出来叫方法
# len() 获取容器数据的大小(长度)
# print(len(data))
# print(data.__len__())




# join(容器)	把可迭代对象的元素连接到字符串的末尾。
# 把容器里面的数据全部提取出来 ，选择一个东西拼接成字符串
# data = 'abcde'
# print('+'.join(data))
# a-b-c-d-e

# replace()	返回字符串，其中指定的值被替换为指定的值。
# 将字符串的一部分数据替换成其他的数据
# data = 'abccde'
# new_data = data.replace('cc', '')
# print(new_data)

# data = 'abcccccde'
# new_data = data.replace('c', '1', 2)
# print(new_data)

# split(sep maxsplit)	在指定的分隔符处拆分字符串，并返回列表。
# 根据指定的符号进行分割，默认以空格分割，返回一个列表
# data = 'ab de'
# print(data.split())

# data = 'ab1de1de'
# print(data.split('1', 1))


# splitlines()	在换行符处拆分字符串并返回列表。
# 根据指定的符号进行分割，默认以\n分割，返回一个列表
# data = 'ab\n de\nde'
# print(data.splitlines(False))
# splitlines(True) 将\n保留下来  默认Fasle不保存

# strip()	返回字符串的剪裁版本。
# 将字符串的左右空白符(所有看不见的数据都是空白符)清除掉
# data = '    \n\t\r\vabdede    \n\t\r\v'
# print(data.strip())


# 索引 切片
# join()	把可迭代对象的元素连接到字符串的末尾。
# replace()	返回字符串，其中指定的值被替换为指定的值。
# split()	在指定的分隔符处拆分字符串，并返回列表。
