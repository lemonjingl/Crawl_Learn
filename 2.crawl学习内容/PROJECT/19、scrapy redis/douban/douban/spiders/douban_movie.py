import scrapy
from ..items import DoubanItem
from scrapy_redis.spiders import RedisSpider
class DoubanMovieSpider(RedisSpider):
    name = 'douban_movie'
    allowed_domains = ['movie.douban.com']
    init=0
    # start_urls = ['https://movie.douban.com/j/chart/top_list?type=24&interval_id=100:90&action=&start=0&limit=20']
    redis_key='douban_movie:start_urls'
    def parse(self, response,*_):
        for i in response.json():
            item=DoubanItem()
            title=i['title']
            score=i['score']
            rank=i['rank']
            release_data=i['release_date']
            actors=i['actors']

            item['title']=title
            item['score']=score
            item['rank']=rank
            item['release_data']=release_data
            item['actors']=actors
            yield item
        self.init+=20
        url_list=f'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100:90&action=&start={self.init}&limit=20'
        yield scrapy.Request(url=url_list,callback=self.parse)
