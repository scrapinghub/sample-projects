from price_monitor.spiders._base import BaseSpider
from price_monitor.items import PriceLoader


class BooksSpider(BaseSpider):
    name = "books.toscrape.com"

    def parse(self, response):
        item = response.meta.get('item', {})
        loader = PriceLoader(item=item, response=response)
        loader.add_value('url', response.url)
        loader.add_css('name', 'h1::text')
        loader.add_css('price', '.price_color::text')
        yield loader.load_item()

