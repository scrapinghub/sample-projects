import scrapy
from extruct.w3cmicrodata import LxmlMicrodataExtractor


class ToScrapeMicrodataSpider(scrapy.Spider):
    name = "toscrape-microdata"
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        extractor = LxmlMicrodataExtractor()
        items = extractor.extract(response.text, response.url)['items']
        for it in items:
            yield it['properties']

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
