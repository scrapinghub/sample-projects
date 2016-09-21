import scrapy


class ToScrapeCSRFLoginSpiderV1(scrapy.Spider):
    name = 'toscrape-csrf-login-v1'
    start_urls = [
        'http://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        # Forms with CSRF verification generates a CSRF token for each request
        # and they require that same value in the data the client sends back.
        # WARNING:
        #  This could be done automatically using FormRequest.from_response()
        #  check toscrape-csrf-login-v2.py for reference
        token = response.css("input[name=csrf_token] ::attr(value)").extract_first()
        yield scrapy.FormRequest(
            self.start_urls[0],
            formdata={
                'csrf_token': token,
                'username': 'valdir',
                'password': 'abc'
            },
            callback=self.after_login
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
