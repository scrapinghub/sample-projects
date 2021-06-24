# Splash + Smart Proxy Manager Example Project

This example project shows how to use [Smart Proxy Manager (Formally Crawlera)](https://www.zyte.com/smart-proxy-manager/)  and [Splash](https://www.zyte.com/splash/) (a JavaScript
rendering service) with Scrapy spiders.


## How does it work?

The integration between Splash and Smart Proxy Manager is done by a
[Lua script](https://github.com/scrapinghub/sample-projects/blob/master/splash_crawlera_example/splash_crawlera_example/scripts/crawlera.lua)
that is sent to Splash with every request created by the spider. This script configures
Splash to use Smart Proxy Manager as its proxy and also defines a couple rules to avoid doing
useless requests, such as analytics ones, stylesheets, images, etc.


## What do I need to run this project?

Here's what you'll need:

- a Splash instance and a Smart Proxy Manager account: you can get both via Scrapy Cloud billing page
  - you can also run Splash in your own machine following the [instructions here](http://splash.readthedocs.io/en/stable/install.html)
- set your Splash settings this project's [settings.py](https://github.com/scrapinghub/sample-projects/blob/master/splash_crawlera_example/splash_crawlera_example/settings.py)
file:
  - `SPLASH_URL`: the URL where your Splash instance is available
  - `SPLASH_APIKEY`: your Splash API key (required if you're using an instance from Scrapy Cloud)
- set your Crawlera settings in the same file:
  - `CRAWLERA_APIKEY`: the API key for your Smart Proxy Manager user
