import requests
import execjs
import re


url='https://passport.wanmei.com/sso/login?service=passport&isiframe=1&location=2f736166652f'
headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

response=requests.get(url=url,headers=headers)

key=re.findall(r'<input id="e" type="hidden" value="(.*?)" />',response.text)#获取公钥


pwd=input('请输入密码:')
#加密的逆向
f=open('wanmeishijie.js','r',encoding='utf-8')
exe_js=f.read()
f.close()
exe_data=execjs.compile(exe_js)
a=exe_data.call('getPasswd',pwd,key[0])

print(a)

