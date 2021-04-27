# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    click_count = scrapy.Field()
    location = scrapy.Field()
    type = scrapy.Field()
    show_time = scrapy.Field()
    grade = scrapy.Field()
    link = scrapy.Field()

