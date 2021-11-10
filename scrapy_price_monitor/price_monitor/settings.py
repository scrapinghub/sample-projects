import os
BOT_NAME = 'price_monitor'

SPIDER_MODULES = ['price_monitor.spiders']
NEWSPIDER_MODULE = 'price_monitor.spiders'

# if you want to run it locally, replace None with your scrapy cloud API key
SHUB_KEY = None
# if you want to run it locally, replace '999999' by your Scrapy Cloud project ID
SHUB_PROJ_ID = os.getenv('SHUB_JOBKEY', '999999').split('/')[0]

ITEM_PIPELINES = {
    'price_monitor.pipelines.CollectionStoragePipeline': 400,
}

# settings for Amazon SES email service
AWS_ACCESS_KEY = os.getenv('$AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('$AWS_SECRET_KEY')
EMAIL_ALERT_FROM = 'Price Monitor <SENDER_EMAIL@provider.com>'
EMAIL_ALERT_TO = ['RECEIVER_EMAIL@provider.com']
