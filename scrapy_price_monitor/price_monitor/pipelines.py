from price_monitor import settings
from price_monitor.collection_helper import CollectionHelper
from price_monitor.utils import reversed_timestamp, get_product_names


class CollectionStoragePipeline:
    def open_spider(self, spider):
        self.data_stores = {}
        for product_name in get_product_names():
            store = CollectionHelper(
                proj_id=settings.SHUB_PROJ_ID,
                collection_name=product_name,
                api_key=settings.SHUB_KEY,
                create=True,
            )
            self.data_stores[product_name] = store

    def process_item(self, item, spider):
        key = "{}-{}-{}".format(
            reversed_timestamp(), item.get('product_name'), item.get('retailer')
        )
        store = self.data_stores[item['product_name']]
        store.set(key, item)
        return item

    def close_spider(self, spider):
        for store in self.data_stores.values():
            store.flush_writer()
