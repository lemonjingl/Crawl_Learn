import requests
from requests import Session
from lxml import etree
class LoginYaoZhiWANG():
    def __init__(self):
        url='https://www.yaozh.com/login'
        headers={'User-Agent':''}
        data={
        'username': '18078418293',
        'pwd': 'Lzz18777392734',
        'country': '86_zh-CN',
        'formhash': '8EB0CB00C6',
        'backurl': 'https%3A%2F%2Fwww.yaozh.com%2F'
            }
        session = Session()
        response=session.post(url=url,data=data,headers=headers)

        url1='https: // www.yaozh.com / member /'
        self.response=session.get(url=url1,headers=headers)

    def parse(self):
        html=etree.HTML(self.response.text)
        balance_title=html.xpath('//*[@id="U_warp"]/div/div[1]/div/div[2]/div[1]/div[1]/h3')
        balance=html.xpath('//*[@id="U_warp"]/div/div[1]/div/div[2]/div[1]/div[1]/div/span[1]')
        print(f'{balance_title}--{balance}')

l=LoginYaoZhiWANG()
l.parse()
