import json
import pkgutil
from datetime import datetime, timedelta


def timestamp_from_reversed(reversed):
    return datetime(5000, 1, 1) - timedelta(seconds=float(reversed))


def reversed_timestamp():
    return str((datetime(5000, 1, 1) - datetime.now()).total_seconds())


def normalize_name(name):
    return name.replace('-', '')


def get_product_names():
    return [
        normalize_name(name)
        for name in json.loads(
            pkgutil.get_data("price_monitor", "resources/urls.json").decode()
        ).keys()
    ]


def get_retailer_name_from_url(url):
        return url.split("://")[1].split("/")[0].replace("www.", "")


def get_retailers_for_product(product_name):
    data = json.loads(
        pkgutil.get_data("price_monitor", "resources/urls.json").decode()
    )
    return {get_retailer_name_from_url(url) for url in data[product_name]}
