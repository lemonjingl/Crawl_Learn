import requests
import threading
from urllib import request,parse
import os
from queue import  Queue
from concurrent.futures import ThreadPoolExecutor
q=Queue(22)

url='https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?'
def url_json_get(p):
    headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55'}
    data={'activityId': '2735',
    'sVerifyCode': 'ABCD',
    'sDataType': 'JSON',
    'iListNum': '20',
    'totalpage': '0',
    'page':f'{p}',
    'iOrder': '0',
    'iSortNumClose': '1',
    'iAMSActivityId': '51991',
    '_everyRead': 'true',
    'iTypeId': '2',
    'iFlowId': '267733',
    'iActId': '2735',
    'iModuleId': '2735',
    '_': '1674006116809'}
    response=requests.get(url,params=data,headers=headers)
    for i in response.json()['List']:
        image_name=i['sProdName']#图片名字
        print(image_name)
        image_name1=parse.unquote(image_name)#图片名字解码
        for it in range(2,9):
            image_url=i[f'sProdImgNo_{it}'].replace('200','0')#获取图片链接
            image_url1=parse.unquote(image_url)#图片链接解码
            q.put([image_name1,image_url1])



def save_image():
    while True:#一直拿数据
        print(f'目前队列的数量{q.qsize()}')
        try:
            data=q.get()
        except:
            break
        path=os.path.join('E:\\PYTHON\\wb',data[0])#os.path.join拼接路径
        try:
            os.makedirs(path)
        except:
            pass
        path = os.path.join(path, data[1].split('/')[-2])
        request.urlretrieve(data[1],path)
        print(f"{data[1].split('/')[-2]}保存成功")



for i in range(10):
    t=threading.Thread(target=url_json_get,args=(i,))#每个线程获取一个页面
    t.start()

for i in range(15):
    t=threading.Thread(target=save_image)#10个消费者保存图片
    t.start()