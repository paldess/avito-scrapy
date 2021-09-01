import scrapy
from avitopars.items import AvitoparsItem
from scrapy.http import HtmlResponse
import time
from date_mounth import mounth_

class AvitoruSpider(scrapy.Spider):
    name = 'avitoru'
    allowed_domains = ['avito.ru']
    start_urls = ['https://www.avito.ru/rossiya/chasy_i_ukrasheniya/kupit-chasy-ASgBAgICAUTQAYYG?p=1&q=%D0%BC%D1%83%D0%B6%D1%81%D0%BA%D0%B8%D0%B5+%D0%BD%D0%B0%D1%80%D1%83%D1%87%D0%BD%D1%8B%D0%B5+%D1%87%D0%B0%D1%81%D1%8B&user=1']
    page = 1
    def parse(self, response: HtmlResponse):
        links = response.xpath('//a[@itemprop="url"]/@href').getall()
        if len(response.xpath("//span[contains(@class, '_readonly')]")) == 0 :
            self.page += 1
            pages = f'https://www.avito.ru/rossiya/chasy_i_ukrasheniya/kupit-chasy-ASgBAgICAUTQAYYG?p={self.page}&q=%D0%BC%D1%83%D0%B6%D1%81%D0%BA%D0%B8%D0%B5+%D0%BD%D0%B0%D1%80%D1%83%D1%87%D0%BD%D1%8B%D0%B5+%D1%87%D0%B0%D1%81%D1%8B&user=1'
            yield response.follow(pages, callback=self.parse)
        elif len(response.xpath("//span[contains(@class, '_readonly')]")) == 1 and self.page == 1:
            self.page += 1
            pages = f'https://www.avito.ru/rossiya/chasy_i_ukrasheniya/kupit-chasy-ASgBAgICAUTQAYYG?p={self.page}&q=%D0%BC%D1%83%D0%B6%D1%81%D0%BA%D0%B8%D0%B5+%D0%BD%D0%B0%D1%80%D1%83%D1%87%D0%BD%D1%8B%D0%B5+%D1%87%D0%B0%D1%81%D1%8B&user=1'
            yield response.follow(pages, callback=self.parse)
        for link in links:
            time.sleep(0.2)
            yield response.follow(link, callback=self.read)


    def read(self, response: HtmlResponse):
        name = response.xpath("//span[@class='title-info-title-text']/text()").get()
        date = response.xpath('//div[@class="title-info-metadata-item-redesign"]/text()').get().split()
        date = ' '.join(date[:2])
        last = mounth_(date)

        try:
            views = int(response.xpath("//div[contains(@class, 'title-info-metadata-views')]/text()").getall()[1].split()[0])
        except IndexError:
            views = None
        if len(response.xpath('//span[@itemprop="price"]')) != 0:
            price1 = response.xpath('//span[@itemprop="price"]/text()').getall()[0].split()
            price = ''
            for i in price1:
                price = price + i
            price = int(price)
        else:
            price = response.xpath("//span[contains(@class, 'price-value-string')]/text()").getall()[-1].replace('\n', '')

        item = AvitoparsItem(name=name, views=views, price=price, last=last)

        yield item