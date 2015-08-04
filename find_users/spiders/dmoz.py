from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.items import Website


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "https://github.com/"

    ]
    user_name="";


    def __init__(self, user_name):
      #super(DmozSpider, self).__init__(*args, **kwargs)
      self.user_name = user_name;

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


emp1 = DmozSpider("My name");
emp1.generate_links();


