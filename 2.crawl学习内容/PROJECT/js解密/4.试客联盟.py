import requests
import execjs

url='http://login.shikee.com/check/?&_1676619703283'
headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

response=requests.post(url=url,headers=headers)
print(response.text)