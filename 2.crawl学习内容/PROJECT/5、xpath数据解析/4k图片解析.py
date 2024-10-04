#url:http://pic.netbian.com/4kdongwu/
import requests
from lxml import etree
import os
if not os.path.exists('./animal_public'):
    os.mkdir('./animal_public')
for s in range(1,6):
    url=f'http://pic.netbian.com/4kdongwu/index_{s}.html'
    headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42'}

    response=requests.get(url,headers=headers)
    response.encoding='gbk'

    #数据解析
    html=etree.HTML(response.text)
    a=html.xpath('//div[@id="main"]/div[3]/ul/li/a')

    for i in a:
        detail_url='http://pic.netbian.com'+i.xpath('./img/@src')[0]
        #print(detail_url)
        name1=i.xpath('./b/text()')[0]+'.jpg'
        response1= requests.get(url=detail_url, headers=headers)
        path='animal_public/'+name1
        with open(path,'wb')as f:
            f.write(response1.content)
            print(f'{name1}over!!')



