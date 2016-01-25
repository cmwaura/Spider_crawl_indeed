# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem


import os
import re
import json



class RedJsonPipeline(object):

    def __init__(self):
        self.file = open('indeed.json', 'wb')
        self.dice_file = open('dice.json', 'wb')
        # self.spider = RedScrapSpider()

    def process_item(self, item, spider):
        '''

        :param item: parsed data/objects
        :param spider: the spider that was referenced as the parser
        :return: a json file

        '''
        if spider.name == 'indeed':
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
        elif spider.name == 'Dice':
            line = json.dumps(dict(item)) + "\n"
            self.dice_file.write(line)
        else:
            return "spider not found"

        return item



