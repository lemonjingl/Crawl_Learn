import requests
from lxml import etree
import re
import threading

lock=threading.Lock()

def requests_get(i, headers):
    url=f'https://www.nyato.com/manzhan/?type=expired&p={i}'
    res = requests.get(url=url, headers=headers)

    html = etree.HTML(res.text)
    href = html.xpath('//ul[@class="w980 pt20"]/li/div[1]')  # 进入详情页的链接
    for url1 in href:
        src = url1.xpath('./a/@href')[0]
        detail_get(src)
    sem.release()

def detail_get(src):
    try:
        res1 = requests.get(url=src, headers=headers)
        # print(res1.text)
        html1 = etree.HTML(res1.text)
        title = html1.xpath('//div[@class="w100s"]/div[2]/h2/text()')[0]
        address = re.findall('<span class="fl mr10">(.*?)</span>', res1.text)[0]
        time = html1.xpath('//div[@class="w100s"]/div[2]/div[2]/text()')[1].strip('\n')
        price = html1.xpath('//div[@class="w100s"]/div[2]/div[3]/span[3]/text()')[0]
        save(title, address, time, price)
    except Exception as e:
        print(e)


def save(title, address, time, price):
    try:
        with open('./data.csv','a+',encoding='gbk')as f:
            lock.acquire()
            f.write(f'{title},{address},{time},{price}\n')
            # print(f'{title}写入成功')
            lock.release()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    headers = {'User-Agent': ''}
    sem=threading.BoundedSemaphore(3)
    for i in range(1,7):
        sem.acquire()
        print(f'正在爬取{i}')
        t=threading.Thread(target=requests_get,args=(i,headers))
        t.start()
    print(f'爬取完成!')