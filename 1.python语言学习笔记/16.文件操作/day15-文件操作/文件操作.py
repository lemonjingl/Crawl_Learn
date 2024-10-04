# 1生成文件 打开文件并且进行操作
# 2读取文件 更新内容
# 3保存数据 关闭文件

# open  确认文件所在的位置
# open('data.txt')

# 打开一个文件 需要确认文件的位置
# 文件位置 绝对路径(位置的路径) 相对路径(当前文件操作路径)
# 绝对路径 'F:\pythonProject2208\day15-文件操作\data.txt'

# open(r'F:\pythonProject2208\day15-文件操作\data.txt')
# 相对路径 'data.txt'
# open(r'data\data.txt')

# 绝对路径 'F:\pythonProject2208\day15-文件操作\data\data.txt'
# 相对路径 'data\data.txt'

# 绝对路径 'F:\pythonProject2208\day14-高阶函数\递归.py'
# 相对路径 '../day14-高阶函数\递归.py'
# open(r'../day14-高阶函数\__init__.py')


# 打开操作文件 确认作的模式 r读取  w写  a追加  +让一个模式同时具体读写功能

# 使用r模式 读取的文件必须存在 否则就会报错 --》找不到文件错误
# f = open('data.txt', 'r+')  # 以读的方式打开文件
# txt_data = f.read()  # f.read() 读取所有内容  f.read(3) 读取指定长度的内容
# f.write('1')

# f.seek(0)  # 将光标移动到最前面  seek(0) 0 是光标的索引位置
# print(f.read())

# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline()) # 读取空的数据
# 读取一行数据

# 把所有行的数据存放到列表
# print(f.readlines())

# f.close()  # 如果不写关闭 数据依然存在内存里面 不会更新到文件中
# print(txt_data)

# w  写数据 如果文件不存在 就会创建文件
# 覆盖原先的文件内容（当open的时候会自动删除文件里面的所有内容）

# f = open('data.txt', 'w')
# f.write('id = 1')  # 写入一个数据
# f.writelines(['id=1\n', 'id=2\n'])  # 同时写入多个数据
# f.close()

# a 追加写 在原有数据的基础上的后面添加数据
# 如果文件不存在就创建文件 操作文件的时候光标在最后 a 不会删除原先的数据
# f = open('data.txt', 'a')
# f.write('id = 1\n')  # 写入一个数据
# f.writelines(['id=1\n', 'id=2\n'])  # 同时写入多个数据
# f.close()


# 编码  以什么编码读取 就要以什么编码打开 utf-8 gbk gb2312
# f = open('data_test.txt', 'w', encoding='utf-8')
# f.write('utf-8 gbk gb2312')
# f.close()
#
# f = open('data_test.txt', 'r', encoding='utf-8')
# print(f.read())
# f.close()


