from .base_spider import BaseSpider


class AmazonSpider(BaseSpider):
    name = "milsims.com"

    def parse(self, response):
        for product in response.css(".view-advanced-catalog tr > td"):
            item = {}
            item ['title'] = product.css(".views-field-title a ::text").extract_first()
            item ['price'] = product.css(".views-field-phpcode span span::text").extract()[1]
            item ['url'] = product.css(".views-field-title a::attr(href)").extract()
        yield item
