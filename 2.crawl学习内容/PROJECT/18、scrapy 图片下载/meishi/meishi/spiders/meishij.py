import scrapy
from ..items import MeishiItem

class MeishijSpider(scrapy.Spider):
    name = 'meishij'
    allowed_domains = ['meishij.net']
    start_urls = ['https://www.meishij.net/china-food/caixi/chuancai/']

    def parse(self, response):
        item=MeishiItem()
        src_list=response.xpath('//*[@id="listtyle1_list"]/div/a/img/@src').extract()
        for src in src_list:
            item['src']=[src]
            yield item
