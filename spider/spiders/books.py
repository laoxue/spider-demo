import scrapy
from spider.items import ImageItem

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["http://books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        item = ImageItem()
        for book in response.css('article.product_pod'):
            image_urls = response.css('img::attr(src)').getall()
            item['image_urls'] = [response.urljoin(url) for url in image_urls]
            yield item