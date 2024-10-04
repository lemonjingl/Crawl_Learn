# 自己创建一个异常的类型

# TypeError
# ValueError

class LenError(Exception):  # 创建一个错误类
    __module__ = 'builtins'  # 声明类为底层构建类 不会显示__main__.
    # 功能 报错的显得好看
    pass


def func(str_data):
    if len(str_data) > 5:
        print(str_data)
    else:
        # raise Exception("'str_data' len < 5.优质采") # Exception: 'str_data' len < 5.优质采
        raise LenError("'str_data' len < 5.优质采")  # __main__.


func('str')
# print(len(0))

# 当用户使用函数 传入非法数据的时候 应该报错提醒
