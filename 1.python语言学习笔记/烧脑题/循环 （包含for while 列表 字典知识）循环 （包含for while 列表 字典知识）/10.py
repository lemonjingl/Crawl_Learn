'''
1.10
输入一个字符串统计每个字符在字符串中出现的次数。
'''
str_data='bblzzhyylyylxl'
list=[]
for i in str_data:
    if i not in list:
        list.append(i)
for j in list:
    print(f'{j},在字符串中有{str_data.count(j)}次')

