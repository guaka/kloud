from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item
from solarproject.items import SolarprojectItem
from scrapy.spider import BaseSpider
from scrapy import log
import scrapy.shell
import urlparse

class TestSpider(CrawlSpider):
    name = "test"
    allowed_domains = ["www.solarshop.net"]
    start_urls = ["http://www.solarshop.net/"]
    rules = [
        Rule(SgmlLinkExtractor(allow=("product_info\.php", )), callback='parse_item', follow=True),
        Rule(SgmlLinkExtractor(), callback='parse_rest', follow=True),
    ]

    def parse_rest(self,response):
        self.log('A response from %s just arrived!' % response.url)


    def parse_item(self,response):
        self.log('PRODUCT: A response from %s just arrived!' % response.url)
        hxs = Selector(response)
        item = SolarprojectItem()

        parsed = urlparse.urlparse(response.url)
        params = dict(urlparse.parse_qsl(parsed.query))
        print params
        item['id'] = params['products_id']
        item['name'] = hxs.select("//h1/text()").extract()
        item['sku'] = hxs.select("//table/tr[6]/td[3]/text()").extract()
        item['price'] = hxs.select("//table/tr[2]/td[3]/span/text()").extract()
        # scrapy.shell.inspect_response(response)

        return item
    
