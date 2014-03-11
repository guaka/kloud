# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class SolarprojectItem(Item):
    # define the fields for your item here like:
    id = Field()
    name = Field()
    price = Field()
    sku = Field()
    modellname = Field()
    schutzgrad = Field()

