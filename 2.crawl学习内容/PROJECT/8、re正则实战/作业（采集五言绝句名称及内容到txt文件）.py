#url="https://so.gushiwen.cn"

import requests
import re
f=open('five words.txt', 'w', encoding='utf-8')
url='https://so.gushiwen.cn/gushi/tangshi.aspx'
headers = {
        'User-Agent': 'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42'}
response=requests.get(url,headers=headers)

#数据解析

#data 取块
data=re.findall(r'<div class="bookMl"><strong>五言绝句</strong></div>(.*?)</div>.*?<div class="bookMl"><strong>七言绝句</strong></div>',response.text,re.S)

obj=re.compile(r'<span><a href="(?P<detail>.*?)" target="_blank">'
               r'(?P<title>.*?)</a>(?P<author>.*?)</span>',re.S)
content=obj.finditer(str(data))

for i in content:
    detail_url='https://so.gushiwen.cn/'+i.group('detail')
    title=i.group('title')
    author=i.group('author')
    #print(f'{title}~{author}')
    response1 = requests.get(url=detail_url, headers=headers)

    data1=re.findall(r'<div class="contson" id="contson.*?">(.*?)<br />(.*?)</div>',response1.text,re.S)
    content=''.join(data1[0])
    #print(content)

    f.write(f'{title}~{author}{content}\n')
f.close()


