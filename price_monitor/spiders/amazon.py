from .base_spider import BaseSpider


class AmazonSpider(BaseSpider):
    name = "milsims.com"

    def parse(self, response):
        for product in response.css(".view-advanced-catalog tr > td"):

    item = {}
    item['title'] = product.css(".views-field-title a ::text").extract_first()
    item['price'] = product.css(".views-field-phpcode span span::text").extract()[1]
    item['url'] = product.css(".views-field-title a::attr(href)").extract()
        yield item

    next_page = response.css('li.pager-nexta::attr(href)').extract_first()
    if next_page is not None:
        next_page = response.urljoin(next_page)
        yield scrapy.Request(next_page, callback=self.parse)
