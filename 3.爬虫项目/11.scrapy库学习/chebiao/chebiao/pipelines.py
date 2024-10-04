# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
import os
from unrar import rarfile

class ChebiaoPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['file_url'],meta={'item':item})

    def file_path(self, request, response=None, info=None, *, item=None):
        item=request.meta['item']

        path=item['file_name']+'.rar'
        return path

