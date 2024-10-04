import requests
from requests import Session
from lxml import etree
class login_17K():
    def __init__(self):
        url='https://passport.17k.com/ck/user/login'
        data={   'loginName': '18078418293',
                'password': 'lzz18777392734'
                }
        headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
                 ,'Cookie': 'GUID=8f0e9054-e1e8-43db-8264-ebeb0ca9fafa; __bid_n=185e3dafd414723cd94207; c_channel=0; c_csc=web; Hm_lvt_9793f42b498361373512340937deb2a0=1674565058,1674619618,1674967115; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F15%252F55%252F53%252F99885355.jpg-88x88%253Fv%253D1673368440000%26id%3D99885355%26nickname%3D%25E6%259F%25A0%25E6%25AA%25AC%25E7%25B2%25BEningmeng%26e%3D1690519147%26s%3Da9980fea83ccace3; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2299885355%22%2C%22%24device_id%22%3A%22185e3dafc9539e-0fb54d80fa9b73-26021051-921600-185e3dafc96e4b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%228f0e9054-e1e8-43db-8264-ebeb0ca9fafa%22%7D; FPTOKEN=ZKObzdXG0Y1hR721rUtdjKUbYHij1aakD1mxRPfxK/cuLX7zZymU/FXdTwAQBl99jm+6q8NOghSCZ5FDCXdzTTvA5l1cl8/KSF+lRWfgC+af52llE4wcA/dwnEcxSeQN/V6aFFrnC8VWiik1HMI/ANWGf6P3jcBrHhHrCDhcAnnBIGPXAPAL1vydArd7vfTaZ1cxOGmKjnk5D/YmbtFCrtgb5850NisBtIfUIGq4u3xZVdiZH9Qa9N1hdd7hV36ksEhs+vvmVchm011EsBWDptssn7sRw2kqYuAzMAbFS5BxyzvZjTwMY1EFZ6fkIBQXXD4mxZC41CNI5vKNEgr6R6a/24xgWPikXANv8qv8dohOvQnKWd0fB0DksJHZdorNuYRNG6zaSVi//XJEGHuv0o6l9GCRRrlCqfaKtHib5PplsegMntyW3p3jHh/4Pevf|yf1y2YEkN4yURUN2Kde36iWC/wM4wOW9E7ffMNr5B6Y=|10|93a3637c778ff2c01355e4fe682f7dc2; Hm_lpvt_9793f42b498361373512340937deb2a0=1674974318'}

        session=Session()
        self.response=session.post(url=url,data=data,headers=headers)

        url1='https://user.17k.com/www/account/index.html'
        self.res=session.get(url=url1,headers=headers)
        self.res.encoding='utf-8'


    def parse(self):
        print(self.response.text)
        html=etree.HTML(self.res.text)
        news_title=html.xpath('//div[@class="rl"]/div[2]/h2/span/text()')#新闻公告

        print(news_title)

l=login_17K()
l.parse()