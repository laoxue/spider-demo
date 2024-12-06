import scrapy
from scrapy.linkextractors import LinkExtractor

class ZhidemaiSpider(scrapy.Spider):
    name = "zhidemai"
    start_urls = ["https://search.smzdm.com/?c=home&s=4070ti+super&v=a&mx_v=a"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                callback=self.parse,
                headers={
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'Accept-Language': 'zh-HK,zh;q=0.9,zh-CN;q=0.8',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
                    'Referer': 'https://search.smzdm.com'
                }
            )

    def parse(self, response):
        # 使用 LinkExtractor 提取下一页链接
        le = LinkExtractor(
            restrict_xpaths='//ul[@id="J_feed_pagenation"]/li[last()]/a'  # 定位下一页按钮
        )
        links = le.extract_links(response)

        # 提取页面中的商品信息
        rows = response.css('ul#feed-main-list li[data-atp="3"]')
        for row in rows:
            title = row.css('h5.feed-block-title a:first-child::text').get().strip()
            price = row.css('h5.feed-block-title a:nth-child(2) div.z-highlight::text').get().strip()
            plantform = row.css('span.feed-block-extras span::text').get().strip()
            detail_url = row.css('h5.feed-block-title a:first-child::attr(href)').get()
            yield scrapy.Request(
                detail_url,
                callback=self.parse_detail,
                headers={
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'Accept-Language': 'zh-HK,zh;q=0.9,zh-CN;q=0.8',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
                    'Referer': 'https://search.smzdm.com'
                },
                meta={'title': title, 'price': price, 'plantform': plantform}
            )
            # yield {
            #     'title': title,
            #     'price': price,
            #     'plantform': plantform,
            #     'detail_url': detail_url
            # }

        # 如果存在下一页链接，继续请求
        # if links:
        #     next_url = links[0].url
        #     self.logger.info(f"Following next page: {next_url}")
        #     yield scrapy.Request(
        #         next_url,
        #         callback=self.parse,
        #         headers={
        #             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        #             'Accept-Language': 'zh-HK,zh;q=0.9,zh-CN;q=0.8',
        #             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        #         }
        #     )

    def parse_detail(self, response):
        title = response.meta['title']
        price = response.meta['price']
        plantform = response.meta['plantform']
        commitbox = response.css('ul.comment-main-list li')
        commit_text_box = []
        for commit in commitbox:
            commit_text = commit.css('div.comment-main-list-item-content-comment span::text').get().strip()
            commit_text_box.append(commit_text)
        yield {
                'title': title,
                'price': price,
                'plantform': plantform,
                'commit_text': commit_text_box
            }
