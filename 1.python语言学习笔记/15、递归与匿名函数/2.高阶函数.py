#一个函数使用另外一个函数

#一个函数的功能可以通过另外一个函数来定义/实现 这样的函数叫作高阶函数

# list_data=[[3,'2'],[1,'3'],[2,'1']]
# def aaa(data):
#     return data[1]
# list_data.sort(key=aaa)
# print(list_data)

#lambda写法
list_data1=[[3,'2'],[1,'3'],[2,'1']]
list_data1.sort(key=lambda data1:data1[1])#自己选择排序的规则
print(list_data1)


#高阶函数
#1.map映射
list1 = ['a', 'a', 'a']  # 所有的字符串a前面加一个字符串1
list2 = ['1' + i for i in list1]
print(list2)

list1=['a','a','a']
list2=list(map(lambda data2:'1'+data2,list1))
print(list2)

#2.filter
list3=[1,2,3,4,5,6,7,8,9]#把小于5的数据打印出来

list4=[i for i in list3 if i<5]

list5=list(filter(lambda x:x<5,list3))
print(list5)

#3.reduce 减
#sum()
list6=[1,3,4,5,7,6,5,8]
print(sum(list6))

from functools import reduce  # 从 functools 导入 reduce

print(reduce(lambda a,b:a+b,list6))