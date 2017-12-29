import scrapy
from scrapy.selector import Selector
from business.items import TesttestItem
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
import re
import time
from pyvirtualdisplay import Display
from pyvirtualdisplay import Display


outside_units = ["5' x 5'", "5' x 10'","8' x 10'", "10' x 8'", "10' x 15'","5' x 15'", "10' x 24'", "10' x 20'", "10' x 24'","10' x 10'","10' x 25'","10' x 30'","5 x 5", "5 x 10","8 x 10", "10 x 8", "10 x 15","5 x 15", "10 x 24", "10 x 20", "10 x 24","10 x 10","10 x 25","10 x 30",]
class MySpider1(scrapy.Spider):
        name = "PublicStorageDoug2"
	
	
 
	
	allowed_domains = ['https://www.publicstorage.com']
	start_urls = ['https://www.publicstorage.com/missouri/self-storage-st-charles-mo/63303-self-storage/1007?lat=38.79101&lng=-90.55954&location=st+peters']

	def parse(self, response):
		def cleanhtml(raw_html):
 	                cleanr = re.compile('<.*?>')
        	        cleantext = re.sub(cleanr, '', raw_html)
                	return cleantext

                display = Display(visible=0, size=(800, 600))
                display.start()

                url='https://www.publicstorage.com/missouri/self-storage-st-charles-mo/63303-self-storage/1007?lat=38.79101&lng=-90.55954&location=st+peters'
                driver = webdriver.Firefox()
                driver.get(url)

		#url2='http://www.a1lockerrental.com/self-storage/mo/st-louis/4427-meramec-bottom-rd-facility/unit-sizes-prices#/units?category=all'
		#driver2 = webdriver.Firefox()
                #driver2.get(url2)
                #html2 = driver.page_source
                #soup2 = BeautifulSoup(html2, 'html.parser')                
                #soup.append(soup2)
                #print soup
		items = []
		inside = "Indoor"
                outside = "Outdoor"
		inside_units = ["5 x 5", "5 x 10"]
		
		
		#print soup.findAll('span',{"class":"sss-unit-size"})
		
                
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
#                time.sleep(3)
                sizeTagz = soup.findAll('div',{"class":"srp_label srp_font_14"})
		
		
		rateTagz = soup.findAll('div',{"class":"srp_label alt-price"})
#		specialTagz2 = soup.findAll('div',{"class":"srp_res_clm srp_clm90"})[0]
                #specialTag = specialTagz2.findAll('div',{"class":"srp_v-space_10"})
#                x = []
 #               for foo in specialTagz2:
  #                      bar = foo.find('div',{"class":"srp_label"}).get_text(strip=True)
#			if bar != None or bar != "":
 #                       	x.append(bar)
  #              print len(x)
	#	specialTagz2 = soup.findAll('div',{"class":"srp_res_clm srp_clm90"})
                #specialTag = specialTagz2.findAll('div',{"class":"srp_v-space_10"})
         
                #specialTagz2 = soup.findAll(True, {'class':['srp_res_clm srp_clm90', 'srp_label']})
#		specialTagz2 = soup.findAll('div',{"class":"srp_v-space_10"})
	#	spec = []
		#for i in specialTagz:
	#
	#		specialTagz2 = i.findAll('div',{"class":"srp_label"})
	#		spec.append(specialTagz2.get_text())
#		specialTagz2 = soup.select('div.srp_res_clm srp_clm90,div.srp_label')
		typesTagz = soup.findAll('ul',{"class":"srp_list"},)
		
		yield {'date': datetime.datetime.now().strftime("%m-%d"),
                'name': "Public Storage"
                       }
		size = []
		for n in range(len(sizeTagz)):
                        print len(sizeTagz)
#			print len(x)
 #                       spec = x[n]
#			print spec
			#spec = soup.get_text()
                        #print (rateTagz[n]).get_text()
                        #special = re.sub(r"(?<=[a-z])\r?\n"," ",(specialTagz2[n]).get_text())
			#if "Online" in special:
			#	special = "None"
                        if "Outside" in (typesTagz[n]).get_text():
                                #if (sizeTagz[n]).get_text() in outside_units:
                                 #       if (sizeTagz[n]).get_text() not in size:
                        	size.append((sizeTagz[n]).get_text())
                                #size.append(re.findall(r'\d+',(sizeTagz2[n]).get_text()))
                                #                print "logic hit"
                
                                yield {
                        #soup.findAll('p',{"class":"icon-bg"})
                        #'name': soup.find('strong', {'class':'high'}).text
                       
                #.replace('\n', '')
                        "special": "Incomplete",
                        "rate": (rateTagz[n]).get_text(),
                        'size': ((sizeTagz[n]).get_text()),
                        "types": "Outside"
	
		}
