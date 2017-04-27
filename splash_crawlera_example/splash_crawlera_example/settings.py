# -*- coding: utf-8 -*-
import os

BOT_NAME = 'splash_crawlera_example'
SPIDER_MODULES = ['splash_crawlera_example.spiders']
NEWSPIDER_MODULE = 'splash_crawlera_example.spiders'

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy_crawlera.CrawleraMiddleware': 300,
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

# Crawlera settings
CRAWLERA_ENABLED = True
CRAWLERA_APIKEY = os.getenv('CRAWLERA_APIKEY')

# Splash settings
SPLASH_URL = os.getenv('SPLASH_URL')  # <-- Splash instance URL from Scrapy Cloud
SPLASH_APIKEY = os.getenv('SPLASH_APIKEY')  # <-- your API key
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
