import scrapy
from ..items import ZaihangItem

class ZaihDataSpider(scrapy.Spider):
    name = "zaih_data"
    allowed_domains = ["www.zaih.com"]
    pag=1
    url="https://www.zaih.com/falcon/mentors?page={}"
    start_urls = [url.format(pag)]


    def parse(self, response):
        print(response.url)
        item=ZaihangItem()
        name_list=response.xpath('//*[@id="__layout"]/section/div/section/div[2]/a/section/div/div[1]/span[1]/text()').extract()
        city_list=response.xpath('//*[@id="__layout"]/section/div/section/div[2]/a/section/div/div[1]/span[2]/text()').extract()
        industry_list=response.xpath('//*[@id="__layout"]/section/div/section/div[2]/a/section/div/div[2]/text()').extract()
        price_list=response.xpath('//*[@id="__layout"]/section/div/section/div[2]/a/section/div/div[3]/span/text()').extract()
        number_chatters_list=response.xpath('//*[@id="__layout"]/section/div/section/div[2]/a/div/span[1]/text()').extract()
        score_list=response.xpath('//*[@id="__layout"]/section/div/section/div[2]/a/div/span[3]/text()').extract()
        data=zip(name_list,city_list,industry_list,price_list,number_chatters_list,score_list)

        for name,city,industry,price,number_chatters,score in data:
            item['name']=name
            item['city']=city
            item['industry']=industry
            item['price']=price.replace('\n','').replace(' ','')
            item['number_chatters']=number_chatters
            item['score']=score.replace('\n','').replace(' ','')
            # print(price)
            # print(score)
            yield item
        # 再次生成请求
        self.pag+=1
        next_url=(self.url.format(self.pag))
        print(next_url)
        yield scrapy.Request(url=next_url,callback=self.parse)
    # 姓名、城市、行业、价格、聊天人数、评分
