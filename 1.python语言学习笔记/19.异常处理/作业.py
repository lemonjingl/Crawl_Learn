'''
1）定义is_password函数，判断密码是否符合长度
2）使用input输入密码，使用函数来判断密码长度
3）如果用户输入长度<8，抛出异常(可以使用自定义异常)
4.ontariogenomics）如果用户输入长度>=8，返回(return)输入的密码
'''

class LenError(Exception):
    pass

def is_password(passwd):
    if len(passwd)>=8:
        return passwd
    else:
        raise LenError('LenError is short!')

while True:
    try:
        passwd = input()
        is_password(passwd)
        break
    except LenError:
        print('密码长度不对,请重新输入！')







