from scrapy.settings import Settings
from scrapy.crawler import CrawlerProcess

from avitopars import settings
from avitopars.spiders.avitoru import AvitoruSpider
# from avitopars.spiders.book24 import Book24Spider

if __name__ == '__main__':
    crauler_settings = Settings()
    crauler_settings.setmodule(settings)

    process = CrawlerProcess(crauler_settings)
    process.crawl(AvitoruSpider)
    # process.crawl(Book24Spider)

    process.start()