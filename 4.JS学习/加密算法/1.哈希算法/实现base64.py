# base64编码和解码

# 字符串编码和解码 ascii,utf-8,gbk

s='中文'.encode('utf-8')
s1='中文'.encode('gbk')
s2='abc'.encode()
print(s.decode())
print(s1.decode('gbk'))
print(s2)
print(s)


import base64

s_64=base64.b64encode(s)
s_64_decode=base64.b64decode(s_64)
print(s_64)
print(s_64_decode.decode())