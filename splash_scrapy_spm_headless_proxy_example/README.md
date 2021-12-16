# Zyte Smart Proxy Headless Proxy + Splash + Scrapy Example Project

This example project shows how to use [Smart Proxy Manager (Formally Crawlera)](https://www.zyte.com/smart-proxy-manager/)
with [Zyte Smart Proxy Headless Proxy](https://github.com/zytedata/zyte-smartproxy-headless-proxy)
and [Splash](https://www.zyte.com/splash/) (a JavaScript
rendering service) with Scrapy spiders.


## How does it work?

The integration between Splash and Zyte Smart Proxy Headless Proxy is done by a
[Lua script](https://github.com/scrapinghub/sample-projects/blob/master/splash_scrapy_spm_headless_proxy_example/splash_scrapy_spm_headless_proxy_example/scripts/smart_proxy_manager.lua)
that is sent to Splash with every request created by the spider. This script configures
Splash to use Zyte Smart Proxy Headless Proxy as its proxy and also defines a couple rules to avoid
doing useless requests, such as analytics ones, stylesheets, images, etc.


## What do I need to run this project?

Here's what you'll need:

- a Splash instance and a Smart Proxy Manager account: you can get both via Scrapy Cloud billing page
  - you can also run Splash in your own machine following the [instructions here](http://splash.readthedocs.io/en/stable/install.html)
- Setup and run Zyte Smart Proxy Headless Proxy using this [documentation](https://docs.zyte.com/smart-proxy-manager/headless.html)
- set your Splash settings this project's [settings.py](https://github.com/scrapinghub/sample-projects/blob/master/splash_scrapy_spm_headless_proxy_example/splash_scrapy_spm_headless_proxy_example/settings.py)
file:
  - `SPLASH_URL`: the URL where your Splash instance is available, by default this is set to `http://localhost:8050`.
