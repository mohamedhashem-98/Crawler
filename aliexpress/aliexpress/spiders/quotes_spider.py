import  scrapy
from ..items import AliexpressItem
class QuoteSpyder(scrapy.Spider):
    name = 'Quotes'  #Spider name
    start_urls = [
        'http://quotes.toscrape.com/'
    ]  #list of urls we want to start crawel from them

    def parse(self, response):
        # To Store data in Temp class
        items = AliexpressItem()
        #title = response.css('title::text').extract()  #To get Page title
        #yield {'titletext' : title}
        all_div_quotes = response.css("div.quote")
        for quote in all_div_quotes:
            title = quote.css("span.text::text").extract()
            author = quote.css(".author::text").extract()
            tags   = quote.css('.tag::text').extract()
            items['title'] = title
            items['author'] = author
            items['tags'] = tags

            yield items

        # To navigate next_pages
        next_page = response.css("li.next a").xpath('@href').get()
        if next_page is not None:
            yield response.follow(next_page , callback=self.parse)




        # title = all_div_quotes.css("span.text::text").extract()
        # author = all_div_quotes.css("span small.author::text").extract()
        # tags   = all_div_quotes.css('.tag::text').extract()
        # yield {
        #     'title' : title ,
        #     'author' : author ,
        #     'tags'  : tags
        # }

# To run scrapy shell
    # scrapy shell "url"

# To save data in json file
# write in command
  # scrapy crawl Quotes -o items.json
  # if want csv or xml items.csv or items.xml