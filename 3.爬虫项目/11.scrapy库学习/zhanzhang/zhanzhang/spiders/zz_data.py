import re

import scrapy
from ..items import ZhanzhangItem


class ZzDataSpider(scrapy.Spider):
    name = "zz_data"
    allowed_domains = ["sc.chinaz.com"]
    start_urls = ["https://sc.chinaz.com/tupian/fengjing.html"]+[f"https://sc.chinaz.com/tupian/fengjing_{i}.html" for i in range(2,51)]

    def parse(self, response):
        url_list=response.xpath('/html/body/div[3]/div[2]/div/img/@data-original').extract()
        name_list=response.xpath('/html/body/div[3]/div[2]/div/img/@alt').extract()
        data=zip(url_list,name_list)
        for i,j in data:
            item=ZhanzhangItem()
            img_url='https:'+i.split('_')[0]+'.jpg'
            img_name=j
            item['img_url']=img_url
            item['img_name']=img_name
            yield item





# https://scpic.chinaz.net/files/default/imgs/2023-08-03/bf4b755506988fb9.jpg
# https://scpic1.chinaz.net/files/default/imgs/2023-08-03/bf4b755506988fb9_s.jpg