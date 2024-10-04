name='小明'
money=10

#1、format 不同的数据类型也可以进行格式化
print('今天{}迟到了，扣款{}元'.format(name,money))

#2、% 格式化
print('今天%s迟到了，扣款%s元'%(name,money))

#3、f 格式化 是format格式化的简化版本
print(f'今天{name}迟到了，扣款{money}元')

