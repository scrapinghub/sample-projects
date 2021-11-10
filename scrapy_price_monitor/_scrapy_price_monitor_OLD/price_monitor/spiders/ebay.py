from extruct.w3cmicrodata import MicrodataExtractor
from .base_spider import BaseSpider


class EbaySpider(BaseSpider):
    name = "ebay.com"

    def parse(self, response):
        extractor = MicrodataExtractor()
        properties = extractor.extract(response.body_as_unicode()).get('items')[0].get('properties', {})
        item = response.meta.get('item', {})
        item['url'] = response.url
        item['title'] = properties.get('name').replace('Details about', '').strip()
        item['price'] = float(
            properties.get('offers', {}).get('properties', {}).get('price', 0)
        )
        yield item
