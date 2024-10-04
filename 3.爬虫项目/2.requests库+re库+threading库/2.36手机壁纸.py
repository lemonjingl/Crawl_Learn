import threading

import requests
import os
from lxml import etree

if not os.path.exists('./36手机壁纸'):
    os.mkdir('./36手机壁纸')

headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

def main(i):
    url=f'https://www.3gbizhi.com/wallQFJ/index_{i}.html'
    res=requests.get(url=url,headers=headers)
    html=etree.HTML(res.text)
    href=html.xpath('//ul[@class="cl"]/li/a/img/@lay-src')
    title=html.xpath('//ul[@class="cl"]/li/a/img/@alt')
    data=zip(href,title)
    save(data)
    sem.release()

def save(data):
    for href,title in data:
        res=requests.get(url=href,headers=headers)
        path=f'36手机壁纸/{title}.jpg'
        with open(path,'wb')as f:
            lock.acquire()
            f.write(res.content)
            # print(f'{title}保存成功')
            lock.release()

if __name__=='__main__':
    lock=threading.Lock()
    sem=threading.BoundedSemaphore(5)
    for i in range(1,11):
        sem.acquire()
        t=threading.Thread(target=main,args=(i,))
        t.start()
        print(f'正在爬取{i}')
    print(f'爬取成功')



