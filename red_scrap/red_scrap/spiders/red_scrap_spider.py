import scrapy
from scrapy.spiders import  CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from red_scrap.items import RedScrapItem, IncomeScrapItem


class RedScrapSpider(CrawlSpider):
    name = "indeed"
    allowed_domains = ["indeed.com"]
    start_urls = [
        "http://www.indeed.com/jobs?q=python+analyst&l=ca&rq=1&fromage=last"
    ]
    rules = (
        Rule(LinkExtractor(allow=('&start=',)), callback='parse_indeed'),
    )

    def parse_indeed(self, response):

        for sel in response.xpath('//div [@class="  row  result"]'):
            items = RedScrapItem()

            items['title'] = sel.xpath('.//a[@class="turnstileLink"]/@title').extract()
            items['url'] =  sel.xpath('.//a[@class="turnstileLink"]/@href').extract()
            for key in items['url']:
                key = [str('http://www.indeed.com/')+ key]
                items['url'] = key
            items['company'] = sel.xpath('.//span[@itemprop="name"]/text()').extract()
            items['location'] = sel.xpath('.//span[@itemprop="addressLocality"]/text()').extract()
            yield items

        for sel in response.xpath('//div [@id="SALARY_rbo"]'):
            quants = IncomeScrapItem()

            quants["quantity"] = sel.xpath('.//a/@title').extract()

            yield quants




