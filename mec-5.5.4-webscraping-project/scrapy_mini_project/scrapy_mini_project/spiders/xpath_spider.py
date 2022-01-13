import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        with open("xpath.json", "w") as outfile:
            json.dump({
                'text': response.xpath('//title/text()').get(),
            }, outfile)
