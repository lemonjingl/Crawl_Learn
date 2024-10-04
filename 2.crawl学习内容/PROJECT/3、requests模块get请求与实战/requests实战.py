import requests
url='https://movie.douban.com/'
header={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'}
response=requests.get(url=url,headers=header)
print(response.status_code)
if response.status_code==200:
    print('访问成功')
else:
    print('访问失败')
#response.content #转换字节流
html=response.text
with open('data.html','w',encoding='utf-8')as f:
    f.write(html)