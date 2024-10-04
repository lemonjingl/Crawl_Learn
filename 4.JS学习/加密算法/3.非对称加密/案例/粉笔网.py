import requests
import execjs

url = 'https://login.fenbi.com/api/users/loginV2'


headers = {
    'origin': 'https://www.fenbi.com',
    'referer': 'https://www.fenbi.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}
phone=input('请输入你的账号：')
pwd=input('请输入你的密码：')
with open('./粉笔网.js','r',encoding='utf-8')as f:
    js_file=f.read()
pwd=execjs.compile(js_file).call('pwd',pwd)
print(pwd)
data = {
    'kav': '100',
    'app': 'web',
    'av': '100',
    'hav': '100',
    'client_context_id': '065930afa5c439efe0d32353d154f176',
    'password': f'{pwd}',
    'persistent': 'true',
    'phone': f'{phone}',
}

response = requests.post(url, headers=headers, data=data)
print(response.text)
