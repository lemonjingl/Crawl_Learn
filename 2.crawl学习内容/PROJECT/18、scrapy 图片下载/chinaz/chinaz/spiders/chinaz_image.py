import scrapy
import re
from ..items import ChinazItem
class ChinazImageSpider(scrapy.Spider):
    name = 'chinaz_image'
    allowed_domains = ['chinaz.com']
    start_urls = ['https://sc.chinaz.com/tupian/fengjing.html']+[f'https://sc.chinaz.com/tupian/fengjing_{i}.html' for i in range(2,11)]

    def parse(self, response):
        object = re.compile(r'<div class="item">.*?<img src=".*?".*?data-original="(?P<image_url>.*?)".*?'
                            r'class="lazy".*?alt="(?P<image_name>.*?)".*?/>', re.S)
        res = object.finditer(response.text)
        for i in res:
            items = ChinazItem()
            image_urls = 'https:' + i.group('image_url')
            image_name = i.group('image_name')
            items['image_name'] = image_name
            items['image_urls'] = [image_urls]
            yield items
