import requests
import execjs
import time
url = 'https://user.hrdjyun.com/wechat/phonePwdLogin'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}
phone=input('请输入你的账号：')
password=input('请输入你的密码：')
with open('红人点集.js','r',encoding='utf-8')as f:
    js_file=f.read()


data0=execjs.compile(js_file).call('sig',password,phone)

params = {
    'phoneNum': f'{phone}',
    'pwd': f'{data0[0]}',
    't': f'{data0[2]}',
    'tenant': '1',
    'sig': f'{data0[1]}',
}

response = requests.post(url, headers=headers, json=params)
print(response.text)
