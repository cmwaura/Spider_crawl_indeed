import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from red_scrap.items import RedScrapItem, DescriptionScrapItem, RedDiceItem


class RedScrapSpider (CrawlSpider):
    name = "Indeed"
    allowed_domains = ["indeed.com"]

    # python+analyst
    rules = (
        Rule(LinkExtractor(allow=('&start=',)), callback='parse_indeed'),
            )

    def __init__(self, job=None, state=None, *args, **kwargs):
        '''

        :param job: str, takes in the job you are searching for. Note, in the command line this will be \
        "scrapy crawl indeed -a job". If the job has two words i.e, python analyst type it as python+analyst
        :param args: pass a non-keyworded, variable length argument
        :param kwargs: pass a keyworded, variable length argument
        :return:

        '''
        # super is used to for inheritance from the class RedScrapSpider

        super(RedScrapSpider, self).__init__(*args, **kwargs)

        # start url with the added job instance
        self.start_urls = [
            "http://www.indeed.com/jobs?q=%s&l=%s&rq=1&fromage=last" %(job, state)
                          ]

    def parse_indeed(self, response):
        '''

        :param response: Html object. This is the parsed object that was stored under respons\
        for reference please check the file indeed.html that comes with the  script.
        :return: Dict

        '''

        for sel in response.xpath('//div [@class="  row  result"]'):
            item = RedScrapItem()

            item['title'] = sel.xpath('.//a[@class="turnstileLink"]/@title').extract()
            item['url'] = sel.xpath('.//a[@class="turnstileLink"]/@href').extract()
            key = [str('http://www.indeed.com/') + key for key in item['url']]
            item['url'] = key

            item['company'] = sel.xpath('.//span[@itemprop="name"]/text()').extract()
            item['location'] = sel.xpath('.//span[@itemprop="addressLocality"]/text()').extract()
            yield item
        #
       


class RedDescriptionSpider(CrawlSpider):
    name = "Descriptor"
    allowed_domains = ["dice.com"]

    rules = (
            Rule(LinkExtractor(allow=("/jobs/detail",)), callback="parse_description_notes"),

        )

    def __init__(self, job=None, state=None, limit=None, *args, **kwargs):
        super(RedDescriptionSpider, self).__init__(*args, **kwargs)

        self.start_urls = [
            # "https://www.dice.com/jobs?q=%s&l=%s" % (job, state)
            "https://www.dice.com/jobs?q=%s&l=%s&limit=%s" % (job, state, limit)

        ]

    def parse_description_notes(self, response):
        filename = response.url.split("/")[-2]+'.html'
        with open(filename, 'wb') as f:
            f.write(response.body)



class RedDiceSpider(scrapy.Spider):
    name = "Dice"
    allowed_domains = ["dice.com"]

    def __init__(self, job=None, state=None, limit=None, *args, **kwargs):
        super(RedDiceSpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            # "https://www.dice.com/jobs?q=%s&l=%s" % (job, state)
            "https://www.dice.com/jobs?q=%s&l=%s&limit=%s" % (job, state, limit)
        ]

    def parse(self, response):

        print "the results from:", RedDiceSpider.name
        for sel in response.xpath('//div [@class="serp-result-content"]'):
            dice_item = RedDiceItem()

            dice_item["title"] = sel.xpath('.//h3/a[@class="dice-btn-link"]/text()').extract()
            clean_data = ' '.join(dice_item["title"]).strip(' \n\t')
            dice_item['title'] = [clean_data]
            dice_item['url'] = sel.xpath('.//h3/a[@class="dice-btn-link"]/@href').extract()
            dice_item["company"] = sel.xpath('.//li [@class="employer"]/span/a[@class="dice-btn-link"]/text()').extract()
            dice_item['location'] = sel.xpath('.//li [@class="location"]/text()').extract()

            yield dice_item

