import requests
import re
url='https://movie.douban.com/top250'
headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42'}

response=requests.get(url,headers=headers)

name=re.findall(r'<li>.*?<div class="item">.*?<span class="title">(.*?)</span>',response.text,re.S)
direct=re.findall(r'<li>.*?<div class="bd">.*?导演:(.*?);&nbsp',response.text,re.S)
year=re.findall(r'<li>.*?<div class="bd">.*?<br>(.*?)&nbsp',response.text,re.S)
score=re.findall(r'<div class="star">.*?<span>(.*?)</span>',response.text,re.S)
data=zip(name,direct,year,score)
print(f'{name},{direct},{year},{score}'+'\n')
