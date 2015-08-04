from scrapy.spiders import Spider
from scrapy.selector import Selector
import duckduckgo

from find_users.items import Website


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]

    user_name="";


    def __init__(self, user_name):
      #super(DmozSpider, self).__init__(*args, **kwargs)
      self.user_name = user_name;
      self.start_urls = [
        "https://github.com/"

    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        #sites = sel.xpath('//ul[@class="directory-url"]/li')
        items = []


    def generate_links(self):
        print self.user_name;
        r = duckduckgo.query('DuckDuckGo')
        self.start_urls.append('data');
        print self.start_urls;


emp1 = DmozSpider("My name");
emp1.generate_links();


