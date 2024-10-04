try:
    f=open('data.txt','w+',encoding='utf-8')
    data=f.read()
    f.close()
except:
    f=open('data.txt','w+',encoding='utf-8')
    f.close()
    data=''#让后面使用数据的代码可以正常运行

else:#当没有发生错误的时候运行里面的内容
    print('真幸运代码没有问题')

finally: #在任何情况下都会运行代码 通常用于文件的关闭
    f.close()