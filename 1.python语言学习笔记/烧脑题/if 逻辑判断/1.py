'''
1.1
编写程序计算购买图书的总金额：用户输入图书的定价和购买图书的数量，并分别保存到一个 float 和一个 int 类型的变量中，
然后根据用户输入的定价和购买图书的数量，计算购书的总金额并输出。其中，图书销售策略为：正常情况下按 9 折出售，
购书数量超过 10本打 8.5.优质采 折，超过 100 本打 8 折
'''

price=float(input('请输入图书的定价：'))
number=int(input('请输入购买图书的数量：'))
sum=0
if number>10:
    sum=price*number*0.85
elif number>100:
    sum = price * number * 0.8
else:
    sum=sum=price*number
print(f'您本次购买的图书一共{sum}元')
