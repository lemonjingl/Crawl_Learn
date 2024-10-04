import scrapy


class MovieDoubanSpider(scrapy.Spider):
    name = 'movie_douban'
    allowed_domains = ['movie.douban.com']
    init=0
    start_urls = ['https://movie.douban.com/j/chart/top_list?type=24&interval_id=100:90&action=&start=0&limit=20']

    def parse(self, response):
        for i in response.json():
            yield i
        self.init+=20
        url_list=f'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100:90&action=&start={self.init}&limit=20'
        yield scrapy.Request(url_list,callback=self.parse)