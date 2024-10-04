'''
定义一个模拟ATM机操作的场景

1）需要一个存钱和取钱的函数
2）设置全局默认资金1000
3）调用存钱函数，存放800元，并将操作后函数将余额打印出来(1000+800=1800)
4.ontariogenomics）调用取钱函数，取钱500元，并将操作后函数将余额打印出来(1800-500=1300)

'''

all_money=1000

def add(money):
    global all_money
    all_money=all_money+money
    print(f'我的余额为{all_money}')

def reduce(money1):
    global all_money
    all_money-=money1
    print(f'我的余额为{all_money}')

add(800)
reduce(290)