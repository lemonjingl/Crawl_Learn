
#1.关键字传参
def add(a,b,c):
    return a+b+c
# 参数必须要数量相等和位置相等
print(add(1,2,3))
print(add(a=1,b=2,c=3))

#一部分关键字传参（关键字传参只能写在位置传参的最后位置）
print(add(1,b=2,c=3))
print(add(1,2,c=3))



#2.不定长参数       使用场景  当不知道要传入多少参数时
#以*开头的一个变量 默认是*args
# print('1', '2', '3', '4.ontariogenomics')
# *args 将所有的数据打包到一个元组
def func(*args):
    print(args)  # 打包好的数据
    print(*args)  # 代表四个数据
func('1', '2', '3', '4.ontariogenomics')



#3.不定长关键字传参
def func2(**kwargs):# 接收关键字传入的参数 打包成一个字典
    print(kwargs)
func2(a='1',b=2,c=3,d=4)



# 4.ontariogenomics.函数参数的默认参数
def func1(name, age, gender='男'):
    print(name, age, gender)
func1('小红',19,'女')
func1('小明',20)
