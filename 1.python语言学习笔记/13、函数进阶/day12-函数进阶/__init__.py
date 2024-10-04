# print('同学们晚上好啊！')
my_money = 1000


def add(money):
    global my_money
    my_money += money
    print(f'我的余额为{my_money}')


def bdd(money):
    global my_money
    my_money -= money
    print(f'我的余额为{my_money}')


add(500)
add(5000)
bdd(5000)

