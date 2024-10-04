'''
1、创建一个data.txt的文件
2、用文件的写的方法往里面写上一首诗，并输出里面的全部内容

静夜思
唐代：李白
床前明月光，疑是地上霜。
举头望明月，低头思故乡。

3、删除最后一行的诗句后并输出删除后的内容
'''

with open('data.txt','w+',encoding='utf-8')as f:
    data=['静夜思','唐代：李白','床前明月光，疑是地上霜。','举头望明月，低头思故乡。']
    for i in data:
        f.write(i+'\n')
    f.seek(0)
    a=f.readlines()
    print(f'被删除的内容为:  {a.pop()}')

