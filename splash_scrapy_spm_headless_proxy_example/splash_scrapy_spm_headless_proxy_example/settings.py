# -*- coding: utf-8 -*-

BOT_NAME = 'splash_scrapy_spm_headless_proxy_example'
SPIDER_MODULES = ['splash_scrapy_spm_headless_proxy_example.spiders']
NEWSPIDER_MODULE = 'splash_scrapy_spm_headless_proxy_example.spiders'

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

# Splash settings
SPLASH_URL = 'http://localhost:8050'  # Splash instance URL from Scrapy Cloud
SPLASH_APIKEY = ''  # Your API key for the Splash instance hosted on Scrapy Cloud
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
