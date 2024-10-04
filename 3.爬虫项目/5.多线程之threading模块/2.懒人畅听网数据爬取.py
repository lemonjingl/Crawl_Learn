import csv

import requests
from fake_useragent import UserAgent
from lxml import etree

class MyThread():
    def __init__(self,url):
        self.headers={'User-Agent':ua.chrome}
        self.url=url

    def requests_get(self):
        res=requests.get(url=self.url,headers=self.headers)
        # print(res.text)
        #数据解析
        html=etree.HTML(res.text)
        data=html.xpath('//ul[@class="clearfix"]/li/div[2]')
        for i in data:
            title=i.xpath('./a/text()')[0]
            author=i.xpath('./div[2]/a[1]/text()')[0]
            weaken=i.xpath('./div[2]/a[2]/text()')[0]
            print(f'{title},{author},{weaken}')
            self.save(title,author,weaken)

    def save(self,title,author,weaken):
        # header=('书名','作者','主播')
        with open('./data.csv','a+',encoding='gbk')as f:
            f.write(f'{title},{author},{weaken}\n')

if __name__=='__main__':
    ua=UserAgent()
    url='http://www.lrts.me/book/category/1/recommend/{}/20'
    urls=[url.format(i) for i in range(1,2)]
    for i in urls:
        m=MyThread(i)
        m.requests_get()
