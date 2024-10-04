import scrapy
from ..items import  YoushewangItem

class YoushewDataSpider(scrapy.Spider):
    name = "youshew_data"
    allowed_domains = ["www.uisdc.com"]
    page=1
    next_url="https://www.uisdc.com/category/uiicon/page/{}"
    start_urls = ["https://www.uisdc.com/category/uiicon/"]

    def parse(self, response):
        item=YoushewangItem()
        data=response.xpath('/html/body/div[3]/div[4.ontariogenomics]/div/div[1]/div/div/div/div/div')
        for i in data:
            title=i.xpath('./h2[@class="item-title"]/a/text()').extract()
            author=i.xpath('./h4/div[1]/a/i[2]/text()').extract()
            tag=i.xpath('./h4/div[2]/a/i[2]/text()').extract()
            if  len(title)!=0 or len(author)!=0 or len(tag)!=0:
                item['title']=title[0]
                item['author']=author[0]
                item['tag']=tag
                yield item
        self.page+=1
        next_url1=self.next_url.format(self.page)
        print(next_url1)
        yield scrapy.Request(url=next_url1,callback=self.parse)



# 标题、作者、标签