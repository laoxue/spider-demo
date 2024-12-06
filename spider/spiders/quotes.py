import scrapy
from scrapy_splash import SplashRequest
from scrapy.linkextractors import LinkExtractor
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["https://quotes.toscrape.com/"]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 2})  # 'wait' 用于等待页面加载

    def parse(self, response):
        title = response.css("div.quote > span.text::text").getall()
        yield {
            'title': title
        }
