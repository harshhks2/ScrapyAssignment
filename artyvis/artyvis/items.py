# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JewelryItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    image_url = scrapy.Field()

class NameItem(scrapy.Item):
    name = scrapy.Field()

class DetailsItem(scrapy.Item):
    details_page = scrapy.Field()

class PriceItem(scrapy.Item):
    price = scrapy.Field()


