import json
import scrapy


# Most AJAX based websites can be scraped by reproducing the API calls made
# by the browser, as we do in this simple example that scrapes
# a website paginated via infinite scrolling (quotes.toscrape.com/scroll)
class ToScrapeInfiniteScrollingSpider(scrapy.Spider):
    name = 'toscrape-infinite-scrolling'
    base_url = 'http://quotes.toscrape.com/api/quotes?page=%d'
    start_urls = [base_url % 1]

    def parse(self, response):
        json_data = json.loads(response.text)
        for quote in json_data['quotes']:
            yield quote
        if json_data['has_next']:
            yield scrapy.Request(self.base_url % (int(json_data['page']) + 1))
