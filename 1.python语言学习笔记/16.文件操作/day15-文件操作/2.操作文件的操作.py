#文件夹操作  创建  重命名 删除
#1.创建
import os
if not os.path.exists('./data_file'):
    os.mkdir('./data_file')#不能执行多层级创建
os.makedirs('data_file1')#多重文件夹 创建嵌套的多个文件夹

#2.修改文件名称
os.rename('data_file1','data')

#3.删除文件夹
os.rmdir('data')
