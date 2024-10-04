# 如何打包成exe的可执行文件 （打包后的文件在没有安装python的情况下也可以正常运行）

# pip install pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple


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


data = input('请输入一个长度大于5的密码:')
func(data)

# -F 打包成一个exe 优点是只有一个文件 缺是启动比较慢 适用于小代码代表
# -D 打包成一个文件夹 优点就是读取运行速度很快 缺点就是文件多 适用于大量代码打包

# 进入到需要打包的文件路径下输入以下命令进行打包
# pyinstaller -F 应用程序.py

# 如果说代码出现了问题 应该通过cmd窗口运行exe
# 直接双击运行 报错程序会自动关闭 程序运行完成也会自动关闭

# 首先进入路径需要先进入盘符 D:
# cd 路径

#
