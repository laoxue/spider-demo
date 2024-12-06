import scrapy
# from ..items import SpiderItem
import json

class TiebaSpider(scrapy.Spider):
    name = "tieba"
    start_urls = ["https://jsonplaceholder.typicode.com/posts"]

    def parse(self, response):
       datas = json.loads(response.text)
       for data in datas:
            yield {
                'id': data['id'],
                'title': data['title'],
                'body': data['body'],
            }