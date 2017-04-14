# -*- coding: utf-8 -*-

# Scrapy settings for splash_based_project project

BOT_NAME = 'splash_based_project'
SPIDER_MODULES = ['splash_based_project.spiders']
NEWSPIDER_MODULE = 'splash_based_project.spiders'

# Splash settings
SPLASH_URL = ''     # <-- Splash instance URL from Scrapy Cloud
APIKEY = ''         # <-- your API key
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
