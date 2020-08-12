import scrapy
from scrapy_splash import SplashRequest
from ..items import SamsunghospitalItem


class QuotesSpider(scrapy.Spider):
    name = 'sh'
    start_urls = [
        'http://www.samsunghospital.com/home/healthInfo/content/contentList.do?CONT_CLS_CD=001020001&TAB=DIS_NM'
    ]

    def parse(self, response):
        for i in range(1, 581):
            url_content = response.css('.card-item:nth-child({}) a::attr(href)'.format(i)).get()
            yield SplashRequest(response.urljoin(url_content), callback=self.parse_doc, args={'wait': 0.5})

    def parse_doc(self, response):
        items = SamsunghospitalItem()
        title = response.css('h1 strong::text').extract()
        definition = response.css('.img::text').extract()
        cause = response.css('.cont:nth-child(4)::text').extract()
        symptoms = response.css('.cont:nth-child(6)::text').extract()
        diagnosis = response.css('.cont:nth-child(8)::text').extract()
        treatment = response.css('.cont:nth-child(10)::text').extract()
        progress = response.css('.cont:nth-child(12)::text').extract()
        prevention = response.css('.cont:nth-child(14)::text').extract()

        items['title'] = title
        items['definition'] = [s.strip() for s in definition]
        items['cause'] = [s.strip() for s in cause]
        items['symptoms'] = [s.strip() for s in symptoms]
        items['diagnosis'] = [s.strip() for s in diagnosis]
        items['treatment'] = [s.strip() for s in treatment]
        items['progress'] = [s.strip() for s in progress]
        items['prevention'] = [s.strip() for s in prevention]
        yield items
