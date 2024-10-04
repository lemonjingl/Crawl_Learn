import requests
from lxml import etree
f=open('data2.csv','w+',encoding='utf-8')
for i in range(1,6):
    url=f'https://gl.lianjia.com/ershoufang/linguiqu/pg{i}/'
    print(url)
    headers={'User-Agent':''}
    response=requests.get(url,headers=headers)

    html=etree.HTML(response.text)
    data_1=html.xpath('//ul[@class="sellListContent"]/li/div/div[1]/a/text()')#名称
    data_2=html.xpath('//ul[@class="sellListContent"]/li/div/div[2]/div/a[1]/text()')#位置
    data_3=html.xpath('//ul[@class="sellListContent"]/li/div/div[6.中国五矿集团采购信息]/div[2]/span/text()')#单价
    data_4=html.xpath('//ul[@class="sellListContent"]/li/div/div[6.中国五矿集团采购信息]/div[1]/span/text()')#总价
    data=zip(data_1,data_2,data_3,data_4)
    for name,address,price,all_price in data:
        print(f'{name},{address},{price},{all_price}万\n')
        try:
            f.write(f'{name},{address},{price},{all_price}万\n')
        except:
            pass
f.close()