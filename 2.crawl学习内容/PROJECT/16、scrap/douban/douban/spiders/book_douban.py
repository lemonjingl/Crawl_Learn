import re
from ..items import DoubanItem
import scrapy


class BookDoubanSpider(scrapy.Spider):
    name = 'book_douban'#名字不要重复  根据爬虫的名字启动爬虫
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/top250?start=0']

    def parse(self, response):
        items=DoubanItem()
        #解析数据
        title_list=response.xpath('//div[@class="pl2"]/a')
        for i in title_list:
            title=i.xpath('./text()').getall()[0].replace(' ','').replace('\n','')
            #封装解析好的数据并传输
            items['title']=title
            yield items




