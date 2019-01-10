# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class TicketItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Train = Field()
    FromStation = Field()
    ToStation = Field()
    BeginTime = Field()
    EndTime = Field()
    SpendTime = Field()
    BusinessSeat = Field()
    FirstClassSeat = Field()
    EconomicClassSeat = Field()
    NoSeat = Field()
    BusinessPrice = Field()
    FirstClassPrice = Field()
    EconomicClassPrice = Field()
    NoSeatPrice = Field()
    pass
