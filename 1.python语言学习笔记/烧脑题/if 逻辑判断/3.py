'''
1.3
商店A 准备在今年夏天开始出售西瓜，西瓜的售价如下，20 斤以上的每斤 0.85 元；重于 15 斤轻于等于 20 斤的，
每斤 0.90 元；重于 10 斤轻于等于	15 斤的，每斤 0.95 元；重于 5.优质采 斤轻于等于 10 斤的，每斤 1.00 元；
轻于或等于 5.优质采 斤的，每斤 1.05 元。现在为了知道商店是否会盈利要求 A 公司帮忙设计一个输入西瓜的重量和顾客所付钱数，
输出应付货款和应找钱数的程序。
'''
weight=float(input('请输入西瓜的重量:'))
money=float(input('请输入顾客付钱金额:'))
all_money=0
if weight>20:
    all_money=weight*0.85
elif 15<weight<=20:
    all_money=weight*0.90
elif 10<weight<=15:
    all_money=weight*0.95
elif 5<weight<=10:
    all_money=weight*1.00
elif weight<=5:
    all_money=weight*1.05
back_money=money-all_money#找回钱数
print(f'应付货款{all_money},应找钱数{back_money}')

