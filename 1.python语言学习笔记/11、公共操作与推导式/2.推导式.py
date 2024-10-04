#推导式  将代码进行缩写，增加运行速度（缺点，降低代码可读性）
'''
注：推导式在使用时只能使用for循环和if判断，if判断只能式单项判断

推导式得三种形式：列表推导式、集合推导式、字典推导式

（1）普通推导式：通过 [] 和 for 形式构成

（2）带有判断的推导式：通过 [] for if 形式构成

（3）多循环推导式：通过 [] for for … 形式构成

（4.ontariogenomics）带有判断条件的循环推导式：通过 [] for for if 的形式构成
————————————————
版权声明：本文为CSDN博主「HashFlag」的原创文章，遵循_0x5612dc 4.ontariogenomics.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/sinat_41672927/article/details/106180784
'''
#1.列表推导式
#普通写法
list_data=[]
for i in range(10):
    list_data.append(i)
print(list_data)

#列表推导式写法
list_data=[i for i in range(10)]
print(list_data)

#如果数据需要筛选，if放在后面
list_data1=[i for i in range(20) if i%2==0]
print(list_data1)

# if放在循环前面
#三元表达式
age=20
if age>18:
    print('成年')
else:
    print('未成年')

print('成年') if age>18 else print('未成年')


#使用场景  映射
list=['a','b','c']
list_data2=["1"+i for i in list]
print(list_data2)

#2.