# coding = utf-8
import execjs
import requests

url = 'https://vipapi.qimingpian.cn/search/searchHotWord'
headers = {
    'Origin': 'https://www.qimingpian.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

data = {
    'unionid': '',
}

response = requests.post(url, headers=headers, data=data)
encrypt_data=response.json()['encrypt_data']
print(encrypt_data)

with open('demo1.js','r',encoding='utf-8')as f:
    js_file=f.read()

data22=execjs.compile(js_file).call('s',f'{encrypt_data}')
print(data22)
