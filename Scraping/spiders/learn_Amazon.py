import scrapy
import pandas as pd 


class LearnSpider(scrapy.Spider):
    name = "amazon"
    # allowed_domains = ["quotes.toscrape.com"] 
    start_urls = ["https://www.amazon.in/dp/B0D2HVJQRX"]

    def parse(self, response):
        # 4** -> uder side error 
        # 5** -> server side error 
        # Assuming response is 200. 
        # csv_data =[] 
        # for data in  response.xpath('.//div[@id="titleSection"]') : 
          title  = response.xpath('.//div[@id="titleSection"]/h1/span/text()').extract()
          rating = response.xpath('.//div[@id="centerCol"]//div[@id="averageCustomerReviews"]//span[@class="a-size-base a-color-base"]/text()').extract() 
          
          print(title,rating)
        
                
            
