import scrapy


class FanyiBaiduSpider(scrapy.Spider):
    name = 'fanyi_baidu'
    allowed_domains = ['fanyi.daidu.com']
    start_urls = ['https://fanyi.baidu.com/sug']

    def start_requests(self):
        data={'kw': '新年'}
        for url in self.start_urls:
            yield  scrapy.FormRequest(url=url,formdata=data,callback=self.parse)

    def parse(self, response):
        print(response.text)
