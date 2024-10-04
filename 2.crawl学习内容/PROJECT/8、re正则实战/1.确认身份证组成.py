import requests
import re

str_data='45032220030214252X'# 0-9 x

data=re.findall('^\d{17}[\dX]$',str_data)
if data:
    print('是正确的身份证')
else:
    print('不是正确身份证格式')
