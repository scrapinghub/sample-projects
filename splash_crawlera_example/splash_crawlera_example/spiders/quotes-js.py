import pkgutil
import scrapy
from scrapy_splash import SplashRequest
from w3lib.http import basic_auth_header


class QuotesJsSpider(scrapy.Spider):
    name = 'quotes-js'

    def __init__(self, *args, **kwargs):
        self.LUA_SOURCE = pkgutil.get_data(
            'splash_crawlera_example', 'scripts/crawlera.lua'
        ).decode()
        super(QuotesJsSpider).__init__(*args, **kwargs)

    def start_requests(self):
        yield SplashRequest(
            'http://quotes.toscrape.com/js',
            endpoint='execute',
            splash_headers={
                'Authorization': basic_auth_header(self.settings['SPLASH_APIKEY'], ''),
            },
            args={
                'lua_source': self.LUA_SOURCE,
                'crawlera_user': self.settings['CRAWLERA_APIKEY'],
                'crawlera_pass': '',
            }
        )

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        next_page = response.css('li.next > a::attr(href)').extract_first()
        if next_page:
            yield SplashRequest(
                url=response.urljoin(next_page),
                endpoint='execute',
                splash_headers={
                    'Authorization': basic_auth_header(self.settings['SPLASH_APIKEY'], ''),
                },
                args={
                    'lua_source': self.LUA_SOURCE,
                    'crawlera_user': self.settings['CRAWLERA_APIKEY'],
                    'crawlera_pass': '',
                }
            )
