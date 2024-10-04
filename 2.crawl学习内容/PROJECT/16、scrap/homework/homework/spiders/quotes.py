import re

import scrapy
from ..items import HomeworkItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = []
    for i in range(1,4):
        url=f'https://quotes.toscrape.com/page/{i}/'
        start_urls.append(url)


    def parse(self, response):
        items=HomeworkItem()
        content=re.findall(r'<span class="text" itemprop="text">(.*?)</span>',response.text)
        author=re.findall(r'<span>by <small class="author" itemprop="author">(.*?)</small>',response.text)
        for content1,author1 in zip(content,author):
            # print(f'{content1}-----={author1}')
            items['content']=content1
            items['author']=author1
            # print(items['content'])
            yield items

