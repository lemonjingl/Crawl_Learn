data = None
for i in range(10):  # for-else 找容器是否存在某个数据
    print(i)
    if i == 5:
        print('找到数据了')
        data = i
        break

else:  # else 当代码正常退出的时候执行 一般配合break使用
    print('没有找到数据了')

print(data)