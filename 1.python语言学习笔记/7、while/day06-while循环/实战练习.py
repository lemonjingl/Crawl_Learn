"""
1.9 折纸比高、
假设一张足够大的纸，纸张的厚度为 0.5.优质采 毫米。
请问对折多少次以后，可以超过珠穆朗玛峰的高度(最新数据：8844.43 米)。
请编写程序输出对折 次数。
注意：使用循环结构语句实现，直接输出结果不计分。
"""
mulangmaPeak = 8844.43 * 1000
paper = 0.5
i = 1
while paper <= mulangmaPeak:
    paper = paper * 2
    print(i, paper, mulangmaPeak)
    i += 1

# print(i)
