import scrapy
from scrapy_splash import SplashRequest
from w3lib.http import basic_auth_header


class QuotesJs2Spider(scrapy.Spider):
    """Example spider using Splash to render JavaScript-based pages.
       Make sure you configure settings.py with your Splash
       credentials (available on Scrapy Cloud).
    """
    name = 'quotes-js-2'

    def start_requests(self):
        yield SplashRequest(
            'http://quotes.toscrape.com/js',
            splash_headers={
                'Authorization': basic_auth_header(self.settings['APIKEY'], ''),
            },
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
                response.urljoin(next_page),
                splash_headers={
                    'Authorization': basic_auth_header(self.settings['APIKEY'], ''),
                },
            )
