import scrapy


class QuotesSpider(scrapy.Spider):
    
        #name must be unique ,you can set the same name for different spiders
        name = "quotes"
   
def start_requests(self):
        #must return an iterable of Requests (you can return a list of requests or write a generator function)
        #  which the Spider will begin to crawl from. Subsequent requests will be generated successively from 
        # these initial requests.
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        #parse(): a method that will be called to handle the response downloaded for each of the requests made.
         #  The response parameter is an instance of TextResponse that holds the page content and has further 
        # helpful methods to handle it.
def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)