class LenghtError(Exception):
    pass


def is_password(password):  # 函数
    if len(password) >= 8:  # 密码长度是否小于8
        return password
    else:
        raise LenghtError('密码长度小于8')  # 抛出异常  异常的详细信息


while True:
    try:
        data = input('请输入一个密码:')
        print(is_password(data))
        break
    except LenghtError:
        print('你输入的密码小于8位，请重新输入')
