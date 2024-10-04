# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql
class DoubanPipeline:
    def process_item(self, item, spider):
        return item

class MySqlSavePipeline:
    def __init__(self):
        self.db = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database='my_spider')
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        sql = 'INSERT INTO douban_data(title,score,rank,release_data,actors) VALUES(%s,%s,%s,%s,%s) '
        try:
            data=(item['title'],item['score'],item['rank'],item['release_data'],'./'.join(item['actors']))
            self.cur.execute(sql,data)
            self.db.commit()
            return item
        except Exception as e:
            print(e)

    def __del__(self):
        self.db.close()