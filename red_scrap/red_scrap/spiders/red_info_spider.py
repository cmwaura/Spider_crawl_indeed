import scrapy
from scrapy.spiders import CrawlSpider, Rule


class RedInfoSpider(CrawlSpider):
    name = "text_indeed"
    rules = (
        Rule(LinkExtractor(allow=('/rc/clk?',)), callback='parse_reader'),
    )
