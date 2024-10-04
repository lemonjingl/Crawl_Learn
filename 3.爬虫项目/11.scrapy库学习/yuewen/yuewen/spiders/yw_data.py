import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CbSpider(CrawlSpider):
    name = 'yw_data'
    allowed_domains = ['write.qq.com']
    start_urls = ['https://write.qq.com/portal/article?filterType=0&page=1']
    # URL 提取规则
    rules = (
        Rule(LinkExtractor(allow=r'.*/portal/content\?caid=\d+&feedType=2&lcid=\d+$'), callback="parse_item"),
        # 寻找下一页 url 地址
        Rule(LinkExtractor(restrict_xpaths="//a[@title='下一页']"), follow=True),
    )

    def parse_item(self, response):
        print("测试输出")
        print(response.url)
        # title = response.css('title::text').extract()[0]
        # print(title)
        item = {}
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        return item
