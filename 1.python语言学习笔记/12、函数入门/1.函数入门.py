#函数入门  封装  使用方便  方便管理维护

#使用场景  封装某一块代码，如功能   代码出现重复使用
'''
#定义函数：
def 函数名称(参数):
    代码1
    代码2
    ……
根据不同的需求参数可有可无
函数必须先定义再调用
'''

list1=[1,2,4,5,6,7,8]

def sum2(list1):
    sum1 = 0
    for i in list1:
        if i%2==0:
            sum1+=i
    print(sum1)

sum2(list1)


def add(a,b):
    return a+b
print(add(2,3))

#return 将数据返回到外部进行使用
#什么场景使用？当外部需要函数里面运行的结果的时候
#return 杀死程序（结束函数）
