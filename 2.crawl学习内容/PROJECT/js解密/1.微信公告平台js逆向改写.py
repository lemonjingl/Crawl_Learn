import requests
import  execjs

url='https://mp.weixin.qq.com/cgi-bin/bizlogin?'
headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

f=open('wecat.js','r',encoding='utf-8')
js_data=f.read()
f.close()

js_code=execjs.compile(js_data)
username=input('请输入你的账号：')
pwd=input('请输入你的密码：')
passwd=js_code.call('getpasswd',pwd)

data={'username': username,
'pwd': passwd,
'f': 'json',
'userlang': 'zh_CN',
'lang': 'zh_CN',
'ajax': '1'
}

response=requests.post(url=url,data=data,headers=headers)
print(response.json())
