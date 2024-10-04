import requests

from requests import Session

url='https://passport.17k.com/ck/user/login'
headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'}
data={'loginName': '18078418293',
'password': 'lzz18777392734'}
session=Session()
response=session.post(url,data=data,headers=headers)
print(response.text)

url1='https://user.17k.com/www/'
response1=session.get(url=url1,headers=headers)
print(response1.text)