import scrapy
import pandas as pd 


class LearnSpider(scrapy.Spider):
    name = "learn"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        # 4** -> uder side error 
        # 5** -> server side error 
        # Assuming response is 200. 
        csv_data = []
        for box in response.xpath('.//div[@class="quote"]'):
            title = ''.join(box.xpath('./span[@class="text"]/text()').extract())
            author = ''.join(box.xpath('./span/small[@class="author"]/text()').extract())
            # tags = box.xpath('./div[@class="tags"]/a[@class="tag"]/text()').extract() # return all possible tags in a list 
            print('title', title)
            print('author', author)
            # ['change', 'deep-thoughts' ......]
            tag_info = []
            for lis in box.xpath('./div[@class="tags"]/a') :
                tag_link = ''.join(lis.xpath("./@href").extract())
                tag_text = ''.join(lis.xpath("./text()").extract())
                # tag = tag_text+","+tag_link
                tag = ' * '.join([tag_text, tag_link])
                tag_info.append(tag)
            tag_info = '|'.join(tag_info)
            print(tag_info)

            data = [title, author, tag_info]
            csv_data.append(data)

        csv_data = pd.DataFrame(csv_data, columns = ['Title', 'Author', 'Tags']) 
        print(csv_data)
        csv_data.to_csv('learn_test.csv', index=False, encoding="utf-8")
        
                
            
