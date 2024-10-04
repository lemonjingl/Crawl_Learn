import requests
import threading
import os
from queue import Queue
from urllib import parse,request
from concurrent.futures import ThreadPoolExecutor
url='https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?'
q=Queue()
def get_parse():
    for t in range(1,11):
        headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
        data={'activityId':'2735',
        'sVerifyCode':'ABCD',
        'sDataType':'JSON',
        'iListNum':'20',
        'totalpage':'0',
        'page':f'{t}',
        'iOrder':'0',
        'iSortNumClose':'1',
        'iAMSActivityId':'51991',
        '_everyRead':'true',
        'iTypeId':'2',
        'iFlowId':'267733',
        'iActId':'2735',
        'iModuleId':'2735',
        '_':'1675042623506'
              }
        response=requests.get(url=url,params=data,headers=headers)
    for i in response.json()['List']:
        name=parse.unquote(i['sProdName'])
        for j in range(2,9):
            image_url=parse.unquote(i[f'sProdImgNo_{j}']).replace('/200','/0')
            q.put([name,image_url])

def image_save():
    while True:
        print(q.qsize())
        data=q.get()
        path=os.path.join('./image/',data[0])
        try:
            if not os.path.exists(path):
                os.makedirs(path)
            else:
                pass
        except Exception as e:
            print(f'失败：{e}')
        try:
            path1=os.path.join(path,data[1].split('/')[-2])
            request .urlretrieve(data[1],path1)
            print(f"{data[1].split('/')[-2]}")
        except Exception as e:
            print(f'保存失败{e}')
get_parse()
image_save()
# pool=ThreadPoolExecutor(max_workers=15)
# pool.submit(get_parse)
#
# pool1=ThreadPoolExecutor(max_workers=20)
# pool1.submit(image_save)

# pool.shutdown()
# pool1.shutdown()
