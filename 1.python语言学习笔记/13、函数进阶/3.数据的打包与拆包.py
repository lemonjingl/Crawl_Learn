#打包元组
data=1,2,3,4
print(data)
print(type(data))

def func():
    return 1,2,3,4
data1=func()
print(data1)


#拆包
data3=(1,2,3)
a,b,c=data3

data4=[1,2,3,4,5]
d,e,f,g,h=data4
print(a,h)

# 拆包的场景使用
list_data = [['小明', 20], ['小刚', 22], ['小芳', 18]]
for i in list_data:
    print(i[0], i[1])

for name, age in list_data:
    print(name, age)

#所有的数据类型都能转换成字符串类型
