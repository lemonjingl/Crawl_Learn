import requests
from fake_useragent import UserAgent
ua=UserAgent()
import threading

# https://mp-action.csdn.net/interact/wrapper/pc/fans/v1/api/getFansOffsetList?pageSize=20&username=qing_gee
class Fan():
    def __init__(self,):
        self.url='https://mp-action.csdn.net/interact/wrapper/pc/fans/v1/api/getFansOffsetList?'
        self.headers = {'User-Agent': ua.chrome}

    #请求参数
    def get_headers(self,fanId):
        data = {
            'pageSize': '20',
            'username': 'qing_gee',
            'fanId': f'{fanId}'
        }
        return data

    def requests_get(self):
        global fanId
        res=requests.get(url=self.url,params=self.get_headers(fanId),headers=self.headers)

        #数据提取
        fanId=str(res.json()['data']['fanId'])
        print(fanId)
        for i in res.json()['data']['list']:
            nickname=i['nickname']
            username=i["username"]
            blogUrl=i['blogUrl']
            print(f'{nickname}\t{username}\t{blogUrl}')
            self.save(nickname,username,blogUrl)
        if len(fanId) >0:
            self.get_headers(fanId)
            self.requests_get()

    def save(self,nickname,username,blogUrl):
        with open('./data.txt','a+',encoding='utf-8')as f:
            f.write(f'{nickname}\t{username}\t{blogUrl}\n')
            print(f'{nickname}爬取完成')

if __name__=='__main__':
    f=Fan()
    f.start()
    fanId=''
    f.get_headers(fanId)
    f.requests_get()