import requests
from fake_useragent import UserAgent
import os
import threading

ua=UserAgent()


def parse(page):
    try:
        url='https://api5.hanfugou.com/Feed/GetFeedList?'
        headers={'User-Agent':ua.chrome}
        data={
            'maxid': '4428352',
            'objecttype': 'trend',
            'count': 10,
            'page': f'{page}'
        }
        res=requests.get(url=url,params=data,headers=headers)
        # print(res.json()['Data'])
        for i in res.json()['Data']:
            # print(i)
            id=i['Images'][0]['ID']
            src_list=i["ImageSrcs"]
            for src in src_list:
                detail_title = src.split('/')[-1].replace('.jpg', '')
                res1=requests.get(url=src,headers=headers)
                save(id,res1,detail_title)
    except Exception as e:
        print(e)

def save(id,res1,detail_title):
    if not os.path.exists(f'./汉服/{id}'):
        os.makedirs(f'./汉服/{id}')
    path=f'汉服/{id}/{detail_title}.jpg'
    with open(path,'wb+')as f:
        f.write(res1.content)
        print(f'{id}写入成功!')


if __name__=='__main__':
    threading.BoundedSemaphore(3)
    for i in range(1,11):
        print('正在爬取%d页' % i)
        t=threading.Thread(target=parse,args=(i,))
        t.start()
        parse(i)
    print('爬取完成')
