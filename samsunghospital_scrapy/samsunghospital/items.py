# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SamsunghospitalItem(scrapy.Item):
    title = scrapy.Field()
    definition = scrapy.Field()
    cause = scrapy.Field()
    symptoms = scrapy.Field()
    diagnosis = scrapy.Field()
    treatment = scrapy.Field()
    progress = scrapy.Field()
    prevention = scrapy.Field()
