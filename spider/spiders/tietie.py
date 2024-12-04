import scrapy

class TietieSpider(scrapy.Spider):
    name = "tietie"
    allowed_domains = ["www.tieba.com"]
    start_urls = ["https://tieba.baidu.com/f?ie=utf-8&kw=%E5%AF%BB%E4%BB%99&fr=search"]

    def parse(self, response):
        for info in response.css('ul#thread_list li.j_thread_list'):
            title = info.xpath('./div/div[2]/div[1]/div[1]/a/text()').extract_first()
            print(title)
            yield {'title': title}
        next_page = response.css('div#frs_list_pager a.next::attr(href)').extract_first()
        print(next_page)
        if next_page:
            next_page_url = 'https:' + next_page
            yield scrapy.Request(next_page_url, callback=self.parse)