class MySpider2(scrapy.Spider):
        name = "LifeStorageDoug2"

        
	
	allowed_domains = ['https://www.lifestorage.com']
	start_urls = ['https://www.lifestorage.com/storage-units/missouri/saint-louis/63376/460-in-saint-peters/?size=5x5']

	def parse(self, response):
		
		display = Display(visible=0, size=(800, 600))
                display.start()
               
                    #print newString
                def replacenth(s, sub, repl, nth):
                    find = s.find(sub)
                    # if find is not p1 we have found at least one match for the substring
                    i = find != -1
                    # loop util we find the nth or we find no match
                    while find != -1 and i != nth:
                        # find + 1 means we start at the last match start index + 1
                        find = s.find(sub, find + 1)
                        i += 1
                    # if i  is equal to nth we found nth matches so replace
                    if i == nth:
                        return s[:find]+repl+s[find + len(sub):]
                    return s
                url='https://www.lifestorage.com/storage-units/missouri/saint-louis/63376/460-in-saint-peters/?size=5x5'
                driver = webdriver.Firefox()
                driver.get(url)

		#url2='http://www.a1lockerrental.com/self-storage/mo/st-louis/4427-meramec-bottom-rd-facility/unit-sizes-prices#/units?category=all'
		#driver2 = webdriver.Firefox()
                #driver2.get(url2)
                #html2 = driver.page_source
                #soup2 = BeautifulSoup(html2, 'html.parser')                
                #soup.append(soup2)
                #print soup
		items = []
		inside = "Indoor"
                outside = "Outdoor"
		inside_units = ["5 x 5", "5 x 10"]
		
		
		#print soup.findAll('span',{"class":"sss-unit-size"})
		
                
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                #time.sleep(3)
                sizeTagz = soup.findAll('div',{"class":"storesRow"})
		
		
		rateTagz = soup.findAll('div',{"class":"priceBox"})
		
		
                #specialTagz2 = soup.findAll('div',{"class":"srp_label"})
		
		typesTagz = soup.findAll('ul',{"class":"features"},)
		#s = soup.findAll(True, {'em':['fiftyMessage', 'pOnly']})
		special = soup.findAll('div',{"class":"priceBox"})
		#special = []
		#for tag in s:
		#specialz = tag.find_all("div", {"class": "priceBox"})
		#special.append[specialz]
		yield {'date': datetime.datetime.now().strftime("%m-%d"),
                'name': "Life Storage"
                       }
		size = []
		for n in range(len(sizeTagz)):
                        #print len(sizeTagz)
                        x = (sizeTagz[n]).get_text()
                        specials = special[n]
			specialz = specials.find("div", {"class": "specialsMessage"})
			if specialz != None:
				specialz = specialz.get_text()
				specialz = specialz.replace("\n", "")
			#special = special.find('div', attrs={'class':"specialsMessage"})
                        #x = re.sub('[*]', '', x)
                        #x = x.replace(' ', '')
                        print x
                        #print x
                        #print (rateTagz[n]).get_text()
                        
                        if "Outdoor" in (typesTagz[n]).get_text():
                                #print "Outdoor hit"
                                for sizes in outside_units:
                                        if sizes in x:
                                                
                                 #               print "right size"
                                                if x not in size and re.findall(r'^\D*(\d+)',(rateTagz[n]).get_text()) != []:
                                                        
                                                        
                                #size.append(re.findall(r'\d+',(sizeTagz2[n]).get_text()))
                                  #                      print "logic hit"
                                                        x = re.sub('[*]', '', x)
                                                        x = x.replace(',', 'x')
                                                        x = x.replace(' ', '')
                                                        x = x.replace('8', '')
                                                        x = re.findall(r'\d+', x)
                                                        x = " ".join(str(i) for i in x)
                                                        x = x.replace(' ', 'x')
                                                        if len(x) > 5:
                                                                x = replacenth(x, "x", "/", 2)
                                                        if x not in size:
                                                                size.append(x)
                                                                print x
                                                                print size
                                                              #  s.append("none")
                                                               # try:
                                                               # gotdata = s[n].get_text()
                                                               # except IndexError:
                                                                #        gotdata = 'none'
                                                                yield {
                        #soup.findAll('p',{"class":"icon-bg"})
                        #'name': soup.find('strong', {'class':'high'}).text
                       
                        
                                                                                "special": specialz,
                                                                                "rate": re.findall(r'^\D*(\d+)',(rateTagz[n]).get_text()),
                                                                                'size': x,
                                                                                "types": "Outside"
                                                                                                
                                                
                                        
		}
		
