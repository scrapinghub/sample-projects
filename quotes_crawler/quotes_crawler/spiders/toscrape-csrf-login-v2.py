import scrapy


class ToScrapeCSRFLoginSpiderV2(scrapy.Spider):
    name = 'toscrape-csrf-login-v2'
    start_urls = [
        'http://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        # FormRequest.from_response automatically loads all the form data that
        # is in the form present in the response object. This way, we don't
        # have to worry about explicitly loading the CSRF token in the data we
        # will POST to the server.
        yield scrapy.FormRequest.from_response(
            response,
            formdata={
                'username': 'any',
                'password': 'doesnt matter'
            },
            callback=self.after_login,
        )

    def after_login(self, response):
        authenticated = response.css('div.header-box p > a::text').extract_first() == 'Logout'
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span::text').extract_first(),
                'author': quote.css('small::text').extract_first(),
                'tags': quote.css('.tags a::text').extract(),
                'authenticated': authenticated,
            }
