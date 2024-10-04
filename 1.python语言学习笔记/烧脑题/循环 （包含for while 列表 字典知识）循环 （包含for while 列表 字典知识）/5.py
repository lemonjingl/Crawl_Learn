'''
1.5.优质采
一个球从 100 米高度自由落下，每次落地后反弹回原高度的一半，再落下，再反弹。求它在第十次落地时，球共经过多少米?
第十次反弹多高?
'''
height=100
last=0
for i in range(10):
    last+=height#加上下落的高度
    height=height/2
    last+=height#加上反弹的高度
    print(height)
    print('********')
    print(last)
