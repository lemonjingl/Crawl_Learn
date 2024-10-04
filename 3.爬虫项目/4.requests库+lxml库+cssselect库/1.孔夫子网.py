# coding = utf-8
import requests
from lxml.html import etree
import csv

class CSS:
    def __init__(self):
        self.url = 'https://www.kongfz.com/1004/?page={}'

        self.cookies = {
            'shoppingCartSessionId': 'd081910f30dbd051bbc30d2a5aa43864',
            'reciever_area': '1006000000',
            'kfz_uuid': '320c3a51-c13c-4f1a-bc3e-1c5151ea026f',
            'Hm_lvt_bca7840de7b518b3c5e6c6d73ca2662c': '1690508930',
            'Hm_lvt_33be6c04e0febc7531a1315c9594b136': '1690508930',
            'acw_tc': '2760829316905089541845822e0a72ca42aa79d93ff6cccb5f862ea190f74e',
            'Hm_lpvt_33be6c04e0febc7531a1315c9594b136': '1690509174',
            'Hm_lpvt_bca7840de7b518b3c5e6c6d73ca2662c': '1690509174',
            'kfz_trace': '320c3a51-c13c-4f1a-bc3e-1c5151ea026f|0|-|',
            'PHPSESSID': 'l4t14uib8j8sjjnukbs2mkrep7',
        }

        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Referer': 'https://www.kongfz.com/1004/?page=2',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'sec-ch-ua': '\\',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '\\',
        }
        self.flage=True

    def request(self,page):
        response = requests.get(url=self.url.format(page), headers=self.headers, cookies=self.cookies)
        html=etree.HTML(response.text)
        data=html.cssselect('#listBox > div > div.item-info')

        for i in data:
            title=i.cssselect('div.title > a')[0].text
            introduce=i.cssselect('div.zl-isbn-info > span:nth-child(1)')[0].text
            published=i.cssselect('div.zl-isbn-info > span:nth-child(2)')[0].text.strip('/').strip(' ')
            self.save(title,introduce,published)

    def save(self,title,intorduce,published):
        with open('./孔夫子网数据.csv','a+',encoding='GB18030',newline='')as csv_file:
            writer=csv.writer(csv_file)

            if self.flage:
                writer.writerow(['书名','简介','出版社'])
                self.flage=False
            writer.writerow([title,intorduce,published])
            # print(f'{title}保存完成')

    def run(self):
        for i in range(1,11):
            print(f'正在爬取第{i}页')
            self.request(i)
        print('爬取完成')

c=CSS()
c.run()

