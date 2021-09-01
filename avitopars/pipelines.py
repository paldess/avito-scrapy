# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class AvitoparsPipeline:
    def __init__(self):
        db =MongoClient('localhost', 27017)
        self.base = db.avito['мужские часы']

    def process_item(self, item, spider):
        if len([i for i in self.base.find(dict(item))]) == 0:
            self.base.insert_one(dict(item))
        return item
