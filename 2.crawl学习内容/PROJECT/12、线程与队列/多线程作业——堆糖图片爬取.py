import requests
import threading
from queue import Queue
from urllib import request
import os
from threading import Lock
import time
lock=Lock()

url='https://www.duitang.com/napi/blog/list/by_search/?'
q=Queue(30)
def url_get():
    for i in range(24,50,24):
        p=1674305643898
        p+=1

        data={'nclude_fields': 'like_count,sender,album,msg,reply_count,top_comments',
        'kw': '夜景',
        'start': f'{i}',
        '_': f'{p}'}

        response=requests.get(url=url,params=data)
        for j in response.json()['data']['object_list']:
            id=j['photo']['id']
            image_url=j['photo']['path']
            # print(id,image_url)
            q.put([id, image_url])
        lock.release()
def image_save():
    while True:
        #print(f'目前队列的数量{q.qsize()}')
        try:
            data=q.get(timeout=5)
            print(data)
        except:
            break
        try:
            path = f'./_public/{data[0]}'
            if not os.path.exists(path):
                os.makedirs(path)

        except:
            pass
        i=0
        path1=f'_public/{data[0]}/{i}.jpg'
        i+=1
        request.urlretrieve(data[1],path1)
# url_get()
# image_save()

for i in range(3):
    lock.acquire()
    t=threading.Thread(target=url_get)
    t.start()
for i in range(5):
    t=threading.Thread(target=image_save)
    t.start()



