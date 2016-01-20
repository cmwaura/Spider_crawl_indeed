# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
# import pandas as pd
import os
import re
import json


# class RedDuplicatePipeline(object):
#     def __init__(self):
#         self.seen_quantity = set()
#
#     def process_item(self, item, spider):
#         # if item['quantity'] in self.seen_quantity:
        #     raise DropItem("duplicate item found:%s" % item)
        # else:
        #     self.seen_quantity.add(item['quantity'])


        # yield item

class RedJsonPipeline(object):

    def __init__(self):
        self.file = open('items.json', 'wb')

    def process_item(self, item, spider):
        '''

        :param item: parsed data/objects
        :param spider: the spider that was referenced as the parser
        :return: a json file

        '''
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item



