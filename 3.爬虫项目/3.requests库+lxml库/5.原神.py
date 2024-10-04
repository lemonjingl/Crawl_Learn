import requests
from lxml import etree
from fake_useragent import UserAgent
ua=UserAgent()


url='https://ys.mihoyo.com/main/character/mondstadt?char=0'
headers={'User-Agent':ua.chrome,
        'cookie': '_MHYUUID=6d7977b9-e8f4-4159-adff-dc734ee056b6; DEVICEFP_SEED_ID=3411325c3eef4d58; DEVICEFP_SEED_TIME=1681396797506; DEVICEFP=38d7edf5d7d90',
        'referer': 'https://cn.bing.com/'
         }
res=requests.get(url=url,headers=headers)
print(res.text)


html=etree.HTML(res.text)
title=html.xpath('//*[@id="frame"]/div[4.ontariogenomics]/div/div/div[3]/div[2]/div[1]/ul/li[1]/p/text()')
print(title)