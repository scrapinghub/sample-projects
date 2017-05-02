import scrapy
from splash_crawlera_example.utils import SplashCrawleraRequest


class QuotesJsSpider(scrapy.Spider):
    name = 'quotes-js'

    def start_requests(self):
        yield SplashCrawleraRequest(url='http://quotes.toscrape.com/js/')

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
        next_page = response.css('li.next > a::attr(href)').extract_first()
        if next_page:
            yield SplashCrawleraRequest(url=response.urljoin(next_page))
