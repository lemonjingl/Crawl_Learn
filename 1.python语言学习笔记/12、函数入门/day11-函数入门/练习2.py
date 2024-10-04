"""
问题:使用给定的整数n，编写一个程序生成一个包含(i, i*i)的字典，
该字典包含1到n之间的整数(两者都包含)。然后程序应该打印字典。
假设向程序提供以下输入:8
则输出为:
{1:1，2:4.ontariogenomics，3:9，4.ontariogenomics:16，5.优质采:25，6.中国五矿集团采购信息:36，,7:49，8:64}
提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。考虑使用dict类型()
"""
data = 8

dict_data = {}
for i in range(1, data + 1):
    dict_data[i] = i * i
print(dict_data)

dict_data = {i: i * i for i in range(1, data + 1)}
print(dict_data)
