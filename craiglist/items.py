
import scrapy
from scrapy.item import Item, Field

class CraigslistSampleItem(Item):
  title = Field()
  link = Field()
  prize = Field()
  image = Field()
  details = Field()
