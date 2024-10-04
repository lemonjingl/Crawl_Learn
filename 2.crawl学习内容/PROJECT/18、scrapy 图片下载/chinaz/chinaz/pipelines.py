# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
class ChinazPipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     return item
    def get_media_requests(self, item, info):
        #这个方法会循环执行
        #前面每次传入一个item这个item被交给了引擎
        #引擎又交给管道来执行  管道里面有很多个方法
        #这些方法会依次执行
        yield scrapy.Request(url=item['image_urls'][0],meta={'item':item})
    def file_path(self, request, response=None, info=None, *, item=None):
        item=request.meta['item']
        #设置图片路径为    类型名称/url地址
        # image_name=item['image_urls'][0].split('/'[-1])
        path=item['image_name']+'.jpg'
        return path