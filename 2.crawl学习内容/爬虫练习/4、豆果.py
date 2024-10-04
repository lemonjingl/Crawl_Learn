import requests
import re
from lxml import etree
import pymysql
import pymongo
from queue import Queue
class DouGuo():
    def get_url(self,url1):
        headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
        self.response=requests.get(url=url1,headers=headers)


    def parse(self):
        self.q=Queue()
        name=re.findall(r'<a class="cookname text-lips" href="/cookbook/.*?.html" target="_blank">(.*?)</a>',self.response.text)
        author=re.findall(r' <a class="author text-lips" .*?>.*?<img src=".*?" alt=".*?"> (.*?)',self.response.text,re.S)
        playback=re.findall(r'<div class="view-coll">.*?<span class="view">(.*?)</span>',self.response.text,re.S)
        collection=re.findall(r'<div class="view-coll">.*?<span class="view">.*?</span>.*?<span class="collect">(.*?)</span>',self.response.text,re.S)
        data=zip(name,author,playback,collection)
        for name,author,playback,collection in data:
            self.q.put([name,author,playback,collection])

    def save_data(self):
        self.parse()
        while True:
            print(self.q.qsize())
            data=self.q.get()

            name=data[0]
            author=data[1]
            playback=data[2]
            collection=data[3]

            db = pymysql.connect(host='localhost', user='root', password='123456', database='my_spider')
            cur = db.cursor()
            sql = 'INSERT INTO douguo_data(name,author,playback,collection) values (%s,%s,%s,%s)'
            try:
                data3=(name,author,playback,collection)
                cur.execute(sql,data3)
                db.commit()
            except Exception as e:
                print(f'失败{e}')

if __name__=='__main__':
    d = DouGuo()
    for i in range(0, 130, 24):
        url1 = f'https://www.douguo.com/jingxuan/{i}'
        d.get_url(url1)

        d.parse()
        d.save_data()

