import hashlib
import random
import time

import requests

# 导入模块
url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

headers = {
    'Cookie': 'OUTFOX_SEARCH_USER_ID=1516130531@10.108.160.101; JSESSIONID=aaadqitdvMclg7z5AU2Wx; OUTFOX_SEARCH_USER_ID_NCOO=760551891.6763604; ___rl__test__cookies=1633011448788',
    'Referer': 'https://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
}

e = '香蕉'

salt = str(int(time.time()) * 1000) + str(int(random.random() * 10))
ddc = "fanyideskweb" + str(e) + str(salt) + "Ygy_4c=r#e#4EX^NUGUc5"
hs = 'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'

data = {'i': e,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        "salt": salt,
        "sign": hashlib.md5(ddc.encode("utf-8")).hexdigest(),
        "lts": str(int(time.time() * 1000)),
        "bv": hashlib.md5(hs.encode("utf-8")).hexdigest(),
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'}

html = requests.post(url=url, data=data, headers=headers)
print(html.text)
for i in html.json()['translateResult'][0]:
    print(i['src'])
    print(i['tgt'])
