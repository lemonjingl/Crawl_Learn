# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter


class ZaihangPipeline:
    def __init__(self):
        self.db=pymysql.connect(host='localhost',
                                user='root',
                                password='123456',
                                database='my_mysql')
        self.cur=self.db.cursor()

    def process_item(self, item, spider):
        try:
            sql='insert into zaihang (`name`,city,industry,price,number_chatters,score) values (%s,%s,%s,%s,%s,%s)'
            data=(item['name'],item['city'],item['industry'],item['price'],item['number_chatters'],item['score'])
            self.cur.execute(sql,data)
            self.db.commit()
        except Exception as e:
            print(e)
        return item

    def close_spider(self):
        self.db.close()

