import requests
url='https://tieba.baidu.com/'+'kw'
headers={'User-Agent':''}

name=input("请输入你想搜的:")
kw={'kw':'name'}

#透明代理
#匿名代理

#proxies={'http':'http://+ip:端口'}

response=requests.get(url=url,params=kw,headers=headers)
print(response.text)
