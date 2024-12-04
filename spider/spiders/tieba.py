import scrapy
from ..items import SpiderItem


class TiebaSpider(scrapy.Spider):
    name = "tieba"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        for sel in response.css('article.product_pod'):
            book = SpiderItem()
            book['name'] = sel.xpath('./h3/a/@title').extract_first()
            book['price'] = sel.css('p.price_color::text').extract_first()
            yield book
        
        next_page = response.css('ul.pager li.next a::attr(href)').extract_first()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)
