# 找到错误

# import requests
# def aaa():
#     requests.get('')
# aaa()

# 如何快速找到报错的代码部分
# 从下往上找 找到自己认识的文件 确认报错的代码

# 分析问题 为什么报错 因为什么报错？
# 在异常类型的提示信息里面 解决问题
# 翻译一下中文 如果还是无法解决进行百度


# 异常处理

# 使用场景 作用
# 本身的代码是很少出现报错的情况
# 异常处理只能够用于可能会发生错误的代码

# print('1' + 1)

# 异常处理针对不稳定的数据 人为的输入数据 读取外部的数据或者文件
# for i in range(3):
#     try:
#         data = input('请输入一个整数:')
#         print(50-int(data))
#         break  # 当代码正常运行就跳出循环
#     except:
#         print('你输入的数据不符合规范')
# else:
#     print('你所有的次数已经使用完')

# 万一外部的数据就是你不希望它传入的数据

# 找到可能会发生错误的部分

# 补救措施
# try:
#     f = open('data.txt', 'r+', encoding='utf-8')
#     data = f.read()
#     f.close()
# except:
#     f = open('data.txt', 'w+', encoding='utf-8')
#     f.close()
#     data = ''  # 让后面使用数据的代码可以正常运行
#
# print(data)
