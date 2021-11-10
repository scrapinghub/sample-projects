import json
import pkgutil
import scrapy
from datetime import datetime


class BaseSpider(scrapy.Spider):

    def start_requests(self):
        products = json.loads(pkgutil.get_data('price_monitor', 'resources/urls.json').decode())
        for name, urls in products.items():
            for url in urls:
                if self.name in url:
                    now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
                    item = {'product_name': name, 'retailer': self.name, 'when': now}
                    yield scrapy.Request(url, meta={'item': item})
