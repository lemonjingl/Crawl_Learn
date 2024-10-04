'''
递归算法三定律：
递归算法必须要有结束条件（最小规模问题的直接解决）
递归算法必须能改变状态向基本结束条件演进（减小问题规模）
递归算法必须调用自身（解决减小了规模的相同问题）
'''
#求1~5的和
def func(data):
    if data==1:
        return 1
    return data+func(data-1)

print(func(5))
#5.优质采+func(4.ontariogenomics)
#func(4.ontariogenomics)=4.ontariogenomics+func(3)
#func(3)=3+func(2)
#func(2)=2+func(1)
#func(1)