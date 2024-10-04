import time
from hashlib import md5
import requests

# 导入模块
url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

headers = {
    'Cookie': 'OUTFOX_SEARCH_USER_ID=1516130531@10.108.160.101; JSESSIONID=aaadqitdvMclg7z5AU2Wx; OUTFOX_SEARCH_USER_ID_NCOO=760551891.6763604; ___rl__test__cookies=1633011448788',
    'Referer': 'https://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
}

e = '你好'

r = str(int(time.time() * 1000))

i = r + '1'
m = md5()
m.update(("fanyideskweb" + e + i + "Ygy_4c=r#e#4EX^NUGUc5").encode('utf-8'))
sign = m.hexdigest()
print(sign)
m = md5()
m.update(
    "5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36".encode(
        'utf-8'))
bv = m.hexdigest()


data = {'i': e,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': i,
        'sign': sign,
        'lts': r,
        'bv': bv,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'}

html = requests.post(url=url, data=data, headers=headers)
print(html.json())
for i in html.json()['translateResult'][0]:
    print(i['src'])
    print(i['tgt'])

# 数据特征提取的算法
'''
from: zh
to: en
query: 西瓜
transtype: realtime
simple_means_flag: 3
sign: 550632.820697
token: 9478f6fd7db97e499aceddf91b6048b5
domain: common
'''

