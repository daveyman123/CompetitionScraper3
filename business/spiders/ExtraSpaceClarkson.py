import scrapy
import csv
from scrapy.selector import Selector
from business.items import TesttestItem
from business import settings
import datetime
import re
class MySpider(scrapy.Spider):
	name = "ExtraSpaceClarkson"
	
	allowed_domains = ['https://www.extraspace.com']
	start_urls = ['https://www.extraspace.com/Storage/Facilities/US/Missouri/Ellisville/1000000675/Facility.aspx']

	def parse(self, response):
		titles = response.css('.u-other , .u-popular')
                outside_units = ["5' x 5'","5' x 10'","5' x 15'","8' x 10'","10' x 10'","10' x 20'","10' x 25'","10' x 30'","10' x 24'", "10' x 15'"]
                inside_units = ["5' x 5'", "5' x 10'", "10' x 10'", "10' x 15'"]
                inside = "Indoor"
                outside = "Outdoor"
                
		yield {'date': datetime.datetime.now().strftime("%m-%d"),
                       'name': "ExtraSpace"
                       }
		for i in titles:
                    item = TesttestItem()
                    item ["special"] = i.css(".promo::text").extract_first()
		    stuff = i.css(".strikeout+ .rate div::text").extract_first()
                    
		    if stuff != None:
   		    	    type = i.css("li:nth-child(2)::text").extract_first()
                            typez = i.css("li::text").extract_first()
                            type2 = typez + type

		    
                            
                            print "second logic"
                            yield {
                            
                        'special': i.css(".promo::text").extract_first(),
                        'types': type2,
                        'size': i.css(".RamaGothicSemiBold div:nth-child(1)::text").extract_first(),  
                        'rate': i.css(".strikeout+ .rate div::text").extract_first()
                        }
                
                
                

