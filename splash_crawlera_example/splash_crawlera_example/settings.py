# -*- coding: utf-8 -*-
import os
BOT_NAME = 'splash_crawlera_example'
SPIDER_MODULES = ['splash_crawlera_example.spiders']
NEWSPIDER_MODULE = 'splash_crawlera_example.spiders'

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

# Splash + Crawlera settings
SPLASH_CRAWLERA_ENABLED = True
CRAWLERA_APIKEY = '' or os.getenv('CRAWLERA_APIKEY')  # Paste your crawlera API key
SPLASH_URL = '' or os.getenv('SPLASH_URL')  # Paste Splash instance URL from Scrapy Cloud
SPLASH_APIKEY = '' or os.getenv('SPLASH_APIKEY')  # Paste your API key for the Splash instance hosted on Scrapy Cloud
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
