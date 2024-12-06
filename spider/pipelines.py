from itemadapter import ItemAdapter
import pymongo

# class PriceConvertPipeline:
#     exchange_rate = 8.5
#     def process_item(self, item, spider):
#         price = float(item['price'][1:]) * self.exchange_rate
#         item['price'] = '￥%.2f' % price
#         return item;

# clappccss SpiderPipeline:
#     def __init__(self):
#         self.book_set = set()
#     def process_item(self, item, spider):
#         name = item['name']
#         if name in self.book_set:
#             raise DropItem('Duplicate book found: %s' % item)
#         else:
#             self.book_set.add(name)
#             return item

# class MongoDBPipeline:
#     def __init__(self, mongo_uri, mongo_db):
#         self.mongo_uri = mongo_uri
#         self.mongo_db = mongo_db

#     @classmethod
#     def from_crawler(cls, crawler):
#         # 从settings中读取配置
#         return cls(
#             mongo_uri=crawler.settings.get('MONGO_URI'),
#             mongo_db=crawler.settings.get('MONGO_DATABASE')
#         )

#     def open_spider(self, spider):
#         # 当爬虫启动时，创建MongoDB连接
#         self.client = pymongo.MongoClient(self.mongo_uri)
#         self.db = self.client[self.mongo_db]

#     def close_spider(self, spider):
#         # 当爬虫关闭时，关闭MongoDB连接
#         self.client.close()

#     def process_item(self, item, spider):
#         # 将数据插入MongoDB
#         self.db['books'].insert_one(ItemAdapter(item).asdict())
#         return item
        