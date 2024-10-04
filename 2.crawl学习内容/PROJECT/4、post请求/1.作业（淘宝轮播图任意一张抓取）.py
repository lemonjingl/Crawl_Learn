import requests

url='https://img.alicdn.com/imgextra/i3/6000000007101/O1CN01nWlF6t22KJGhlYJoe_!!6000000007101-2-octopus.png'
headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'}
response=requests.get(url,headers=headers)

with open('img.jpg','wb+')as f:
    f.write(response.content)

