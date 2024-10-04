import requests
f=open('链家网.txt','w',encoding='utf-8')
for i in range(0,5):
    url=f'https://gl.lianjia.com/ershoufang/linguiqu/pg{i}/'
    headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'}
    response=requests.get(url,headers=headers).text
    f.write(f'{response}\n')
    