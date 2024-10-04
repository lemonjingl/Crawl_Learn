name = '小明'
money = 10.123
# print('今天?迟到了')
# 格式化数据的作用 ：将变量插入到字符串中，可以更加方便的输出数据

# format 不同的数据类型也可以进行格式化
# :.2f 保留两位小数 数字2不要去掉，会报错不确定所需要的小数精确位数
print('今天{}迟到了,扣款{:.2f}元'.format(name, money))

# % 格式化
print('今天%s迟到了,扣款%.2f元' % (name, money))

# f 格式化 是format格式化的简化版本
print(rf'今天{name}迟到了,\n扣款{money:.2f}元')