class AStorageInnCave(scrapy.Spider):
	name = "AStorageInnCave"

	allowed_domains = ['http://www.python.org']
	start_urls = ['http://www.python.org']

	def parse(self, response):
                display = Display(visible=0, size=(800, 600))
                display.start()
		#url = "http://www.python.org"
                url='https://www.storageinns.net/self-storage/mo/saint-peters/n-service-road/#/units?category=all'
                driver = webdriver.Firefox()
		#time.sleep(10)
                driver.get(url)
		#time.sleep(10)
		#url2='http://www.a1lockerrental.com/self-storage/mo/st-louis/4427-meramec-bottom-rd-facility/unit-sizes-prices#/units?category=all'
		#driver2 = webdriver.Firefox()
                #driver2.get(url2)
                #html2 = driver.page_source
                #soup2 = BeautifulSoup(html2, 'html.parser')
                #soup.append(soup2)
                #print
                items = []
                inside = "Indoor"
                outside = "Outdoor"
                inside_units = ["5 x 5", "5 x 10"]
		outside_units = ["5 x 6", "10 x 16","6 x 12", "8 x 10","10 x 10","10 x 20","10 x 12","10 x 30","10 x 25", "10 x 12"]
                #outside_units = ["5 x 6", "10 x 16","6 x 12", "8 x 10","10 x 10","10 x 20","10 x 12","10 x 30","10 x 25"]
                driver.execute_script("window.scrollTo(0, 111);")
        		#print soup.findAll('span',{"class":"sss-unit-size"})

                SCROLL_PAUSE_TIME = 0.5
                driver.execute_script("window.scrollTo(0, 444);")
                # Get scroll height
                time.sleep(5)
                #last_height = driver.execute_script("return document.body.scrollHeight")
                driver.execute_script("window.scrollTo(0, 1111);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(0, 2222);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(0, 3333);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(0, 4444);")
                time.sleep(2)

                time.sleep(2)
                driver.execute_script("window.scrollTo(0, 3333);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(0, 4444);")
                time.sleep(2)

                driver.execute_script("window.scrollTo(0, 5555);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(0, 6666);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(0, 7777);")
                time.sleep(2)
               # while True:
                #     Scroll down to bottom
                driver.execute_script("window.scrollTo(0, 9999);")
                time.sleep(5)
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                sizeTagz = soup.findAll('span',{"class":"sss-unit-size"})
        		#sizeTagz2 = soup2.findAll('span',{"class":"sss-unit-size"})

                            # Wait to load page
                            #time.sleep(SCROLL_PAUSE_TIME)
                            #print "loooping"
                            # Calculate new scroll height and compare with last scroll height
                            #new_height = driver.execute_script("return document.body.scrollHeight")
                            #if new_height == last_height:
                             #   break
                            #print "loooping"
                            #last_height = new_height
                            #print "loooping"

                rateTagz = soup.findAll('p',{"class":"price unit-price"})


                specialTagz = soup.findAll('span',{"class":"unit-special-offer"})
                typesTagz = soup.findAll('div',{"class":"unit-info"},)

                #rateTagz2 = soup2.findAll('p',{"class":"unit-special-offer"})


                #specialTagz2 = soup2.findAll('span',{"class":"unit-special-offer"})
                #typesTagz2 = soup2.findAll('div',{"class":"unit-info"},)
                yield {'date': datetime.datetime.now().strftime("%m-%d"),
                'name': "AStorageInnCave"
                   }
                size = []
                for n in range(len(sizeTagz)):

                    Special = (specialTagz[n]).get_text()

                    if "Outside" in (typesTagz[n]).get_text():
                        if (sizeTagz[n]).get_text() in outside_units:
                        	if (sizeTagz[n]).get_text() not in size and "Online" not in Special and Special != "":
                        	    size.append((sizeTagz[n]).get_text())
                        	    yield {"special": Special, "rate": re.findall('\d+\.\d+',(rateTagz[n]).get_text()),
'size': ((sizeTagz[n]).get_text()),
"types": "Outside"

        		}
