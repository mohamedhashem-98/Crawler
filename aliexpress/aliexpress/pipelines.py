# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class AliexpressPipeline(object):
    def process_item(self, item, spider):
       # print("PipeLine" + item['title'][0])
        return item
