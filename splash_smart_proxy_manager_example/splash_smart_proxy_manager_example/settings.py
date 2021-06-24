# -*- coding: utf-8 -*-

BOT_NAME = 'splash_smart_proxy_manager_example'
SPIDER_MODULES = ['splash_smart_proxy_manager_example.spiders']
NEWSPIDER_MODULE = 'splash_smart_proxy_manager_example.spiders'

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

CRAWLERA_APIKEY = ''  # Your crawlera API key

# Splash settings
SPLASH_URL = ''  # Splash instance URL from Scrapy Cloud
SPLASH_APIKEY = ''  # Your API key for the Splash instance hosted on Scrapy Cloud
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
