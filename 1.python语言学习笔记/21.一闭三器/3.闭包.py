# 什么是一个闭包？

# 函数的嵌套
# 保证数据的安全 同时函数不会死亡 函数里面的数据属于局部变量，外部无法使用

def outer():
    list_data = []

    def inner():
        list_data.append(1)
        return list_data

    return inner  # inner() None /  inner


inner = outer()  # outer() == inner
print(inner())
print(inner())

# outer()()

# 当外部需要使用到函数里面的数据

# 不希望这个数据直接被使用
# 调用函数修改列表 而不是直接调用列表进行修改