class ExtraSpaceCave(scrapy.Spider):
	name = "ExtraSpaceDoug22"
	
	allowed_domains = ['https://www.extraspace.com']
	start_urls = ['https://www.extraspace.com/Storage/Facilities/US/Missouri/St._Peters/1000000466/Facility.aspx']

	def parse(self, response):
		info = response.css('.unit')
		items = []
		inside = "Indoor"
                outside = "Outdoor"
		inside_units = ["5' x 5'", "5' x 10'"]
		#outside_units = ["10' x 24'","5' x 5'", "10' x 15'","5' x 6'", "6' x 12'","10' x 10'","10' x 20'","10' x 25'","10' x 30'", "10' x 16'", "10' x 12'", "10' x 14'", "12' x 12'",]
		yield {'date': datetime.datetime.now().strftime("%m-%d"),
                       'name': "Extra Space"
                       }
		for i in info:
		    print len(info)
                    rate = (i.css(".promo::text").extract_first())
                    print len(info)
		   
		    rate2 = i.css(".strikeout+ .rate div::text").extract_first()
		    
                    #rate = remove_tags(rate)
                    #print i.css(".RamaGothicSemiBold div:nth-child(1)::text").extract_first()   
                    if i.css(".RamaGothicSemiBold div:nth-child(1)::text").extract_first() in outside_units and rate2 != None and 'Drive-Up Access' in i.css("li:nth-child(2)::text").extract_first():
                        yield {
			
                                        "special": rate,
                                        "rate": rate2,
                                        "size": i.css(".RamaGothicSemiBold div:nth-child(1)::text").extract_first(),
                                        "types": i.css("li:nth-child(2)::text").extract_first()
	
		}

class StPetersCave(scrapy.Spider):
        name = "StPeters"

        
	
	allowed_domains = ['https://a1ustoreit.net']
	start_urls = ['https://www.lifestorage.com/storage-units/missouri/saint-louis/63376/460-in-saint-peters/']

	def parse(self, response):
                display = Display(visible=0, size=(800, 600))
                display.start()
                url='https://www.lifestorage.com/storage-units/missouri/saint-louis/63376/460-in-saint-peters/'
                driver = webdriver.Firefox()
                driver.get(url)

		#url2='http://www.a1lockerrental.com/self-storage/mo/st-louis/4427-meramec-bottom-rd-facility/unit-sizes-prices#/units?category=all'
		#driver2 = webdriver.Firefox()
                #driver2.get(url2)
                #html2 = driver.page_source
                #soup2 = BeautifulSoup(html2, 'html.parser')                
                #soup.append(soup2)
                #print soup
		items = []
		inside = "Indoor"
                outside = "Outdoor"
		inside_units = ["5 x 5", "5 x 10"]
		#outside_units = ["10' x 15'","5' x 6'", "6' x 12'","10' x 10'","10' x 20'","10' x 25'","10' x 30'", "10' x 16'", "10' x 12'", "10' x 14'", "12' x 12'", "10' x 24'", "10' x 8'"]
		
		#print soup.findAll('span',{"class":"sss-unit-size"})
		
                
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                time.sleep(3)
                sizeTagz = soup.findAll('span',{"class":"sss-unit-size"})
		
		
		rateTagz = soup.findAll('span',{"class":"price-value"})
		
		
                #specialTagz2 = soup.findAll('div',{"class":"srp_label"})
		specialTagz = soup.findAll('span',{"special-text unit-special-offer"})
		#typesTagz = soup.findAll('ul',{"class":"features"},)
		
		yield {'date': datetime.datetime.now().strftime("%m-%d"),
                'name': "St. Peters"
                       }
		size = []
		for n in range(len(sizeTagz)):
                        print len(sizeTagz)
                        x = (sizeTagz[n]).get_text()
                        #x = re.sub('[*]', '', x)
                        #x = x.replace(' ', '')
                        #print x
                        #print x
                        #print (rateTagz[n]).get_text()
                        
                        #if "Outdoor" in (typesTagz[n]).get_text():
                                #print "Outdoor hit"
                        
                        
                        for sizes in outside_units:
                                sizes = sizes.replace("'", '')
                                if sizes in x:
                                 #               print "right size"
                                        if x not in size:
                                
                                                size.append(x)
                                #size.append(re.findall(r'\d+',(sizeTagz2[n]).get_text()))
                                  #                      print "logic hit"
                                                x = re.sub(',', 'x', x)
                                                x = re.findall(r'\d+', x)
                                                x = " ".join(str(i) for i in x)
                                                x = x.replace(' ', 'x')
                                                        #x = x.replace(' ', '')
                                                yield {
                        #soup.findAll('p',{"class":"icon-bg"})
                        #'name': soup.find('strong', {'class':'high'}).text
                       
                
                        "special": specialTagz[n].get_text(),
                        "rate": re.findall(r'^\D*(\d+)', rateTagz[n].get_text()),
                        'size': x,
                        "types": "Outside"
	
		}

