import threading

import requests
from lxml import etree
import csv
import re

lock=threading.Lock()

headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
def run(index):
    url=f'https://ac.qq.com/Comic/index/page/{index}'
    res=requests.get(url=url,headers=headers)
    html1=res.text
    parse(html1)

    # 释放线程
    sem.release()

def parse(html1):
    html=etree.HTML(html1)
    title = html.xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li/div[2]/h3/a/@title')
    author = html.xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li/div[2]/p[1]/@title')
    type = re.findall(
        '<span href="/Comic/all/theme/.*?" target="_blank">(.*?)</span>.*?<span href="/Comic/all/theme/.*?" target="_blank">(.*?)</span>',
        html1, re.S)
    popularity = html.xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li/div[2]/p[2]/span[3]/em/text()')
    data = zip(title, author, type, popularity)

    csv_file = open('./漫画数据2.csv', 'a+', encoding='GB18030', newline='')
    writer = csv.writer(csv_file)

    # 保证只写入一次表头
    global  flag
    if flag:
        writer.writerow(['书名', '作者', '类型', '人气'])
        flag=False

    for title, author, type, popularity in data:
        type1 = type[0] + '/' + type[1]

        # 锁上
        lock.acquire()
        writer.writerow([title, author, type1, popularity])
        # print(f'{title}保存完成')
        # 关闭

        lock.release()
    csv_file.close()



if __name__=='__main__':
    flag=True
    sem=threading.BoundedSemaphore(5)
    sem_list=[]
    for index in range(1,101):
        sem.acquire()
        t=threading.Thread(target=run,args=(index,))
        t.start()
        sem_list.append(t)
        print(f'正在爬取{index}')
    for rt in sem_list:
        rt.join()
    print('数据爬取完毕')

