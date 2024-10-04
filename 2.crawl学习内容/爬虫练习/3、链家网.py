import threading

import requests
from lxml import etree
import re
import pymysql
import pymongo
from queue import  Queue


class LianJia():
    def get_url(self,url):
        headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
        self.response=requests.get(url=url,headers=headers)

    def parse(self):
        self.q=Queue(100)
#xpath 获取的数据
        # html=etree.HTML(self.response.text)
        # data_list=html.xpath('//*[@id="content"]/div[1]/ul/li/div[1]')
        # for i in data_list:
        #     self.title=i.xpath('./div[1]/a/text()')[0]#房子名称
        #
        #     a = i.xpath('./div[2]/div/a/text()')[0]
        #     b=i.xpath('./div[2]/div/a/text()')[1]
        #     self.location=a+b#房子位置
        #     self.conten= i.xpath('./div[3]/div/text()')[0]#房子情况
        #     self.all_price = i.xpath('./div[6.中国五矿集团采购信息]/div[1]/span/text()')[0]#房子总价
        #     self.price = i.xpath('./div[6.中国五矿集团采购信息]/div[2]/span/text()')[0]#房子多少钱一平
        #     self.q.put([self.title,self.location,self.conten,self.all_price,self.price])
        #     print(f'parse    {threading.current_thread()}')


        data1=re.findall(r'<div class="info clear">.*?<div class="title"><a class="" href=".*?" .*?>(.*?).</a>',self.response.text,re.S)
        data2=re.findall(r'<a href=".*?" target="_blank" data-log_index=".*?" data-el="region">(.*?) </a>',self.response.text)
        data3=re.findall(r'<div class="houseInfo"><span class="houseIcon"></span>(.*?)</div></div><div class="followInfo">',self.response.text)
        data4=re.findall(r'<div class="totalPrice totalPrice2"><i> </i><span class="">(.*?)</span><i>.*?</i>',self.response.text)
        data5 = re.findall(r'<div class="unitPrice" data-hid=".*?" data-rid=".*?" data-price=".*?"><span>(.*?)</span></div>', self.response.text)
        data=zip(data1,data2,data3,data4,data5)
        for self.title,self.location,self.conten,self.all_price,self.price in data:
            self.q.put([self.title,self.location,self.conten,self.all_price,self.price])
            # print(f'{self.title}---{self.location}----{self.conten}----{self.all_price}---{self.price}')
#re获取的数据


    def save_data(self):
        self.parse()
        while True:
            print(self.q.qsize() )
            data=self.q.get()#从队列中取得数据
            title=data[0]
            location=data[1]
            conten=data[2]
            all_price=data[3]
            price=data[4]
            if self.q.qsize()==0:
                break
#mysql保存数据
            try:
                db=pymysql.connect(host='localhost',
                                user='root',
                                password='123456',
                                database='my_spider')
                cur=db.cursor()
            except Exception as e:
                print(e)

            sql='INSERT INTO lianjia_data(title,location,conten,all_price,price) VALUES (%s,%s,%s,%s,%s)'
            try:
                data=(title,location,conten,all_price,price)
                cur.execute(sql,data)
                db.commit()
                print('保存成功')
            except Exception as e:
                print(f'失败:{e}')

#mongodb数据保存
            # cli=pymongo.MongoClient(host='localhost',port=27017)
            # # 获取要操作的数据库
            # db=cli.my_spiders
            # # 获取要操作的集合
            # Collection=db.lianjia_data
            # data2={'title':title,'location':location,'conten':conten,'all_price':all_price,'price':price}
            # Collection.insert_one(data2)
            # print('保存成功')


if __name__=='__main__':
    l=LianJia()
    for i in range(1, 15):
        url = f'https://gl.lianjia.com/ershoufang/linguiqu/pg{i}'
        l.get_url(url)
        l.parse()
        l.save_data()






