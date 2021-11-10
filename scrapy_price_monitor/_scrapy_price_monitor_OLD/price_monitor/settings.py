# -*- coding: utf-8 -*-
import os

BOT_NAME = 'price_monitor'
SPIDER_MODULES = ['price_monitor.spiders']
NEWSPIDER_MODULE = 'price_monitor.spiders'

ROBOTSTXT_OBEY = True

SHUB_KEY = os.getenv('$SHUB_KEY')
# if you want to run it locally, replace '999999' by your Scrapy Cloud project ID below
SHUB_PROJ_ID = os.getenv('SHUB_JOBKEY', '999999').split('/')[0]


# settings for Amazon SES email service
AWS_ACCESS_KEY = os.getenv('$AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('$AWS_SECRET_KEY')
EMAIL_ALERT_FROM = 'Price Monitor <SENDER_EMAIL@provider.com>'
EMAIL_ALERT_TO = ['RECEIVER_EMAIL@provider.com']

# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'price_monitor.pipelines.CollectionStoragePipeline': 400,
}

AUTOTHROTTLE_ENABLED = True
# HTTPCACHE_ENABLED = True
