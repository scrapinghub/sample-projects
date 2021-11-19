from scrapy import Item, Field
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from price_parser import Price


class Product(Item):
    url = Field()
    title = Field()
    price = Field()


class ProductLoader(ItemLoader):
    default_item_class = Product
    default_output_processor = TakeFirst()

    title_in = MapCompose(lambda x: x.strip())
    price_in = MapCompose(lambda x: Price.fromstring(x).amount_float)




