import scrapy

class SpiderItem(scrapy.Item):
    # 定义你的字段
    name = scrapy.Field()
    price = scrapy.Field()
    
class ImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()  # 需要添加这个字段来存储下载的图片信息