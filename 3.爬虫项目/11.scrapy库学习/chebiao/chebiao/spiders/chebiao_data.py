import scrapy
from ..items import ChebiaoItem

class ChebiaoDataSpider(scrapy.Spider):
    name = "chebiao_data"
    allowed_domains = ["www.521609.com"]
    start_urls = ["http://www.chebiao.net/domestic.php"]

    def parse(self, response):
        url_list=response.xpath('//*[@id="main"]/div[2]/div/dl/dd/a[1]/@href').extract()
        name_list=response.xpath('//*[@id="main"]/div[2]/div/dl/dd/a[1]/text()').extract()
        data=zip(url_list,name_list)
        item=ChebiaoItem()
        for i,j in data:
            file_url='http://www.chebiao.net/'+i
            file_name=j
            item['file_url']=file_url
            item['file_name']=j
            yield item


