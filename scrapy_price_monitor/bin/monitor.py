"""Simple price monitor built with Scrapy and Scrapy Cloud
"""
import argparse
import os
from datetime import datetime, timedelta

import boto
from hubstorage import HubstorageClient
from jinja2 import Environment, PackageLoader
from price_monitor import settings
from price_monitor.utils import get_product_names, get_retailers_for_product
from w3lib.html import remove_tags

jinja_env = Environment(loader=PackageLoader('price_monitor', 'templates'))


class DealsChecker(object):

    def __init__(self, latest_deals, previous_deals, price_threshold=0):
        self.price_threshold = price_threshold
        self.latest_deals = latest_deals
        self.previous_deals = previous_deals

    def is_from_latest_crawl(self, deal):
        """Checks whether the given deal is from the most recent execution.
        """
        return deal in self.latest_deals

    def get_best_deal(self):
        """Returns the item with the best overall price. self.price_threshold can be set to avoid
           considering minor price drops.
        """
        best_so_far = min(self.previous_deals, key=lambda x: x.get('price'))
        best_from_last = min(self.latest_deals, key=lambda x: x.get('price'))
        if best_from_last.get('price') + self.price_threshold < best_so_far.get('price'):
            return best_from_last
        else:
            return best_so_far


class DealsFetcher(object):

    def __init__(self, product_name, apikey, project_id, hours):
        self.product_name = product_name
        project = HubstorageClient(apikey).get_project(project_id)
        self.item_store = project.collections.new_store(product_name)
        self.load_items_from_last_n_hours(hours)

    def load_items_from_last_n_hours(self, n=24):
        """Load items from the last n hours, from the newest to the oldest.
        """
        since_time = int((datetime.now() - timedelta(hours=n)).timestamp() * 1000)
        self.deals = [item.get('value') for item in self.fetch_deals_newer_than(since_time)]

    def fetch_deals_newer_than(self, since_time):
        return list(self.item_store.get(meta=['_key', '_ts'], startts=since_time))

    def get_latest_deal_from_retailer(self, retailer):
        """Returns the most recently extracted deal from a given retailer.
        """
        for deals in self.deals:
            if retailer in deals.get('url'):
                return deals

    def get_deals(self):
        """Returns a tuple with (deals from latest crawl, deals from previous crawls)
        """
        latest_deals = [
            self.get_latest_deal_from_retailer(retailer)
            for retailer in get_retailers_for_product(self.product_name)
        ]
        previous_deals = [
            deal for deal in self.deals if deal not in latest_deals
        ]
        return latest_deals, previous_deals


def send_email_alert(items):
    ses = boto.connect_ses(settings.AWS_ACCESS_KEY, settings.AWS_SECRET_KEY)
    html_body = jinja_env.get_template('email.html').render(items=items)

    ses.send_email(
        settings.EMAIL_ALERT_FROM,
        'Price drop alert',
        remove_tags(html_body),
        settings.EMAIL_ALERT_TO,
        html_body=html_body
    )


def main(args):
    items = []
    for prod_name in get_product_names():
        fetcher = DealsFetcher(prod_name, args.apikey, args.project, args.days * 24)
        checker = DealsChecker(*fetcher.get_deals(), args.threshold)
        best_deal = checker.get_best_deal()
        if checker.is_from_latest_crawl(best_deal):
            items.append(best_deal)

    if items:
        send_email_alert(items)


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apikey', default=settings.SHUB_KEY or os.getenv('SHUB_KEY'),
                        help='API key to use for scrapinghub (fallbacks to SHUB_KEY variable)')
    parser.add_argument('--days', type=int, default=1,
                        help='How many days back to compare with the last price')
    parser.add_argument('--threshold', type=float, default=0,
                        help='A margin to avoid raising alerts with minor price drops')
    parser.add_argument('--project', type=int, default=settings.SHUB_PROJ_ID,
                        help='Project ID to get info from')

    return parser.parse_args()


if __name__ == '__main__':
    main(parse_args())
