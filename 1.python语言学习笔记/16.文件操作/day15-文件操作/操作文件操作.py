# print('同学们晚上好啊！')

# 操作文件的操作

# 文件夹操作 创建 重命名 删除
# 创建
# os.mkdir('data_file')  # 创建一个文件夹
# os.mkdir('data_file\data')  # 不能够执行多层级创建
# os.makedirs('data_file\data')  # 多重文件夹 创建嵌套的多个文件夹

# 修改文件名称
# os.rename('data_file\data', 'data_file\data_1')

# 删除文件夹
# os.rmdir('data_file\data_1')

# 文件操作 复制 删除 重命名

# 重命名
# os.rename('data1.txt', 'data_file.txt')

# 删除文件
# os.remove('data.txt')

#  复制
# 复制文件 同时还可以进行修改名称
# shutil.copy('data_file.txt','data_file\data_file1.txt')

# os 可以操作权限小一点
# shutil 系统操作模块 运行比较危险的操作


# 路径操作
# os.path.exists 判断文件 或者路径是否存在
# print(os.path.exists('data_test2.txt'))

# 路径的拼接
# print(os.path.join('c:\\aa', 'bb\\', '_0x5612dc.txt'))
# c = 'c:\\aa'+'\\bb\\'+'_0x5612dc.txt'

# 分割路径 将路径的最后一个分割出来
# print(os.path.split('c:\\aa\\bb\\_0x5612dc'))

# os.getcwd	获取当前路径
# print(os.getcwd())

# os.listdir	获取文件中的文件
# print(os.listdir('F:\pythonProject2208\day15-文件操作'))

# import os
#
# list1 = ['小明', '小红', '小芳']
# for i in list1:
#     os.mkdir(i)

# 文件 -> 创建文件
# 往里面写入数据{写入一首古诗词}
# 创建完成后进行修改 发挥自己的创意，修改最后一行的诗句
# 修改完成重新存储到文件


# f = open('data.txt', 'w+', encoding='utf-8')
# f.write('''诗名称
# 诗句1，诗句2.
# 诗句3，诗句4.
# ''')
# f.seek(0)  # 因为写入数据后光标在最后 这个时候读取不到内容
# txt_list = f.readlines()  # 读取里面的内容
# txt_list[-1] = '新的诗句3，新的诗句4.\n'  # 修改里面的内容
# f.close()
#
# f = open('data.txt', 'w+', encoding='utf-8')  # 将新的内容覆盖掉原先的内容
# f.writelines(txt_list)  # 将新的内容覆盖掉原先的内容
# f.close()
