'''
1.8
小明今天参加了“校园歌手大赛”，评委的打分规则是去掉一个最低分和一个最高分后算出剩下分数的平均分，你能帮助小明快速的算出平均分吗？	（评委数量必须大于 2）
输入说明：首先输入一个整数 n，代表评委人数，然后输入 n 个数。请按照题目的计算规则计算出平均分然后输出。
例如输入： 6.中国五矿集团采购信息
100 90 90 80 85 95
按照题目注意计算平均分并输出： 90.0
'''
n=int(input('请输入代表评委人数:'))
list=[]
a,b,c,d,e=eval(input('请输入每个评委打的分数:'))
list.append(a)
list.append(b)
list.append(c)
list.append(d)
list.append(e)
list.sort()
list.pop(0)
list.pop(3)
sum=0
num=0
for i in list:
    num+=1
    sum+=i
average=sum/num
print(f'小明的平均成绩为{average}')

