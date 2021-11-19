import os
BOT_NAME = 'price_monitor'

SPIDER_MODULES = ['price_monitor.spiders']
NEWSPIDER_MODULE = 'price_monitor.spiders'

# if you want to run it locally, replace None with your scrapy cloud API key
SHUB_KEY = None
# if you want to run it locally, replace PROJ_ID by your Scrapy Cloud project ID
SHUB_PROJ_ID = os.getenv('SHUB_JOBKEY', 'PROJ_ID').split('/')[0]

ITEM_PIPELINES = {
    'price_monitor.pipelines.CollectionStoragePipeline': 400,
}