class AStorageInnCave(scrapy.Spider):
	name = "AStorageInnCave"

	allowed_domains = ['http://www.python.org']
	start_urls = ['http://www.python.org']

	def parse(self, response):
                display = Display(visible=0, size=(800, 600))
                display.start()
		#url = "http://www.python.org"
                url='https://www.storageinns.net/self-storage/mo/saint-peters/n-service-road/#/units?category=all'
                driver = webdriver.Firefox()
		#time.sleep(10)
                driver.get(url)
		#time.sleep(10)
		#url2='http://www.a1lockerrental.com/self-storage/mo/st-louis/4427-meramec-bottom-rd-facility/unit-sizes-prices#/units?category=all'
		#driver2 = webdriver.Firefox()
                #driver2.get(url2)
                #html2 = driver.page_source
                #soup2 = BeautifulSoup(html2, 'html.parser')
                #soup.append(soup2)
                #print
                items = []
                inside = "Indoor"
                outside = "Outdoor"
                inside_units = ["5 x 5", "5 x 10"]
                outside_units = ["5 x 6", "10 x 16","6 x 12", "8 x 10","10 x 10","10 x 20","10 x 12","10 x 30","10 x 25", "10 x 12"]
                driver.execute_script("window.scrollTo(0, 111);")
        		#print soup.findAll('span',{"class":"sss-unit-size"})

                SCROLL_PAUSE_TIME = 0.5
                driver.execute_script("window.scrollTo(0, 444);")
                # Get scroll height
                time.sleep(5)
                #last_height = driver.execute_script("return document.body.scrollHeight")
                driver.execute_script("window.scrollTo(0, 1111);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(0, 2222);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(0, 3333);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(0, 4444);")
                time.sleep(2)

                time.sleep(2)
                driver.execute_script("window.scrollTo(0, 3333);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(0, 4444);")
                time.sleep(2)

                driver.execute_script("window.scrollTo(0, 5555);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(0, 6666);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(0, 7777);")
                time.sleep(2)
               # while True:
                #     Scroll down to bottom
                driver.execute_script("window.scrollTo(0, 9999);")
                time.sleep(5)
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                sizeTagz = soup.findAll('span',{"class":"sss-unit-size"})
        		#sizeTagz2 = soup2.findAll('span',{"class":"sss-unit-size"})

                            # Wait to load page
                            #time.sleep(SCROLL_PAUSE_TIME)
                            #print "loooping"
                            # Calculate new scroll height and compare with last scroll height
                            #new_height = driver.execute_script("return document.body.scrollHeight")
                            #if new_height == last_height:
                             #   break
                            #print "loooping"
                            #last_height = new_height
                            #print "loooping"

                rateTagz = soup.findAll('p',{"class":"price unit-price"})


                specialTagz = soup.findAll('span',{"class":"unit-special-offer"})
                typesTagz = soup.findAll('div',{"class":"unit-info"},)

                #rateTagz2 = soup2.findAll('p',{"class":"unit-special-offer"})


                #specialTagz2 = soup2.findAll('span',{"class":"unit-special-offer"})
                #typesTagz2 = soup2.findAll('div',{"class":"unit-info"},)
                yield {'date': datetime.datetime.now().strftime("%m-%d"),
                'name': "AStorageInnCave"
                   }
                size = []
                for n in range(len(sizeTagz)):

                    Special = (specialTagz[n]).get_text()

                    if "Outside" in (typesTagz[n]).get_text():
                        if (sizeTagz[n]).get_text() in outside_units:
                        	if (sizeTagz[n]).get_text() not in size and "Online" not in Special and Special != "":
                        	    size.append((sizeTagz[n]).get_text())
                        	    yield {"special": Special, "rate": re.findall('\d+\.\d+',(rateTagz[n]).get_text()),
'size': ((sizeTagz[n]).get_text()),
"types": "Outside"

        		}
                        driver.close()

                
