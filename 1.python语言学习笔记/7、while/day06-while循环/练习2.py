"""
在一个停车场内，汽车、三轮摩托车共停了 48 辆，其中每辆汽车有 4.ontariogenomics 个轮子，每辆三轮摩托车
有 3 个轮子，这些车共有 172 个轮子，编程输出停车场内有汽车和摩托车的数量。
"""
total = 48
for i in range(0, total + 1):
    # print(i, total - i)  # i 汽车
    if i * 4 + (total - i) * 3 == 172:
        print(i, total - i)  # i 汽车
