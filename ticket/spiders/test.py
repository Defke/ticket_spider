from scrapy import Selector
from scrapy.spiders import CrawlSpider
from ticket.middlewares import TicketInfo
from ticket.items import TicketItem

class Ticket(CrawlSpider):
    def __init__(self):
        pass
        TicketInfo.from_station = input("请输入起始站:")
        TicketInfo.to_station = input("请输入终点站:")
        TicketInfo.train_date = input("请输入出发日期:")
    name ="ticket"
    start_urls =['https://www.12306.cn']
    def parse(self,response):
        selector = Selector(response)
        cree=selector.xpath('//div[@class="t-list"]/table/tbody[@id="queryLeftTable"]/tr[@class]')
        for tr in cree :
            train=tr.xpath(".//div[@class='train']/div/a/text()").extract()
            from_stataion=tr.xpath(".//div[@class='cdz']/strong/text()").extract()[0]
            to_stataion=tr.xpath(".//div[@class='cdz']/strong/text()").extract()[-1]
            beginTime =tr.xpath(".//div[@class='cds']/strong[@class='start-t']/text()").extract()
            endTime = tr.xpath(".//div[@class='cds']/strong[@class='color999']/text()").extract()
            spendTime = tr.xpath(".//div[@class='ls']/strong/text()").extract()[0]
            businessSeat = tr.xpath("./td[@hbdata]/.//text()").extract()[0]
            firstClassSeat = tr.xpath("./td[@hbdata]/.//text()").extract()[1]
            seleniumClassSeat = tr.xpath("./td[@hbdata]/.//text()").extract()[2]
            noSeat =tr.xpath("./td[@hbdata]/.//text()").extract()[-2]
            item= TicketItem()
            item['Train'] = train
            item['FromStation'] = from_stataion
            item['ToStation'] = to_stataion
            item['BeginTime'] = beginTime
            item['EndTime'] = endTime
            item['SpendTime'] = spendTime
            item['BusinessSeat'] = businessSeat
            item['FirstClassSeat'] = firstClassSeat
            item['EconomicClassSeat'] = seleniumClassSeat
            item['NoSeat'] = noSeat
            yield item
