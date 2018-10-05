#scrapy runspider spider.py -o teste1.json

import scrapy

class ScratchSpiders(scrapy.Spider):
	name = 'scratchspider'
	
	def start_requests(self):
		num_event = 10000
		for i in range(1, num_event):
				yield scrapy.Request('https://day.scratch.mit.edu/events/{}'.format(i), self.parse)

	def parse(self, response):
		yield{
			'Event': response.xpath('//*[@id="event-name"]/text()').extract(),
			'Host': response.xpath('//*[@id="event-display"]/div/article[1]/div/header/p/a/span/text()').extract(),
			'Date': response.xpath('normalize-space(//*[@id="event-when"]/time/text())').extract(),
			'Address': [i.strip() for i in response.xpath('//*[@id="details"]/li/div[1]/address//text()').extract()],
			'About': response.xpath('//*[@id="event-description"]/p/text()').extract(),
			'Plans': [i.strip() for i in response.xpath('//*[@id="event-plans"]//text()').extract()],
			'Costs': [i.strip() for i in response.xpath('//*[@id="event-cost"]/text()').extract()],
			'Mail': response.xpath('//*[@id="host-email-link"]/@href').extract(),
			'Registration': response.xpath('normalize-space(//*[@id="event-registration"]/text())').extract(),
			'Host_info': response.xpath('//*[@id="author"]/li/div/p[1]/text()').extract(),
			'User': response.xpath('//*[@id="event-display"]/div/article[1]/div/header/p/a/span/text()').extract(),
			'Organization': response.xpath('//*[@id="author"]/li/div/p[2]/text()').extract(),
			'Organization Website': response.xpath('//*[@id="author"]/li/div/p[3]/a/@href').extract(),
			'URL': response.url
		}