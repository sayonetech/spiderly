import re

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from lxml import html

from test_project.items import CraigslistSampleItem
from scrapy.http import Request


class MySpider(BaseSpider):
    name = "craig"
    allowed_domains = ["craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/npo/"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.xpath("//span[@class='pl']")
        for titless in titles[41:42]:
            link = titless.xpath("a/@href").extract()
            url = 'http://sfbay.craigslist.org/'+link[0]
            yield Request(url=url, callback=self.parse_details)

    def parse_details(self, response):
        doc = html.fromstring(response.body)
        item = CraigslistSampleItem()
        item['title'] = doc.xpath('.//span[@class="postingtitletext"]')[0].text_content()
        if doc.xpath('.//div[@class="slide first visible"]//img/@src'):
          item['image']  = doc.xpath('.//div[@class="slide first visible"]//img/@src')[0]
        item['details'] = re.sub('\n|\t', '', doc.find('.//section[@id="postingbody"]').text_content())
        yield item
