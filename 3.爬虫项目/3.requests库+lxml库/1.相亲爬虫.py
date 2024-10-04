import requests
import time
import os
if not os.path.exists('./相亲'):
    os.mkdir('./相亲')

from lxml import etree

def save(src,title):
    try:
        res=requests.get(url=src)
        path=f'相亲/{title}.jpg'
        with open(path,'wb+')as f:
            f.write(res.content)
            print(f'{title}保存成功')
    except Exception as e:
        print(e)

def run(url):
    headers={'User-Agent':'',
             'Host': 'www.19lou.com',
             'Referer': 'https: // www.19lou.com / r / 1 / 19lnsxq.html',
             'Cookie': '_Z3nY0d4C_ = 37XgPK9h',
             }
    try:
        res=requests.get(url=url,headers=headers)

        #将html转换成ELement对象
        html=etree.HTML(res.text)
        #xpath路径提取@class为选取class属性
        divs=html.xpath('//div[@class="pics"]')
        #遍历Elements节点
        for div in divs:
            src=div.xpath('./img/@data-src')[0].replace('200x240','no')
            title=div.xpath('./img/@alt')[0]
            save(src,title)
    except Exception as e:
        print(e)

if __name__=='__main__':
    urls=['https://www.19lou.com/r/1/19lnsxq.html']
    for i in range(2,11):
        urls.append(f'https://www.19lou.com/r/1/19lnsxq-{i}.html')
    for url in urls:
        print(f'正在抓取{url}')
        run(url)
    print('全部抓取成功!')



# http://att3.citysbs.com/200x240/baomihua/2022/03/31/15/1200x1599-150929_v3_11331648710569477_d97cc4c199478e54147d952333ddf6a9.jpg
# http://att3.citysbs.com/no/baomihua/2022/03/31/15/1200x1599-150929_v3_11331648710569477_d97cc4c199478e54147d952333ddf6a9.jpg