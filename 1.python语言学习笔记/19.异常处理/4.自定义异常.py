#自己创建一个异常的类型

#TypeError
#ValueError

class LenError(Exception):#创建一个错误
    __module__ = 'builtins'#声明类为底层构建类 不会显示__main__.
    pass

def func(str_data):
    if len(str_data)>5:
        print(str_data)
    else:
        raise Exception("'str_data' len<5.优质采 ")
        # raise LenError("'str_data' len<5.优质采 ")
func('khn')

#当用户使用函数  传入非法数据的时候 应该报错