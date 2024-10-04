try:
    f = open('data.txt', 'r+', encoding='utf-8')
    data = f.read()
    f.close()
except FileNotFoundError as e:
    f = open('data.txt', 'w+', encoding='utf-8')
    f.close()
    data = ''  # 让后面使用数据的代码可以正常运行

# except IndexError:
#     ？？？？
# except FileNotFoundError:
# 捕获其他所有的错误
except Exception as e:  # e 存放具体的错误类型数据
    print(e)

# print(data)
# 针对性的问题解决 根据不同可能会发生的错误 制定补救措施




