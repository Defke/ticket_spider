# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time

from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TicketInfo():
    to_station = ''
    from_station = ''
    train_date = ''

class SeleniumMiddleware():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="E:\\chromedriver")
    def process_request(self,request,spider):
        driver = self.driver
        driver.get(request.url)
        time.sleep(5)
        driver.find_element_by_id("fromStationText").click()
        time.sleep(1)
        driver.find_element_by_id("fromStationText").send_keys(TicketInfo.from_station)
        time.sleep(1)
        driver.find_element_by_id("fromStationText").send_keys(Keys.ENTER)
        driver.find_element_by_id("toStationText").click()
        driver.find_element_by_id("toStationText").send_keys(TicketInfo.to_station)
        time.sleep(1)
        driver.find_element_by_id("toStationText").send_keys(Keys.ENTER)
        driver.execute_script("document.getElementById('train_date').removeAttribute('readonly');")
        driver.find_element_by_id("train_date").clear()
        driver.find_element_by_id("train_date").send_keys(TicketInfo.train_date)
        driver.find_element_by_id("train_date").click()
        driver.find_element_by_id("train_date").send_keys(Keys.TAB)
        driver.execute_script("document.getElementsByClassName('cal-wrap')[0].style.display='none';")
        driver.find_element_by_css_selector("[class='btn btn-primary form-block']").click()
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        time.sleep(5)
        return HtmlResponse(url=request.url, body=driver.page_source, request=request, encoding='utf-8',
                            status=200)


class TicketSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TicketDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
