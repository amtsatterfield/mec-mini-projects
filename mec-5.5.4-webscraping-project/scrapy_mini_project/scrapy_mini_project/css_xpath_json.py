from spiders import quotes_spider, css_spider, xpath_spider
from scrapy.crawler import CrawlerProcess


def save_html():
    process = CrawlerProcess()
    process.crawl(quotes_spider.QuotesSpider)
    process.start()


def save_css_title():
    process = CrawlerProcess()
    process.crawl(css_spider.QuotesSpider)
    process.start()


def save_xpath_title():
    process = CrawlerProcess()
    process.crawl(xpath_spider.QuotesSpider)
    process.start()


def main():
    # comment/uncomment methods you would like to before running
    # save_html()
    # save_css_title()
    save_xpath_title()


if __name__ == '__main__':
    main()
