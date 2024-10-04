import requests
from lxml import etree
from fake_useragent import UserAgent
ua=UserAgent()

class XueJuZi():
    def __init__(self):
        self.url='http://www.xuejuzi.cn/jilirenxin/'
        self.headers={'User-Agent':ua.chrome}
        self.href_list=[]

    def requests_get(self):
        res=requests.get(url=self.url,headers=self.headers)
        res.encoding='gb2312'

        #获取一页中的所有链接
        html=etree.HTML(res.text)
        href_list1=html.xpath('/html/body/div[2]/div[1]/dl/dd[1]/a/@href')
        for i in href_list1:
            self.href_list.append(i)

    def detail_get(self):
        for i in self.href_list:
            res=requests.get(url=i,headers=self.headers)
            res.encoding='gb2312'
            print(f'正在爬取{i}页')
            html=etree.HTML(res.text)
            #每一页详情页的标题
            title=html.xpath('/html/body/div[2]/div[1]/div[2]/h1/text()')[0]
            content_list1=html.xpath('//*[@id="content"]/p/text()')
            content_list1.insert(0,title)
            for j in content_list1:
                self.save(j,title)


    def save(self,i,title):
        with open('./data.txt','a+',encoding='utf-8')as f:
            f.write(f'{i}\n')
            print(f'{title}爬取成功!!')

x=XueJuZi()
x.requests_get()
x.detail_get()