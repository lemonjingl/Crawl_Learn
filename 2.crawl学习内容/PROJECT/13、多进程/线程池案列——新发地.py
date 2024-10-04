from queue import Queue
import requests
import csv
import time
from concurrent.futures import ThreadPoolExecutor

q=Queue(30)
f=open('data1.csv','w',newline="",encoding='gbk')
writer1=csv.writer(f)
head=['id', 'prodName', 'prodCatid', 'prodCat', 'prodPcatid', 'prodPcat', 'lowPrice', 'highPrice', 'avgPrice', 'place', 'specInfo', 'unitInfo', 'pubDate', 'status','userIdCreate', 'userIdModified', 'userCreate', 'userModified', 'gmtCreate', 'gmtModified']
writer1.writerow(head)
def get_data(data):
    url='http://www.xinfadi.com.cn/getPriceData.html'
    headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55'}
    res=requests.post(url=url,data=data,headers=headers)
    for i in res.json()['list']:
        q.put(list(dict(i).values()))

def save_csv():
    while True:
        try:
            data=q.get(timeout=3)
            print(f'目前队列数量为{q.qsize()}')
            writer1.writerow(data)
        except:
            f.close()
            break
start=time.time()
pool=ThreadPoolExecutor(10)
for i in range(1,101):
    url_list=[{'limit': '20','current': f'{i}'}]
    for data in url_list:
        pool.submit(get_data,data)

pool1=ThreadPoolExecutor(15)
pool1.submit(save_csv)
pool1.shutdown()
pool.shutdown()
stop=time.time()
print(stop-start)
