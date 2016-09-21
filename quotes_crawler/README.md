#Spiders for Quotes.Toscrape.com

This project contains spiders to scrape many variations of the [quotes.toscrape.com](https://quotes.toscrape.com), such as:

* `toscrape-css`: scrapes [quotes.toscrape.com](https://quotes.toscrape.com) using CSS selectors;
* `toscrape-xpath`: scrapes [quotes.toscrape.com](https://quotes.toscrape.com) using XPath;
* `toscrape-microdata`: read the semantic markup data from [quotes.toscrape.com](https://quotes.toscrape.com) using [extruct](https://github.com/scrapinghub/extruct);
* `toscrape-js`: scrapes the JavaScript-powered version of `Quotes to Scrape`([quotes.toscrape.com/js](https://quotes.toscrape.com/js)) using [js2xml](https://github.com/scrapinghub/js2xml) to parse the data from inside the JavaScript code;
* `toscrape-selenium`: scrapes the JavaScript-powered version of `Quotes to Scrape`([quotes.toscrape.com/js](https://quotes.toscrape.com/js)) using Selenium + PhantomJS to render the page;
* `toscrape-infinite-scrolling`: scrapes the infinite scrolling version ([quotes.toscrape.com/scroll](https://quotes.toscrape.com/scroll)) via AJAX API calls;
* `toscrape-csrf-login-v1`: authenticates into [quotes.toscrape.com/login](https://quotes.toscrape.com/login) loading the CSRF token manually into the request;
* `toscrape-csrf-login-v2`: authenticates into [quotes.toscrape.com/login](https://quotes.toscrape.com/login) using `FormRequest.from_respose()` to load automatically the CSRF token;

